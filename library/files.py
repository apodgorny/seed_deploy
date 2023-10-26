import os
import shutil
import settings

from library.seed_error import SeedError


class Files:
	@staticmethod
	def exists(path):
		return os.path.exists(path)

	@staticmethod
	def rm(path):
		dir_path = os.path.join(settings.BASE_DIR, path)
		if not os.path.exists(dir_path):
			raise SeedError(f'Entity does not exist')
		return shutil.rmtree(dir_path)

	@staticmethod
	def mkdir(path):
		dir_path = os.path.join(settings.BASE_DIR, path)
		if os.path.exists(dir_path):
			raise SeedError(f'Entity already exists')
		return os.mkdir(dir_path)