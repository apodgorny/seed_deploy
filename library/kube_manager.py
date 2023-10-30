import os
import subprocess

from library.seed_error import SeedError


class KubeManager:
	@staticmethod
	def _exec(command, path=None):
		if path:
			os.chdir(path)
		res = subprocess.run(command, shell=True, capture_output=True, text=True)
		return res.stdout, res.stderr

	@staticmethod
	def apply(file):
		stdout, stderr = KubeManager._exec(f'kubectl apply -f {file}')
		if stderr:
			SeedError.error_exit(f'Error applying file "{file}": {stderr}')
		print(stdout)

	@staticmethod
	def create_namespace(namespace_name=None):
		stdout, stderr = KubeManager._exec(f'kubectl create namespace {namespace_name}')
		if stderr:
			SeedError.error_exit(f'Error creating namespace "{namespace_name}": {stderr}')
		print(stdout)

	@staticmethod
	def delete_namespace(namespace_name):
		stdout, stderr = KubeManager._exec(f'kubectl delete namespace {namespace_name}')
		if stderr:
			raise SeedError(f'Error deleting namespace "{namespace_name}": {stderr}')
		print(stdout)
