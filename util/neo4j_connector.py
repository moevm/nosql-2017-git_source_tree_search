import getpass
import logging
import os

from neo4j.exceptions import AuthError, ServiceUnavailable
from neo4j.v1 import GraphDatabase


class Neo4j:
    _instance = None
    _driver = None

    def __init__(self):
        self._log = logging.getLogger('gsts.neo4j')

        if not self._driver or self._driver.closed():
            self._init_database_driver()

        self._log.debug('Neo4j connector initialized')

    def _init_database_driver(self):
        try:
            username = os.environ["NEO4J_USERNAME"]
            password = os.environ["NEO4J_PASSWORD"]
        except KeyError:
            self._log.info('Environment variables NEO4J_USERNAME and NEO4J_PASSWORD doesn\'t set.')
            username, password = self._get_auth_data()

        retries = 2
        while True:
            try:
                self._driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=(username, password))
                break
            except AuthError as ae:
                retries -= 1
                self._log.error(str(ae) + ' ' + str(retries) + ' retries left')
                if retries > 0:
                    username, password = self._get_auth_data()
                else:
                    self._log.critical('Can\'t sign into Neo4j')
                    exit()
            except ServiceUnavailable as su:
                self._log.critical(su)
                exit()

    @staticmethod
    def _get_auth_data():
        username = input('Neo4j username:')
        password = getpass.getpass('Neo4j password:')
        return username, password

    @staticmethod
    def get_instance():
        if not Neo4j._instance:
            Neo4j._instance = Neo4j()

        instance = Neo4j._instance
        instance._log.debug('instance created')

        if not instance._driver or instance._driver.closed():
            instance._init_database_driver()

        return instance

    def __enter__(self):
        self._log.debug('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        self._log.debug('__exit__()')

    def create_repository_node(self, repo_path):
        statement = 'CREATE ( r :Repository :GSTS { path: {repo_path} } ) ' \
                    'RETURN r'

        with self._driver.session() as session:
            result = session.run(statement,
                                 repo_path=repo_path)
            self._log.debug('Created: ' + str(result.single()))

    def return_all(self):
        statement = 'MATCH ( n :GSTS ) ' \
                    'RETURN n'

        with self._driver.session() as session:
            result = session.run(statement)

            self._log.debug('All elements: ' + str(list(result.records())))

    def delete_all(self):
        statement = 'MATCH ( n :GSTS ) ' \
                    'DETACH DELETE n'

        with self._driver.session() as session:
            session.run(statement)
            self._log.debug('All data erased')

    def close(self):
        self._driver.close()