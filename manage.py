from settings        import *
from library.pod_set import PodSet

class Manager:
	@staticmethod
	def create_pod_set(name):
		PodSet(name).create()

	@staticmethod
	def delete_pod_set(name):
		PodSet(name).delete()

	@staticmethod
	def add_pod(pod_set_name, name):
		PodSet(pod_set_name).add_pod(name)

	@staticmethod
	def delete_pod(pod_set_name, name):
		PodSet(pod_set_name).delete_pod(name)

	@staticmethod
	def get_pod(pod_set_name, name):
		if PodSet(pod_set_name).get_pod(name):
			print(f'Pod {name} on PodSet {pod_set_name} is exists.')
		else:
			print(f'Pod {name} on PodSet {pod_set_name} does not exists.')


if __name__ == '__main__':
	pod_set = 'haha'
	pod     = 'hahaha'
	Manager.create_pod_set(pod_set)
	Manager.add_pod(pod_set, pod)
	Manager.get_pod(pod_set, pod)
	Manager.delete_pod(pod_set, pod)
	Manager.get_pod(pod_set, pod)
	Manager.delete_pod_set(pod_set)
