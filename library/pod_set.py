import os

from settings import *

from library.file       import File
from library.pod        import Pod
from library.seed_error import SeedError

class PodSet:
	def __init__(self, name):
		self.name = name
		self.pods = {}
		self.path = File.path(PODSETS_DIR_NAME, self.name)
		self._read_pods()

	######################### PRIVATE ########################

	def _read_pods(self):
		if File.exists(self.path):
			for pod_name in File.list_dirs(self.path):
				self.pods[pod_name] = Pod(self, pod_name)

	def _guard(self):
		if not File.exists(self.path):
			SeedError.error_exit(f'PodSet "{self.name}" does not exist.')

	######################### PUBLIC #########################

	@staticmethod
	def get_all():
		return [PodSet(ps_dir) for ps_dir in File.list_dirs(PODSETS_DIR_NAME)]

	def create(self):
		if not File.exists(self.path):
			File.mkdir(self.path)
			print(f'Created PodSet "{self.name}"')
		else:
			SeedError.error_exit(f'PodSet "{self.name}" already exists.')
		return self

	def delete(self):
		self._guard()
		File.rm(os.path.join('pod_sets', self.name))
		print(f'Removed PodSet "{self.name}"')
		return self

	def list(self, indent=''):
		self._guard()
		for pod in self.pods:
			print(indent + '- ' + pod)

	def get(self, pod_name):
		self._guard()
		if pod_name in self.pods:
			return self.pods[pod_name]
		else:
			SeedError.error_exit(f'Pod "{self.name} -> {pod_name}" does not exists.')

	def build(self, namespace_name):
		self._guard()
		for pod_name in self.pods:
			self.get(pod_name).build(namespace_name)
		return self

	def deploy(self, namespace_name):
		self._guard()
		for pod_name in self.pods:
			self.get(pod_name).deploy(namespace_name)
		return self
