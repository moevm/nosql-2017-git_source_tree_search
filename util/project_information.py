import logging
import os

import pygit2

from util.neo4j_connector import Neo4j


class ProjectInformation:
    def __init__(self, args):
        self._log = logging.getLogger('gsts.project')

        if args['command'] == 'init':
            project_dir = os.path.abspath(args['project_path'][0])
        else:
            project_dir = os.getcwd()

        repository_path = None
        try:
            repository_path = pygit2.discover_repository(project_dir)
        except KeyError:
            self._log.critical('Not in Git repository')
            exit()

        self._log.debug('Found repository dir at: ' + str(repository_path))
        self._repository_path = repository_path

        self._project_root = os.path.dirname(repository_path.replace('/', os.sep).rstrip(os.sep))
        self._log.debug('Found project root at: ' + self._project_root)

    def init_project(self):
        connection = Neo4j()

        if not connection.has_repository_node(self._repository_path):
            connection.create_repository_node(self._repository_path)
            print('Project initialized')
        else:
            print('Project already exists')
