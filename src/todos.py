import sys
import typer
from datetime import datetime

sys.path.append('./')

from src.lists.list import *



app = typer.Typer(add_completion=False)

### CLI METHODS ###

@app.command("create")
def create(name: str = typer.Option("Unnamed", "-ln", "--listname")):

    """Create a new to-do list
    
    Parameters
    ----------
    name : string
        Name of the list to be created
        
    """

    if check_list_exists(name):
        print("There is already a todo list with this name.")
        return

    create_list(name)
    print(f"Todo list {name} successfully created!")


@app.command("list")
def list_lists():

    """Lists all existing todo lists
    
    Print all the list

    This command have no parameters
    
    """

    existing_lists = get_existing_lists()
    for ls in existing_lists:
        print(ls)


@app.command("show")
def show_list(list_name: str = typer.Option(..., "-ln", "--listname")):

    """Shows Task in one list
    
    First of all, validate if the list exists
    If the list exists, load and show the the content of the list

    Parameters
    ----------
    listname : string
        The name of the list to be showed
    
    """
    
    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    df = load_list(list_name)
    print(df.to_markdown())


@app.command("add")
def add_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_name: str = typer.Option(..., "-tn", "--taskame"),
    summary: str = typer.Option(None, "-d", "--description"),
    owner: str = typer.Option(..., "-o", "--owner"),
):
    """Add a task to a given todo list
    
    Validate if the listname exists
    If the list exists, a new row is created with the fields:
        created: the datetime the row is created
        task: the name of the task (taskname)
        summary: the description given, if not, assign None
        status: "todo"
        owner: the owner of the task 

    Parameters
    ----------
    listname : string
        The name of the list 
    taskname : string
        The name of the task 
    summary: string
        Description of the task 
    owner: string
        Name of the person owner the task

    """

    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
    else:
        new_row = {"created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"), 
        "task": task_name, 
        "summary": summary or None, 
        "status": "todo", 
        "owner": owner}
        add_to_list(list_name, new_row)
        print("Task successfully added")


@app.command("update")
def update_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_id: int = typer.Option(..., "-i", "--taskid"),
    field: str = typer.Option(..., "-f", "--field"),
    change: str = typer.Option(..., "-c", "--change"),
):

    """Update a task in a given todo list
    
    Validate if the listname exists
    If the list exists, it updates the task with the update_task_in_list()
    function using the parameters: list_name, task_id, field and 
    parameters.

    Parameters
    ----------
    listname : string
        The name of the list
    task_id : int
        row of the task to be updated.
    field: string
        Name of the column to be updated
    change: string
        This value replaces the previous one   
    
    """

    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    update_task_in_list(list_name, task_id, field, change)
    print("Task successfully updated")


if __name__ == "__main__":
    app()
