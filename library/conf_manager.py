import os
import json
import importlib.util

from library.file import File


class ConfManager:
	def __init__(self, base_path):
		self.constants      = {}
		self.variables      = None
		self.path           = File.path(base_path, 'conf')
		self.constants_path = File.path(base_path, 'conf', 'constants.json')
		self.variables_path = File.path(base_path, 'conf', 'variables.py')
		self.isInitialized  = False

	######################### PRIVATE #######################

	def _init(self):
		if not self.isInitialized:
			if not File.exists(self.path):
				File.mkdir(self.path)

			File.mkfile(self.constants_path, '{}')
			File.mkfile(self.variables_path, 'class Variables:\n\t...')

			self._read_constants()
			self._read_variables()
			self.isInitialized = True

	def _read_constants(self):
		contents = File.read(self.constants_path)
		self.constants = json.loads(contents)

	def _read_variables(self):
		if File.exists(self.variables_path):
			spec   = importlib.util.spec_from_file_location('variables', self.variables_path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			self.variables = module.Variables()
		else:
			print(f'Warning: "{path}" does not exist.')

	######################### PUBLIC #########################

	def create(self):
		self._init()

	def get(self, name, default=None):
		self._init()

		# Search in constants
		value = self.constants.get(name, None)
		if value is not None:
			return value
		
		# Search in variables
		if self.variables:
			value = self.variables.get(name, None)
			if value is not None:
				return value
		
		# Return default if name not found in either
		return default

	def apply(template_content):
		self._init()
		pattern = re.compile('$namespace.' + r'\.(([a-zA-Z]+[a-zA-Z0-9_]*)')
		
		def replace_var(match):
			return self.get(match.group(1), '')
			
		return pattern.sub(replace_var, template_content)
