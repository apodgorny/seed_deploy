import os
import sys

from settings import *

from library.file         import File
from library.conf_manager import ConfManager
from library.seed_error   import SeedError


class Namespace():
	def __init__(self, name):
		self.name = name
		self.path = File.path(NAMESPACES_DIR_NAME, self.name)
		self.conf = ConfManager(self.path)

	######################### PRIVATE ########################

	def _guard(self):
		if not File.exists(self.path):
			SeedError.error_exit(f'Namespace "{self.name}" does not exist.')

	######################### PUBLIC #########################

	def create(self):
		try:
			File.mkdir(self.path)
			self.conf.create()
			print(f'Created Namespace: "{self.name}"')
			return self
		except Exception as e:
			SeedError.error_exit(f'Error creating namespace: {e}', file=sys.stderr)

	def delete(self):
		self._guard()
		try:
			File.rm(self.path)
		except SeedError as e:
			SeedError.error_exit(str(e))
		print(f'Deleted Namespace: "{self.name}".')
