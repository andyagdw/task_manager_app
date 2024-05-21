'''
Contains business logic that is reused across different parts of the
application
'''

from typing import Any
from model import model

def create_new_task(task_information: list) -> Any:
    '''
    Receives task information and creates a new task. It then returns
    the new task to the controller
    '''
    title, description, category, deadline, priority = task_information

    new_task = model.Task(
        title,
        description,
        model.Category(category),
        model.Deadline(deadline),
        model.Priority(priority)
    )
    return new_task
