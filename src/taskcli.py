
import json
import os 

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
    
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        for i in range(len(self.tasks)-1):
            if self.tasks[i].task_id == task_id:
                del self.tasks[i] 
        
    def to_dict(self):
        return {
            "last_id" : self.last_id,
            "tasks" : [t.to_dict() for t in self.tasks] 
        }
    def update_task(self, task_id, desc):
        for task in self.tasks:
            if task.task_id == task_id:
                task.desc = desc 
                return 
        raise ValueError()

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
    new_task = Task(tasklist.last_id, args.item, status="todo")
    tasklist.add_task(new_task)
    write_tasklist(tasklist)
    print(f"task added successfully (Id: {tasklist.last_id})")

def list_command(args):
    tasklist = load_tasklist()
    for task in tasklist.tasks:
        if args.status and task.status != args.status:
            continue
        print(task.desc, f" Id: {task.task_id}")

def delete_command(args):
    tasklist = load_tasklist()
    tasklist.remove_task(args.task_id)
    write_tasklist(tasklist)
    print(f"Successfully removed task with id {args.task_id}")

def update_command(args):
    tasklist = load_tasklist()
    try:
        tasklist.update_task(args.task_id, args.desc)
    except ValueError:
        print(f"No task with id {args.task_id} found!")
        return
    write_tasklist(tasklist)
    print(f"Successfully updated task with id {args.task_id}")