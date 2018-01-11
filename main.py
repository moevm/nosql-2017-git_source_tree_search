#!/usr/bin/env python3
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(prog='Git Source Tree Search',
                                     allow_abbrev=False)

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show debug messages')

    subparsers = parser.add_subparsers(help='Sub-command help')

    init = subparsers.add_parser('init',
                                 help='create a new project node in the Neo4j database')
    init.set_defaults(command='init')
    init.add_argument('project_path',
                      action='store_const',
                      help='path to project',
                      metavar='PROJECT_PATH',
                      const=os.getcwd())

    status = subparsers.add_parser('status',
                                   help='show current project status')
    status.set_defaults(command='status')

    predict = subparsers.add_parser('predict',
                                    help='predict commit-affected unittests')
    predict.set_defaults(command='predict')

    args = vars(parser.parse_args())

    if 'command' not in args:
        parser.print_help()

    return args


if __name__ == '__main__':
    args = parse_arguments()
    print(args)
