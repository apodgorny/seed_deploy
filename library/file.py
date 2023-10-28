import os
import shutil
import settings

from library.seed_error import SeedError


class File:
	@staticmethod
	def path(*args):
		path = os.path.join(*args)
		path = path.replace(settings.BASE_DIR, '', 1).lstrip('/')
		path = os.path.join(settings.BASE_DIR, path)
		return path

	@staticmethod
	def exists(path):
		path = File.path(path)
		return path if os.path.exists(path) else False

	@staticmethod
	def rm(path):
		path = File.exists(path)
		if not os.path.exists(path):
			raise SeedError(f'Entity does not exist')
		return shutil.rmtree(path)

	@staticmethod
	def mkdir(path):
		if File.exists(path):
			raise SeedError(f'Directory "{path}" already exists')
		return os.mkdir(File.path(path))

	@staticmethod
	def mkfile(path, content=''):
		if File.exists(path):
			raise SeedError(f'File "{path}" already exists')
		with open(File.path(path), 'w') as f:
			f.write(content)

	@staticmethod
	def write(path, content=''):
		if not File.exists(path):
			raise SeedError(f'File "{path}" does not exists')
		with open(File.path(path), 'w') as f:
			f.write(content)

	@staticmethod
	def read(path):
		if not File.exists(path):
			raise SeedError(f'File "{path}" does not exists')
		with open(File.path(path), 'r') as f:
			return f.read()

	@staticmethod
	def list_dirs(path=''):
		path = File.exists(path)
		dirs = []
		for item in sorted(os.listdir(path)):
			item_path = os.path.join(path, item)
			if os.path.isdir(item_path) and not item.startswith(('_', '.')):
				dirs.append(item)
		return dirs