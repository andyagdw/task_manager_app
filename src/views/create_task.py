'''
Displays to the user an interface where they can create
a task
'''

import datetime
from util import util
from communications import communications

def get_task_information(task_categories: list,
                         update_current_task: bool = False
                         ) -> list:
    '''
    Returns a list containing task information (e.g., task title,
    task description) to the controller

    Takes in:
    1) task_categories - A list of unique task categories from the
    database, if any
    2) update_current_task - The boolean value 'True', meaning that the
    user wants to update a task
    '''
    categories_str = (
        f"Your categories: {task_categories}\n"
        )
    new_task_str = ' new ' if update_current_task is True else ' '

    while True:
        task_title = get_task_title(new_task_str)
        if task_title is None:
            continue
        task_description = get_task_description(new_task_str)
        if task_description is None:
            continue
        task_category = get_task_category(categories_str,
                                          task_categories)
        if task_category is None:
            continue
        task_deadline = get_task_deadline(new_task_str)
        if task_deadline is False:
            continue
        task_priority = get_task_priority(new_task_str)
        if task_priority is False:
            continue

        return [
            task_title,
            task_description,
            task_category,
            task_deadline,
            task_priority]


def get_task_title(new_task_str: str) -> None | str:
    '''Gets the task title to create a new task'''
    task_title = input(f"\nWhat is the{new_task_str}task title:\n")
    if not task_title:
        title_str = 'title'
        communications.no_input(title_str)
        return None
    return task_title


def get_task_description(new_task_str: str) -> None | str:
    '''Gets the task description to create a new task'''
    task_description = input(
        f"\nWhat is the{new_task_str}task description:\n"
        )
    if not task_description:
        description_str = 'description'
        communications.no_input(description_str)
        return None
    return task_description


def get_task_category(categories_str: str,
                      task_categories: list) -> None | str:
    '''Gets the task category to create a new task'''
    task_category = input(
        "\nWhat category do you want to put this task in" +
        (":\n" + categories_str if task_categories else ":\n")
        )
    if not task_category:
        category_str = 'category'
        communications.no_input(category_str)
        return None
    return task_category


def get_task_deadline(new_task_str: str) -> bool | datetime.date:
    '''Gets the task deadline to create a new task'''
    task_date = input(
        f"\nWhen is the{new_task_str}deadline (Please enter in this "
        f"format 'DD-MM-YYYY', as in day-month-year)\n- Note: "
        "Please ensure that the deadline entered starts "
        "from today onwards:\n"
        )
    task_deadline = util.DateUtils().dmy_to_datetime_date(task_date)
    if task_deadline < util.DateUtils().full_date():
        communications.incorrect_deadline()
        return False
    return task_deadline


def get_task_priority(new_task_str: str) -> bool | int:
    '''Gets the task priority to create a new task'''
    task_priority = int(input(
        f"\nWhat is the{new_task_str}priority level"
        "\n(1 = High Priority, "
        "2 = Medium Priority, "
        "3 = Low Priority):\n")
                        )
    if task_priority not in {1, 2, 3}:
        communications.incorrect_priority_level()
        return False
    return task_priority
