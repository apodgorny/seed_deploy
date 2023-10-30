from settings import *

from library.command_manager import CommandManager
from library.file            import File
from library.namespace       import Namespace
from library.pod_set         import PodSet
from library.pod             import Pod


class Manager(CommandManager):
	DIRS = [PODSETS_DIR_NAME, NAMESPACES_DIR_NAME]
	COMMANDS = {
		'create': {
			'podset'    : ['podset_name'],
			'pod'       : ['podset_name', 'pod_name'],
			'namespace' : ['namespace_name']  
		},
		'delete': {
			'podset'    : ['podset_name'],
			'pod'       : ['podset_name', 'pod_name'],
			'namespace' : ['namespace_name']  
		},
		'build': {
			'podset'    : ['podset_name', 'namespace_name'],
			'pod'       : ['podset_name', 'pod_name', 'namespace_name'],
			'all'       : []
		},
		'deploy': {
			'podset'    : ['podset_name', 'namespace_name'],
			'pod'       : ['podset_name', 'pod_name', 'namespace_name'],
			'all'       : []
		},
		'list': [],
	}
		
	######################### PUBLIC #########################

	@staticmethod
	def create__podset(podset_name):
		PodSet(podset_name).create()

	@staticmethod
	def create__pod(podset_name, pod_name):
		podset = PodSet(podset_name)
		Pod(podset, pod_name).create()

	@staticmethod
	def create__namespace(namespace_name): # TODO: add optional param file (namespace.yaml)
		Namespace(namespace_name).create()

	@staticmethod
	def delete__podset(podset_name):
		PodSet(podset_name).delete()

	@staticmethod
	def delete__pod(podset_name, pod_name):
		PodSet(podset_name).get(pod_name).delete()

	@staticmethod
	def delete__namespace(namespace_name):
		Namespace(namespace_name).delete()

	@staticmethod
	def list():
		i = ' '
		print(i, 'Podsets:')
		for d in File.list_dirs(PODSETS_DIR_NAME):
			podset = PodSet(d)
			print(i, '-', podset.name)
			for _, pod in podset.pods.items():
				print(i, i, '-', pod.name)
				for ns, files in pod.get_build().items():
					print(i, i, i, '::', ns, files)
		print(i, 'Namespaces:')
		for d in File.list_dirs(NAMESPACES_DIR_NAME):
			namespace = Namespace(d)
			print(i, i, '-', namespace.name)

	@staticmethod
	def build__podset(podset_name, namespace_name):
		PodSet(podset_name).build(namespace_name)

	@staticmethod
	def build__pod(podset_name, pod_name, namespace_name):
		PodSet(podset_name).get(pod_name).build(namespace_name)

	@staticmethod
	def build__all():
		for podset in PodSet.get_all():
			for namespace in Namespace.get_all():
				podset.build(namespace.name)

	@staticmethod
	def deploy__podset(podset_name, namespace_name):
		PodSet(podset_name).deploy(namespace_name)

	@staticmethod
	def deploy__pod(podset_name, pod_name, namespace_name):
		PodSet(podset_name).get(pod_name).deploy(namespace_name)

	@staticmethod
	def deploy__all():
		for podset in PodSet.get_all():
			for namespace in Namespace.get_all():
				podset.deploy(namespace.name)


if __name__ == '__main__':
	Manager()
