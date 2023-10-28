import sys

from library.file import File


class CommandManager:
	DIRS     = []  # Dirs that must be present in base directory, created if absent
	COMMANDS = {}  # Command structure expected from CLI

	def __init__(self):
		self.sub_commands = []
		self.args         = []
		self._ensure_dirs(self.DIRS)
		self._accept_args(self.COMMANDS, sys.argv[1:], [])
		self._execute()

	######################### PRIVATE #########################

	def _ensure_dirs(self, dirs):
		for d in dirs:
			if not File.exists(d):
				File.mkdir(d)

	def _accept_args(self, commands, remaining_args, command_path):
		if not isinstance(commands, dict):
			self.args = remaining_args[:len(commands)]
			if len(self.args) < len(commands):
				missing_arg = commands[len(self.args)]
				print(f'Missing argument: {missing_arg}', file=sys.stderr)
				sys.exit(1)
			return

		if not remaining_args:
			self._print_invalid_command(commands, command_path)
			sys.exit(1)

		command = remaining_args[0]
		if command not in commands:
			self._print_invalid_command(commands, command_path)
			sys.exit(1)

		self.sub_commands.append(command)
		self._accept_args(commands[command], remaining_args[1:], command_path + [command])

	def _execute(self):
		method_name = '__'.join(self.sub_commands)
		method = getattr(self, method_name, None)
		if method is not None:
			method(*self.args)
		else:
			print(f'Could not find method to execute for command: {method_name}', file=sys.stderr)
			sys.exit(1)

	def _print_invalid_command(self, commands, command_path):
		print('Invalid or incomplete command. Possible commands are:', file=sys.stderr)
		for cmd in self._build_command_list(commands, command_path):
			print(f'    – {cmd}', file=sys.stderr)

	def _build_command_list(self, commands, command_path):
		return [f'{" ".join(command_path + [cmd])}' for cmd in commands.keys()]

