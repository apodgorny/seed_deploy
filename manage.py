from settings import *

from library.command_manager import CommandManager
from library.file            import File
from library.namespace       import Namespace
from library.pod_set         import PodSet
from library.pod             import Pod


class Manager(CommandManager):
	DIRS = [PODSETS_DIR_NAME, NAMESPACES_DIR_NAME]
	COMMANDS = {
		'pod': {
			'create' : ['pod_set_name', 'name'],
			'delete' : ['pod_set_name', 'name'],
			'list'   : ['pod_set_name']
		},
		'podset': { 
			'create' : ['name'],
			'delete' : ['name'],
			'list'   : []
		},
		'namespace':  {
			'create' : ['name'],
			'delete' : ['name']
		},
		'list': []
	}

	######################### PUBLIC #########################

	@staticmethod
	def podset__create(name):
		PodSet(name).create()

	@staticmethod
	def podset__delete(name):
		PodSet(name).delete()

	@staticmethod
	def list():
		indent = ' '
		print(indent, 'Podsets:')
		for d in File.list_dirs(PODSETS_DIR_NAME):
			print(indent + '  ', '-', d)
			PodSet(d).list(indent + '    ') 
		print(indent, 'Namespaces:')
		for d in File.list_dirs(NAMESPACES_DIR_NAME):
			print(indent + '  ', '-', d)

	@staticmethod
	def pod__create(pod_set_name, name):
		pod_set = PodSet(pod_set_name)
		Pod(pod_set, name).create()

	@staticmethod
	def pod__delete(pod_set_name, name):
		PodSet(pod_set_name).pods[name].delete()

	@staticmethod
	def namespace__create(name):
		Namespace(name).create()

	@staticmethod
	def namespace__delete(name):
		Namespace(name).delete()


if __name__ == '__main__':
	Manager()
