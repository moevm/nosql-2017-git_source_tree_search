from os import environ

from neo4j.v1 import GraphDatabase


class HelloWorldExample(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri=uri,
                                            auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)",
                        message=message)
        return result.single()[0]


def test_neo4j_connection():
    try:
        uri = "bolt://localhost:7687"
        user = environ["NEO4J_USERNAME"]
        password = environ["NEO4J_PASSWORD"]
        print(uri, user, password)
        example = HelloWorldExample(uri, user, password)
        example.print_greeting("Hello, world!")
        example.close()
    except KeyError:
        print("can't find environment variables NEO4J_USERNAME and NEO4J_PASSWORD")


def main():
    test_neo4j_connection()


if __name__ == '__main__':
    main()
