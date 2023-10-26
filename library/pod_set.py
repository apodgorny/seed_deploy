# – Pod Set
# 	create(pod_set_name)
# 	addPod(pod_name)
# 	deletePod(pod_name)
# 	getPod(pod_name)
# 	build(pod_names[], namespace_name[])
# 	deploy(pod_names[], namespace_names[])

import os
import settings

from files              import Files
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
		...

	def delet_pod(self, name):
		...

	def get_pod(self, name):
		...

	def build(self, pod_names, namespace_name):
		...

	def deploy(self, pod_names, namespace_name):
		...