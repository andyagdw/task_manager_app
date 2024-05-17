'''Responsible for the CRUD operation: create task'''

from views import create_task
from model import model
from communications import communications
from database_manager import database


def create_controller() -> None:
    '''Controller responsible for creating a task'''
    try:
        # Returns task information
        task_info = create_task.get_task_information()
    # Catch any incorrect inputs
    except ValueError:
        communications.incorrect_input()
        return None
    new_task = model.create_task(task_info)
    database.DatabaseCreate(database.DB_NAME).add_task(new_task)
    communications.task_added()
    return None
