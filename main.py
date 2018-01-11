import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show debug messages')

    parser.parse_args()


if __name__ == '__main__':
    parse_arguments()
