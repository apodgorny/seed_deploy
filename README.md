# seed_deploy
Deployment services for Kubernetes. Works for "seed" repo in particular, but can be adopted for any.

– PodSets
	– PodSet1
		– Pod1
			– Build # Generated files
				– Namespace1
					– deployment.yaml
				– Namespace2
					– deployment.yaml
			– Templates
				– template.deployment.yaml
				...
			– Source
				– constants.json  // Configuration for a vagon – env data / contains docker-image link
				– variables.py    // Dynamic configuratio for a vagon
– Namespaces
	– Namespace1
		– constants.json
		– variables.py 
	– Namespace2
		– constants.json
		– variables.py


Functions:

	– Pod Set
		create(pod_set_name)
		addPod(pod_name)
		deletePod(pod_name)
		getPod(pod_name)
		build(pod_names[], namespace_name[])
		deploy(pod_names[], namespace_names[])

	– Pod
		create(pod_name)
		delete()
		addTemplate(template_name)
		deleteTemplate(template_name)
		build(namespace_name) –> build_id
		deploy(namespace_name)





