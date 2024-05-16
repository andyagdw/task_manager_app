'''Performs a CRUD operation: read task'''

from typing import Any
from views import (all_tasks,
                   get_task_id,
                   view_task,
                   task_categories,
                   task_deadlines,
                   task_priorities)
from communications import communications
from database_manager import database


def read_controller(user_choice: int, tasks: Any, action: str) -> None:
    '''
    Controller for reading a task or many tasks

    Takes in:
    1) user_choice - Action a user wants to perform stored as an integer
    2) tasks - Tasks from a database, if any
    3) action - Action a user wants to perform stored as a string
    '''
    match user_choice:
        case 1:  # View tasks
            # Check if there are tasks in the tasks list
            if tasks:
                _tasks_ = (
                    database.DatabaseRetrieve(database.DB_NAME)
                    .get_tasks()
                    )
                all_tasks.view_tasks(_tasks_)
                return None
            else:
                # Informs the user that there are no tasks
                communications.no_tasks()
                return None
        case 5:  # View a task
            if tasks:
                try:
                    task_id = get_task_id.get_task_id(action)
                # Catch inputs that are not integers
                except ValueError:
                    communications.incorrect_input()
                    return None
                task_to_be_viewed = (
                    database.DatabaseRetrieve(database.DB_NAME)
                    .get_task(task_id)
                    )
                if task_to_be_viewed is not None:
                    view_task.view_task(task_to_be_viewed)
                    return None

                communications.task_does_not_exist()
                return None
            else:
                communications.no_tasks()
                return None
        case 6:  # View priorities
            if tasks:
                tasks_sorted_by_priority = (
                    database.DatabaseRetrieve(database.DB_NAME)
                    .get_tasks())
                task_priorities.view_priorities(tasks_sorted_by_priority)
                return None

            communications.no_tasks()
            return None
        case 7:  # View categories
            if tasks:
                tasks_sorted_by_category = (
                    database.DatabaseRetrieve(database.DB_NAME)
                    .get_tasks())
                task_categories.view_categories(tasks_sorted_by_category)
                return None

            communications.no_tasks()
            return None
        case 8:  # View deadlines
            if tasks:
                tasks_sorted_by_deadline = (
                    database.DatabaseRetrieve(database.DB_NAME)
                    .get_tasks())
                task_deadlines.view_deadlines(tasks_sorted_by_deadline)
                return None

            communications.no_tasks()
            return None
