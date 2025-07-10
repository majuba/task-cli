
import argparse

from taskcli import add_command, list_command, delete_command, update_command

if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
                prog='task-cli', 
                description='Simple CLI Todo list'
                )
    subparsers = parser.add_subparsers(required=True)

    # add command 
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument('item')
    parser_add.set_defaults(func=add_command)

    # list command
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"])
    parser_list.set_defaults(func=list_command)

    # delete command 
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("task_id",type=int)
    parser_delete.set_defaults(func=delete_command)

    # update command 
    parser_update = subparsers.add_parser("update")
    parser_update.add_argument("task_id", type=int)
    parser_update.add_argument("desc")
    parser_update.set_defaults(func=update_command)

    args = parser.parse_args()
    args.func(args)
