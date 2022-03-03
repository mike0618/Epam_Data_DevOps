from task9_class import Docker

dock = Docker('tcp://127.0.0.1:2375')  # or 'unix://var/run/docker.sock'

dock.warnings()
dock.docker_ps_a()
dock.docker_images()
dock.inspect('headnode')
