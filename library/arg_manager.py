import sys

class ArgManager:
	COMMANDS = {}

	def __init__(self):
		self.args    = {}
		self.command = []
		self._accept_args(self.COMMANDS, sys.argv[1:], [])
		self._execute()

	######################### PRIVATE #########################
		
	def _accept_args(self, commands, remaining_args, command_path):
		if not isinstance(commands, dict):
			for i, expected_arg in enumerate(commands):
				try:
					self.args[expected_arg] = remaining_args[i]
				except IndexError:
					print(f'Missing argument: {expected_arg}', file=sys.stderr)
					sys.exit(1)
			return

		if not remaining_args:
			self._print_invalid_command(commands, command_path)
			sys.exit(1)

		command = remaining_args[0]
		if command not in commands:
			self._print_invalid_command(commands, command_path)
			sys.exit(1)

		self.command.append(command)
		self._accept_args(commands[command], remaining_args[1:], command_path + [command])

	def _execute(self):
		method_name = '__'.join(self.command)
		method = getattr(self, method_name, None)
		if method is not None:
			args = [self.args.get(arg) for arg in self.COMMANDS[self.command[0]][self.command[1]]]
			method(*args)
		else:
			print(f'Could not find method to execute for command: {method_name}', file=sys.stderr)
			sys.exit(1)

	def _print_invalid_command(self, commands, command_path):
		print('Invalid or incomplete command. Possible commands are:', file=sys.stderr)
		for cmd in self._build_command_list(commands, command_path):
			print(f'    – {cmd}', file=sys.stderr)

	def _build_command_list(self, commands, command_path):
		return [f'{" ".join(command_path + [cmd])}' for cmd in commands.keys()]
