import os
import sys

from settings import *

from library.file         import File
from library.seed_error   import SeedError
from library.no_op        import NoOp
from library.conf_manager import ConfManager


class Pod:
	def __init__(self, pod_set, name):
		self.name           = name
		self.pod_set        = pod_set
		self.path           = File.path(PODSETS_DIR_NAME, pod_set.name, self.name)
		self.conf           = ConfManager(self.path)
		self.build_path     = File.path(self.path, 'build')
		self.templates_path = File.path(self.path, 'templates')

	######################### PRIVATE ########################

	def _guard(self):
		if not File.exists(self.path):
			SeedError.error_exit(f'PodSet "{self.name}" does not exist.')

	######################### PUBLIC #########################

	def create(self):
		try:
			File.mkdir(self.path)
			File.mkdir(self.templates_path)
			File.mkdir(self.build_path)

			self.conf.create()

			print(f'Created pod: {self.pod_set.name} -> {self.name}')
			return self
		except SeedError as e:
			SeedError.error_exit(f'Error creating pod: {e}')
		except FileNotFoundError as e:
			SeedError.error_exit(f'PodSet "{self.pod_set.name}" does not exists.')

	def delete(self):
		self._guard()
		try:
			File.rm(self.path)
			print(f'Deleted pod: {self.pod_set.name} -> {self.name}')
		except SeedError as e:
			SeedError.error_exit(f'Error deleting pod: {e}')

	def create_template(self, name):
		self._guard()
		template_path = f'{self.templates_path}/{name}.yaml'
		try:
			with open(template_path, 'w') as f:
				pass  # Create an empty file
			return self
		except Exception as e:
			SeedError.error_exit(f'Error creating template: {e}')

	def get_teplates(self):
		self._guard()
		# TODO: implement
		return []

	def delete_template(self, name):
		self._guard()
		template_path = f'{self.templates_path}/{name}.yaml'
		if File.exists(template_path):
			os.remove(template_path)
			return self
		else:
			SeedError.error_exit(f'Template {name} does not exist')

	def build(self, namespace_names):
		self._guard()
		for namespace_name in namespace_names:
			namespace = Namespace(namespace_name)
			DeployManager(namespace, self).build()

		# TODO: Add logic to build the pod for the given namespace names
		return self  # Assuming successful for now

	def deploy(self, namespace_names):
		self._guard()
		# TODO: Add logic to deploy the pod to the given namespace names
		return self  # Assuming successful for now
