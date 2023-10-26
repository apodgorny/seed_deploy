from settings        import *
from library.pod_set import PodSet

class Manager:
	@staticmethod
	def create_pod_set(name):
		PodSet(name).create()

	@staticmethod
	def delete_pod_set(name):
		PodSet(name).delete()


if __name__ == '__main__':
	Manager.create_pod_set('haha')
	Manager.delete_pod_set('haha')
