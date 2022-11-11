import os
import pandas as pd
from pathlib import Path

# Set the Data path 
PATH = str(Path(__file__).parent.parent)
PATH_TO_DATA = f"{PATH}/data/"


### LIST METHODS TO BE REFACTORED ###

## This method do an update on a specific field of a Task
def update_task_in_list(list_name: str, task_id: int, field: str, change: str) -> None:

    """ Edits a task of list name
    Load a csv file named as the list_name parameter from the data directory 
    Update the task_id and field specified and replaces it with the change string
    Saves the DataFrame with the store_list() function

    Parameters
    ----------
    name : string
        The name of the list
    
    task_id : int
        id of the task to be edited.
    
    field: str
        Name of the field to be edited.
    
    change: str
        New value to be changed

    Returns
    -------
    None
    """

    df = load_list(list_name)
    df.loc[task_id, field] = change
    store_list(df, list_name)

## This method Create a new list
def create_list(list_name: str) -> None:

    """ Creates a list and saves it in data directory
    Creates a new DataFrame with the columns 'created', 'task', 
    'summary', 'status', 'owner' and saves
    it as a list in thedata  directory with function store_list().

    Parameters
    ----------
    name : string
        The name of the list to be saved 

    Returns
    -------
    None
    """

    df = pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])
    store_list(df, list_name)

## This method get all the lists present in the Data Directory Default
def get_existing_lists() -> list:
    
    """
    Load all lists in data directory.

    Get a list with all the lists in the data directory. 
    Don't use arguments.

    Returns
    -------
    list
        List all lists in the data directory
    
    """
    return os.listdir(PATH_TO_DATA)

## This method check if a list exists in the Data Directory Default
def check_list_exists(list_name: str) -> bool:

    """ Checks if the list exists.
    Get the filename of the list using the get_list_filename() function with 
    name of the list as its parameter. Then, check if the list filename is located
    in the existing list of lists, using the get_existing_lists() function.
    Parameters
    ----------
    name : string
        The name of the list
    Returns
    -------
    bool
        True if the list already exists, False if not.
    """

    return get_list_filename(list_name) in get_existing_lists()

## This method get the name of a specific list
def get_list_filename(list_name: str) -> str:

    """ Get the filename of a specified list.
    Gets the filename of a list name

    Parameters
    ----------
    name : string
        The name of the list 

    Returns
    -------
    string
        The name of the list + .csv as the filename.
    """

    return f"{list_name}.csv"

## This method load and return the data of a list
def load_list(list_name: str) -> pd.DataFrame:

    """ Load csv from directory as a DataFrame.
    Load a csv file named as the list_name parameter from the data directory 
    using the get_list_path() function

    Parameters
    ----------
    name : string
        The name of the list

    Returns
    -------
    pd.DataFrame
        A DataFrame of the the content of the todo list.
    """

    return pd.read_csv(get_list_path(list_name))

## This method save the information of a list into a csv file
def store_list(df, list_name: str)  -> None:

    """ Stores the list 
    Save the dataframe as a csv document

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to be saved
    name : string
        The name of the list
    
    Returns
    -------
    None
    """

    df.to_csv(get_list_path(list_name), index=False)

## This method get path of a list
def get_list_path(list_name: str) -> str:

    """ Get the path of a specified list.
    Get the path of a list name

    Parameters
    ----------
    name : string
        The name of the list 

    Returns
    -------
    string
        The PATH_TO_DATA + name + .csv
    """

    return f"{PATH_TO_DATA}{get_list_filename(list_name)}"

## This method add a task to a list
def add_to_list(list_name: str, new_row: list) -> None:

    """ Add a new row to a given list name
    Load a csv file named as the list_name parameter from the data directory 
    Then assign new_row to the list pd.DataFrame.
    It saves the edited DataFrame with the store_list() function.

    Parameters
    ----------
    name : string
        The name of the list 
    
    new_row : list or pandas.Series
        New row of the list in the order ["created", "task", "summary", "status", "owner"]

    Returns
    -------
    None
    """

    df = load_list(list_name)
    df.loc[len(df.index)] = new_row
    store_list(df, list_name)