from util.neo4j_connector import Neo4j


def init_project(args):
    with Neo4j.get_instance() as neo4j:
        neo4j.create_repository_node('somepath')
        neo4j.create_repository_node('fun')
        neo4j.create_commit_node('fun', 'blablabla')
        neo4j.return_all()
        neo4j.delete_all()
