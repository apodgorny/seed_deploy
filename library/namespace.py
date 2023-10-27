import os
import sys

from library.files          import Files
from library.config_manager import ConfigManager
from library.seed_error     import SeedError


class Namespace(ConfigManager):
	def __init__(self, name):
		self.name           = name
		self.namespace_path = os.path.join('namespaces', self.name)
		super().__init__(self.namespace_path)  # Call ConfigManager constructor with base_dir

	def create(self):
		try:
			# Create namespace directory
			Files.mkdir(self.namespace_path)
			
			# Paths for constants.json and variables.py
			constants_path = os.path.join(self.namespace_path, 'constants.json')
			variables_path = os.path.join(self.namespace_path, 'variables.py')

			# Create empty constants.json file
			with open(constants_path, 'w') as f:
				f.write('{}')

			# Create empty variables.py file
			with open(variables_path, 'w') as f:
				f.write('# variables.py\nclass Variables:\n\t...')

			print(f'Created Namespace "{self.name}" with empty constants.json and variables.py')
			return self
		except Exception as e:  # SeedError was used, replaced with a general Exception for this example
			print(f'Error creating namespace: {e}', file=sys.stderr)
			# Implement or import NoOp() as appropriate
			return None  # Replace with NoOp() as per your implementation


	def delete(self):
		try:
			Files.rm(self.namespace_path)
		except SeedError as e:
			SeedError.error_exit(str(e))
		print(f'Deleted Namespace "{self.name}".')
		return self