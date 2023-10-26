# – Pod
# 	create(pod_name)
# 	delete()
# 	addTemplate(template_name)
# 	deleteTemplate(template_name)
# 	build(namespace_name) –> build_id
# 	deploy(namespace_name)


class Pod:
	def __init__(self, name):
		self.name = name

	def create(self):
		...

	def delete(self):
		...

	def add_template(self, name, content):
		...

	def delete_templae(self, name):
		...

	def build(self, namespace_names):
		...

	def deploy(self, namespace_names):
		...