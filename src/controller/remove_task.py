'''Responsible for the CRUD operation: remove task'''

from typing import Any
from views import get_task_id
from communications import communications
from database_manager import database


def remove_controller(tasks: Any, action: str) -> None:
    '''
    Controller for removing a task

    Takes in:
    1) tasks - Tasks from the database, if any
    2) action - Action a user wants to perform, stored as a string
    '''
    if tasks:
        try:
            task_id = get_task_id.get_task_id(action)
        # Catch inputs that are not integers
        except ValueError:
            communications.incorrect_input()
            return None
        task_to_be_removed = (
            database.DatabaseRetrieve(database.DB_NAME)
            .get_task(task_id)
            )
        if task_to_be_removed is not None:
            if communications.confirm_choice() == "Yes":
                (database.DatabaseRemove(database.DB_NAME)
                 .remove_task(task_id))
                communications.task_removed_successfully()
                return None
            communications.operation_cancelled()
            return None
        else:
            communications.task_does_not_exist()
            return None
    else:
        communications.no_tasks()
        return None
