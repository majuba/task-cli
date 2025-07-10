import os
import sys 
import argparse
import json

DATA_FILE = 'data.json'

class Task():
    def  __init__(self, task_id, desc, status):
        self.task_id = task_id  
        self.desc = desc
        self.status = status
    
    def to_dict(self):
        return {
            "task_id" : self.task_id,
            "desc" : self.desc,
            "status": self.status 
            }
    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["desc"], data["status"])

class TaskList():
    def __init__(self, last_id = 0, tasks = []):
        self.last_id = last_id
        self.tasks = tasks

    def to_dict(self):
        return {
            "last_id" : self.last_id,
            "tasks" : [t.to_dict() for t in self.tasks] 
        }
    
    @staticmethod
    def from_dict(data):
        tasks = [Task.from_dict(task) for task in data['tasks']]
        return TaskList(data["last_id"], tasks)

     
def load_tasklist():
    if not os.path.isfile(DATA_FILE):
        return TaskList()
    with open(DATA_FILE) as f:
        return TaskList.from_dict(json.load(f))
    
def write_tasklist(tasklist):
    with open(DATA_FILE, "w") as f:
        json.dump(tasklist.to_dict(), f)

def add_command(args):
    tasklist = load_tasklist()
    tasklist.last_id += 1
    new_task = Task(tasklist.last_id, args.item, status="in_progress")
    tasklist.tasks.append(new_task)
    write_tasklist(tasklist)
    #print(f"add!{ args.item}")
    return 1

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
