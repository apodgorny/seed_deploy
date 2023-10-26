# – Pod Set
# 	create(pod_set_name)
# 	addPod(pod_name)
# 	deletePod(pod_name)
# 	getPod(pod_name)
# 	build(pod_names[], namespace_name[])
# 	deploy(pod_names[], namespace_names[])

import os
import settings

from library.files      import Files
from library.seed_error import SeedError


class PodSet:
	def __init__(self, name):
		self.name = name

	def create(self):
		Files.mkdir(os.path.join('pod_sets', self.name))
		print(f'Created PodSet "{self.name}"')

	def delete(self):
		Files.rm(os.path.join('pod_sets', self.name))
		print(f'Removed PodSet "{self.name}"')

	def add_pod(self, name):
		Files.mkdir(os.path.join('pod_sets', self.name, name))
		print(f'Created Pod {name} on PodSet {self.name}')


	def delete_pod(self, name):
		Files.rm(os.path.join('pod_sets', self.name, name))
		print(f'Removed Pod {name} on PodSet {self.name}')

	def get_pod(self, name):
		return Files.exists(os.path.join('pod_sets', self.name, name))

	def build(self, pods_names, namespaces_names):
		for pod_name in pods_names:
			for namespace_name in  namespaces_names:
				...

	def deploy(self, pods_names, namespaces_names):
		for pod_name in pods_names:
			for namespace_name in namespaces_names:
				...