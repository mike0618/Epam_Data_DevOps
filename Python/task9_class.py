import docker
from docker import errors
from tabulate import tabulate
from humanize import naturalsize, precisedelta
from datetime import datetime
from pprint import pprint


class Docker:
    def __init__(self, host=None):
        try:
            self.client = docker.DockerClient(base_url=host)
        except errors.DockerException as err:
            print(err)
            self.client = docker.from_env()
            print('Connection from_env')

    def warnings(self):  # part 1
        print('\n1. Warnings:')
        for container in self.client.containers.list(all=True):
            state = container.attrs.get('State')
            c_name = container.attrs.get('Name')
            if state.get('Dead'):
                print(f'Container "{c_name}" with ID: "{container.id}" is dead.')
            if not state.get('Running'):
                print(f'Container "{c_name}" with ID: "{container.id}" is not running.')

    def docker_ps_a(self, a=True):  # part 2
        """
        'docker ps -a' analogue.

        :param a: True(default) to show all containers
        """
        tab_head = ['CONTAINER ID', 'IMAGE', 'COMMAND', 'CREATED', 'STATUS', 'PORTS', 'NAMES']
        table = []
        now = datetime.now()
        for container in self.client.containers.list(all=a):
            state = container.attrs.get('State')
            config = container.attrs.get('Config')
            running = state.get('Running')
            c_name = container.attrs.get('Name')
            status_col = f'{state.get("Status")} ({state.get("ExitCode")})'
            created = datetime.strptime(container.attrs.get('Created')[:19], '%Y-%m-%dT%H:%M:%S')
            p_created = precisedelta(now - created, minimum_unit='days', format='%.0f') + ' ago'
            if running:
                status_col = f'Up from {state.get("StartedAt")[:19]}'
            table.append([config.get('Hostname'),
                          config.get('Image'),
                          f'{config.get("Cmd")} {config.get("Entrypoint")}',
                          p_created,
                          status_col,
                          list(config.get('ExposedPorts').keys()),
                          c_name])

        print('\n2. "docker ps -a"')
        print(tabulate(table, headers=tab_head, tablefmt='github'))

    def docker_images(self):  # part 3
        """
        'docker image ls' analogue.
        """
        tab_head = ['REPOSITORY', 'TAG', 'IMAGE ID', 'CREATED', 'SIZE']
        now = datetime.now()
        table = []
        for image in self.client.images.list():
            attrs = image.attrs
            image_id = attrs.get('Id').split(':')[1][:12]
            created = datetime.strptime(attrs.get('Created')[:19], '%Y-%m-%dT%H:%M:%S')
            p_created = precisedelta(now - created, minimum_unit='days', format='%.0f') + ' ago'
            size = naturalsize(attrs.get("Size"), format='%.3g')
            add_lst = [image_id, p_created, size]
            repotags = attrs.get('RepoTags')
            for rt in repotags:
                table.append(rt.split(':') + add_lst)

        print('\n3. "docker image ls"')
        print(tabulate(table, headers=tab_head, tablefmt='github'))

    def inspect(self, cont):
        print(f'\n4. "docker inspect {cont}"')
        try:
            pprint(self.client.containers.get(cont).attrs)
        except errors.NotFound as err:
            print(err)
