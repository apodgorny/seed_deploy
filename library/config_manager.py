import os
import json
import importlib.util

class ConfigManager:
	def __init__(self, config_path):
		self.constants   = {}
		self.variables   = None
		self.config_path = config_path
		self.constants_file_path = os.path.join(self.config_path, 'constants.json')
		self.variables_file_path = os.path.join(self.config_path, 'variables.py')
		self._read_constants()
		self._import_and_init_variables()

	######################### PRIVATE #######################

	def _read_constants(self):
		if os.path.exists(self.constants_file_path):
			with open(self.constants_file_path, 'r') as f:
				self.constants = json.load(f)
		else:
			print('Warning: constants.json not found in the specified directory.')

	def _import_and_init_variables(self):
		if os.path.exists(self.variables_file_path):
			spec = importlib.util.spec_from_file_location('variables', self.variables_file_path)
			variables_module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(variables_module)
			self.variables = variables_module.Variables()
		else:
			print('Warning: variables.py not found in the specified directory.')

	######################### PUBLIC #########################

	def get(self, name, default=None):
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

# Usage
# config_manager = ConfigManager('/path/to/your/directory')
# result = config_manager.get('some_key', 'default_value')
# print(result)
