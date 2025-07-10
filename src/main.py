
import argparse

from taskcli import add_command

if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
                prog='task-cli', 
                description='Simple CLI Todo list'
                )
    subparsers = parser.add_subparsers(required=True)

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument('item')
    parser_add.set_defaults(func=add_command)

    args = parser.parse_args()
    args.func(args)
