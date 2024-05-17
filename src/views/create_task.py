'''
A view: Displays to the user an interface where they can create
a task
'''

from util import util


def get_task_information(new: bool = False) -> list:
    '''
    Returns a list containing task information (e.g., task title,
    task description) to the controller
    '''
    new_task_str = ' new ' if new is True else ' '
    while True:
        task_title = input(f"\nWhat is the{new_task_str}task title:\n")
        task_description = input(
            f"What is the{new_task_str}task description:\n"
            )
        task_category = input(
            "What category do you want to put this task in:\n"
            )

        task_date = input(
            f"When is the{new_task_str}deadline (Please enter in this "
            f"format '01-1-{util.full_date().year}', as in day-month-year)\n"
            "\tNote: Please ensure that the deadline entered starts "
            "from today onwards:\n"
            )
        task_deadline = util.dmy_to_datetime_date(task_date)
        if task_deadline < util.full_date():
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
