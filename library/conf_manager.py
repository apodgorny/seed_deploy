import re
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

	######################### PRIVATE #######################

	def _init(self, additional_values=None):
		additional_values = additional_values if additional_values else {}
		if not File.exists(self.path):
			File.mkdir(self.path)
			constants = json.loads(File.read('templates/constants.json'))
			constants.update(additional_values)
			File.write(self.constants_path, json.dumps(constants))
			File.write(self.variables_path, File.read('templates/variables.py'))

		self._read_constants()
		self._read_variables()

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
			print(f'Warning: "{self.path}" does not exist.')

	######################### PUBLIC #########################

	def create(self, additional_values=None):
		self._init(additional_values)

	def get(self, name, default=None):
		self._init()
		
		# Search in constants
		if name in self.constants:
			return self.constants[name]

		# Search in variables
		if self.variables:
			value = self.variables.get(name, None)
			if value is not None:
				return value
		
		return default

	def get_constants(self):
		return json.loads(File.read(self.constants_path))

	def apply(self, template_content):
		self._init()
		pattern = re.compile('$namespace.' + r'\.(([a-zA-Z]+[a-zA-Z0-9_]*)')
		
		def replace_var(match):
			return self.get(match.group(1), '')
			
		return pattern.sub(replace_var, template_content)
