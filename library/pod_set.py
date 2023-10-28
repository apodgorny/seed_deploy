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

	def build(self, pod_names, namespace_names):
		self._guard()
		for pod_name in pod_names:
			pod = self.get_pod(pod_name)
			if pod:
				pod.build(namespace_names)
		return self

	def deploy(self, pod_names, namespace_names):
		self._guard()
		for pod_name in pod_names:
			pod = self.get_pod(pod_name)
			if pod:
				pod.deploy(namespace_names)
		return self
