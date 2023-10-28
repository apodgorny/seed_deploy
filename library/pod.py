import os
import re
import sys

from settings import *

from library.file         import File
from library.seed_error   import SeedError
from library.conf_manager import ConfManager
from library.namespace    import Namespace


class Pod:
	def __init__(self, pod_set, name):
		self.name           = name
		self.pod_set        = pod_set
		self.path           = File.path(PODSETS_DIR_NAME, pod_set.name, self.name)
		self.build_path     = File.path(self.path, 'build')
		self.templates_path = File.path(self.path, 'templates')
		self.conf           = ConfManager(self.path)

	######################### PRIVATE ########################

	def _guard(self):
		if not File.exists(self.path):
			SeedError.error_exit(f'PodSet "{self.name}" does not exist.')

	def _get_templates(self):
		return {
			file_name : File.read(File.path(self.templates_path, file_name))
			for file_name in File.list_files(self.templates_path, ['yaml'])
		}

	def _build_template(self, namespace, s):
		s = re.sub(r'\$namespace\.(\w+)', lambda match: namespace.conf.get(match.group(1)), s)
		s = re.sub(r'\$pod\.(\w+)',       lambda match: self.conf.get(match.group(1)), s)
		return s

	######################### PUBLIC #########################

	def create(self):
		try:
			File.mkdir(self.path)
			File.mkdir(self.templates_path)
			File.mkdir(self.build_path)

			File.mkfile(
				File.path(self.templates_path, 'test.yaml'),
				File.read('templates/test.yaml')
			)
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

	def delete_template(self, name):
		self._guard()
		template_path = f'{self.templates_path}/{name}.yaml'
		if File.exists(template_path):
			os.remove(template_path)
			return self
		else:
			SeedError.error_exit(f'Template {name} does not exist')

	def get_build(self):
		build = {}
		for d in File.list_dirs(self.build_path):
			build[d] = []
			for f in File.list_files(File.path(self.build_path, d), 'yaml'):
				build[d].append(f)
		return build

	def build(self, namespace_name):
		self._guard()

		templates     = self._get_templates()
		namespace     = Namespace(namespace_name)
		ns_build_path = File.path(self.build_path, namespace.name)

		File.mkdir(ns_build_path, True)

		for tpl_name in templates:
			build_content   = self._build_template(namespace, templates[tpl_name])
			build_file_path = File.path(ns_build_path, tpl_name)

			File.write(build_file_path, build_content)

		return self

	def deploy(self, namespace_names):
		self._guard()
		# TODO: Add logic to deploy the pod to the given namespace names
		return self  # Assuming successful for now










