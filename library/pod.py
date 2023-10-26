# – Pod
# 	create(pod_name)
# 	delete()
# 	addTemplate(template_name)
# 	deleteTemplate(template_name)
# 	build(namespace_name) –> build_id
# 	deploy(namespace_name)


import os
import sys

from library.files      import Files
from library.seed_error import SeedError
from library.no_op      import NoOp


class Pod:
	def __init__(self, name):
		self.name           = name
		self.pod_path       = f'pod_sets/{self.name}'
		self.templates_path = f'{self.pod_path}/templates'
		self.build_path     = f'{self.pod_path}/build'
		self.conf_path      = f'{self.pod_path}/conf'

	######################### PUBLIC #########################

	def create(self):
		try:
			Files.mkdir(self.pod_path)
			Files.mkdir(self.templates_path)
			Files.mkdir(self.build_path)
			Files.mkdir(self.conf_path)

			with open(f'{self.conf_path}/constants.json', 'w') as f:
				f.write('{}')

			with open(f'{self.conf_path}/variables.py', 'w') as f:
				f.write('# variables.py')

			return self
		except SeedError as e:
			print(f'Error creating pod: {e}', file=sys.stderr)
			return NoOp()

	def delete(self):
		try:
			Files.rm(self.pod_path)
			return self
		except SeedError as e:
			print(f'Error deleting pod: {e}', file=sys.stderr)
			return NoOp()

	def create_template(self, name):
		template_path = f'{self.templates_path}/{name}.yaml'
		try:
			with open(template_path, 'w') as f:
				pass  # Create an empty file
			return self
		except Exception as e:
			print(f'Error creating template: {e}', file=sys.stderr)
			return NoOp()

	def delete_template(self, name):
		template_path = f'{self.templates_path}/{name}.yaml'
		if Files.exists(template_path):
			os.remove(template_path)
			return self
		else:
			print(f'Template {name} does not exist', file=sys.stderr)
			return NoOp()

	def build(self, namespace_names):
		# TODO: Add logic to build the pod for the given namespace names
		return self  # Assuming successful for now

	def deploy(self, namespace_names):
		# TODO: Add logic to deploy the pod to the given namespace names
		return self  # Assuming successful for now
