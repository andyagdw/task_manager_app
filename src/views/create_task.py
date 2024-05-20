'''
A view: Displays to the user an interface where they can create
a task
'''
from util import util


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
        f"\tExisting categories are: {task_categories}\n"
        )
    new_task_str = ' new ' if update_current_task is True else ' '

    while True:
        task_title = input(f"\nWhat is the{new_task_str}task title:\n")
        task_description = input(
            f"What is the{new_task_str}task description:\n"
            )
        task_category = input(
            "What category do you want to put this task in" +
            (":\n" + categories_str if task_categories else ":\n")
            )

        task_date = input(
            f"When is the{new_task_str}deadline (Please enter in this "
            f"format 'DD-MM-YYYY', as in day-month-year)\n\tNote: "
            "Please ensure that the deadline entered starts "
            "from today onwards:\n"
            )
        task_deadline = util.DateUtils().dmy_to_datetime_date(task_date)
        if task_deadline < util.DateUtils().full_date():
            print(
                "\nOops🤔. Please enter a deadline that starts "
                "from today onwards"
                )
            continue

        task_priority = int(input(
            f"What is the{new_task_str}priority level"
            "\n(1 = High Priority, "
            "2 = Medium Priority, "
            "3 = Low Priority):\n")
                            )
        if task_priority not in {1, 2, 3}:
            print(
                "\nOops🤔. Please enter a priority level that is either "
                "1, 2, or 3"
            )
            continue

        return [
            task_title,
            task_description,
            task_category,
            task_deadline,
            task_priority]
