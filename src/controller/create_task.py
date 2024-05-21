'''Responsible for the CRUD operation: create task'''

from views import create_task
from services import services
from communications import communications
from database_manager import database


def create_controller() -> None:
    '''Controller responsible for creating a task'''
    task_categories = (database.DatabaseRetrieve(database.DB_NAME)
                       .get_task_categories())
    try:
        # Returns task information
        task_info = create_task.get_task_information(task_categories)
    # Catch any incorrect inputs
    except ValueError:
        communications.incorrect_input()
        return None
    new_task = services.create_new_task(task_info)
    database.DatabaseCreate(database.DB_NAME).add_task(new_task)
    communications.task_added()
    return None
