import os
import sys

from library.files          import Files
from library.config_manager import ConfigManager


class Namespace(ConfigManager):
	def __init__(self, name):
		self.name     = name
		self.base_dir = os.path.join('ROOT_DIR', 'namespaces', self.name)
		super().__init__(self.base_dir)  # Call ConfigManager constructor with base_dir

	def create(self):
		try:
			# Create namespace directory
			Files.mkdir(self.base_dir)
			
			# Paths for constants.json and variables.py
			constants_path = os.path.join(self.base_dir, 'constants.json')
			variables_path = os.path.join(self.base_dir, 'variables.py')

			# Create empty constants.json file
			with open(constants_path, 'w') as f:
				f.write('{}')

			# Create empty variables.py file
			with open(variables_path, 'w') as f:
				f.write('# variables.py')

			print(f'Created Namespace "{self.name}" with empty constants.json and variables.py')
			return self
		except Exception as e:  # SeedError was used, replaced with a general Exception for this example
			print(f'Error creating namespace: {e}', file=sys.stderr)
			# Implement or import NoOp() as appropriate
			return None  # Replace with NoOp() as per your implementation
