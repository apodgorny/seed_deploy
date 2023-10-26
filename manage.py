from settings            import *

from library.arg_manager import ArgManager
from library.pod_set     import PodSet


class Manager(ArgManager):
	COMMANDS = {
		'pod': {
			'create': ['pod_set_name', 'name'],
			'delete': ['pod_set_name', 'name']
		},
		'pod_set': {
			'create': ['name'],
			'delete': ['name']
		}
	}

	######################### PUBLIC #########################

	@staticmethod
	def pod_set__create(name):
		PodSet(name).create()

	@staticmethod
	def pod_set__delete(name):
		PodSet(name).delete()

	@staticmethod
	def pod__create(pod_set_name, name):
		PodSet(pod_set_name).create_pod(name)

	@staticmethod
	def pod__delete(pod_set_name, name):
		PodSet(pod_set_name).delete_pod(name)


if __name__ == '__main__':
	manager = Manager()
