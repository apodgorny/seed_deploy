class DeployManager:
	def __init__(self, namespace, pod):
		self.namespace = namespace
		self.pod       = pod

	def build():
		templates = self.pod.get_templates()
		for template_name, template_content in templates:
			template_content = self.pod.conf_manager.apply(template_content)
			template_content = self.namespace.conf_manager.apply(template_content)
			self.pod.write_to_build(namespace.name, template_name, template_content)

