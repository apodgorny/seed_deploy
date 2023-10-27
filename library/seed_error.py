import sys

from library.colors import Colors


class SeedError(Exception):
	def __init__(self, message='A custom error occurred'):
		super().__init__(message)

	@staticmethod
	def error_exit(message='Critical error.', code=2):
		print(f'{Colors.RED}{message}{Colors.RESET}', file=sys.stderr)
		sys.exit(code)
