#!/usr/bin/env python3
import argparse
import logging
import os
import sys

import command.init as init


def parse_arguments():
    parser = argparse.ArgumentParser(prog='gsts.py')

    parser.add_argument('-v', '--verbose',
                        action='count',
                        help='show debug messages [ WARNING, INFO, DEBUG ]')

    subparsers = parser.add_subparsers(help='Sub-command help')

    init = subparsers.add_parser('init',
                                 help='create a new project node in the Neo4j database')
    init.set_defaults(command='init')

    init.add_argument('--project-path',
                      action='store',
                      nargs=1,
                      help='path to project',
                      metavar='PATH',
                      default=[os.getcwd()])

    init.add_argument('--virtualenv',
                      action='store',
                      nargs=1,
                      help='virtual environment directory name',
                      metavar='PATH',
                      default='venv')

    status = subparsers.add_parser('status',
                                   help='show current project status')
    status.set_defaults(command='status')

    predict = subparsers.add_parser('predict',
                                    help='predict commit-affected unittests')
    predict.set_defaults(command='predict')

    args = vars(parser.parse_args())

    if 'command' not in args:
        parser.print_help()
        exit()

    return args


if __name__ == '__main__':
    args = parse_arguments()
    print(args)

    loggers = [
        'gsts.init',
        'gsts.predict',
        'gsts.status',
        'gsts.crawler',
        'gsts.neo4j',
        'gsts.project'
    ]

    if args['verbose']:
        logging.basicConfig(stream=sys.stdout)

        level = args['verbose']

        if level > 3:
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        else:
            level -= 1

            levels = [
                logging.WARNING,
                logging.INFO,
                logging.DEBUG
            ]

            for log_name in loggers:
                logger = logging.getLogger(log_name)
                logger.setLevel(levels[level])
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

    if args['command'] == 'init':
        init.init_project(args)
