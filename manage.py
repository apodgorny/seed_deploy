from settings            import *

from library.arg_manager import ArgManager
from library.files       import Files
from library.namespace   import Namespace
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
		},
		'namespace': {
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

	@staticmethod
	def namespace__create(name):
		Namespace(name).create()

	@staticmethod
	def namespace__delete(name):
		Namespace(name).delete()


def main():
	if not Files.exists('pod_sets'):
		Files.mkdir('pod_sets')
	if not Files.exists('namespaces'):
		Files.mkdir('namespaces')
	manager = Manager()


if __name__ == '__main__':
	main()
