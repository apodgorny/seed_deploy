import os
import sys

from settings import *

from library.file         import File
from library.conf_manager import ConfManager
from library.seed_error   import SeedError
from library.kube_manager import KubeManager


class Namespace:
	def __init__(self, name):
		self.name = name
		self.path = File.path(NAMESPACES_DIR_NAME, self.name)
		self.conf = ConfManager(self.path)

	######################### PRIVATE ########################

	def _guard(self):
		if not File.exists(self.path):
			SeedError.error_exit(f'Namespace "{self.name}" does not exist.')

	######################### PUBLIC #########################

	@staticmethod
	def get_all():
		return [Namespace(ns_dir) for ns_dir in File.list_dirs(NAMESPACES_DIR_NAME)]

	def create(self, namespace_like_name=None):
		try:
			File.mkdir(self.path)
			constants = {}
			if (namespace_like_name):
				constants.update(Namespace(namespace_like_name).conf.get_constants())
				
			constants['namespace'] = self.name
			self.conf.create(constants)
			KubeManager.create_namespace(self.name)
			print(f'Created Namespace: "{self.name}"')
			return self
		except Exception as e:
			SeedError.error_exit(f'Error creating namespace: {e}', file=sys.stderr)

	def delete(self):
		self._guard()
		try:
			File.rm(self.path)
			KubeManager.delete_namespace(self.name)
		except SeedError as e:
			SeedError.error_exit(str(e))
		print(f'Deleted Namespace: "{self.name}".')
