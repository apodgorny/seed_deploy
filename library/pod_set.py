# – Pod Set
# 	create(pod_set_name)
# 	addPod(pod_name)
# 	deletePod(pod_name)
# 	getPod(pod_name)
# 	build(pod_names[], namespace_name[])
# 	deploy(pod_names[], namespace_names[])

import os

from library.files import Files
from library.pod   import Pod

class PodSet:
	def __init__(self, name):
		self.name = name
		self.pods = {}
		self._read_pods()

	######################### PRIVATE ########################

	def _read_pods(self):
		pod_set_path = os.path.join('pod_sets', self.name)
		if Files.exists(pod_set_path):
			for pod_name in os.listdir(pod_set_path):
				pod_path = os.path.join(pod_set_path, pod_name)
				if os.path.isdir(pod_path):
					self.pods[pod_name] = Pod(pod_name)

	######################### PUBLIC #########################

	def create(self):
		Files.mkdir(os.path.join('pod_sets', self.name))
		print(f'Created PodSet "{self.name}"')
		return self

	def delete(self):
		Files.rm(os.path.join('pod_sets', self.name))
		print(f'Removed PodSet "{self.name}"')
		return self

	def create_pod(self, name):
		new_pod = Pod(name).create()
		if new_pod:  # if not a NoOp object
			self.pods[name] = new_pod
			print(f'Created Pod {name} on PodSet {self.name}')
		return self

	def delete_pod(self, name):
		if name in self.pods:
			self.pods[name].delete()
			del self.pods[name]
			print(f'Removed Pod {name} on PodSet {self.name}')
		return self

	def get_pod(self, name):
		return self.pods.get(name, None)

	def build(self, pod_names, namespace_names):
		for pod_name in pod_names:
			pod = self.get_pod(pod_name)
			if pod:
				pod.build(namespace_names)
		return self

	def deploy(self, pod_names, namespace_names):
		for pod_name in pod_names:
			pod = self.get_pod(pod_name)
			if pod:
				pod.deploy(namespace_names)
		return self
