'''A view: displays to the user all tasks'''

from typing import Any
from util.constants import constants


def view_tasks(tasks: Any) -> None:
    '''
    Takes in tasks (records from a database) and prints out it out
    '''
    print(" ")

    for task in tasks:
        task_id, title, _, _, deadline, _ = task
        print(f"\n{constants.TASK_ID_STRING}{task_id}"
              f"\n{constants.TASK_TITLE_STRING}{title.title()}"
              f"\n{constants.TASK_DEADLINE}{deadline}")

    print(f"\nYou have {len(tasks)} task(s) to do\n")
