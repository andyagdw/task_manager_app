'''Responsible for the CRUD operation: update task'''

from typing import Any
from views import (get_task_id,
                   create_task)
from communications import communications
from database_manager import database


def update_controller(tasks: Any, action: str, new: bool) -> None:
    '''
    Controller for updating a task

    Takes in:
    1) tasks - Tasks from a database, if any
    2) action - Action a user wants to perform, stored as a string
    '''
    if tasks:
        try:
            task_id = get_task_id.get_task_id(action)
        # Catch inputs that are not integers
        except ValueError:
            communications.incorrect_input()
            return None
        task_to_be_updated = (
            database.DatabaseRetrieve(database.DB_NAME).get_task(task_id)
        )
        if task_to_be_updated is not None:
            try:
                new_task_details = create_task.get_task_information(new)
            # Catch incorrect inputs
            except ValueError:
                communications.incorrect_input()
                return None
            (database.DatabaseUpdate(database.DB_NAME)
             .update_task(task_id, new_task_details))
            communications.task_updated()
            return None
        else:
            communications.task_does_not_exist()
            return None
    else:
        communications.no_tasks()
        return None
