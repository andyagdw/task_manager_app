'''Displays a task'''

from typing import Any
from util.constants import constants


def view_task(task: Any) -> None:
    '''Takes in a task (a record from a database) and prints it'''
    task_id, title, description, category, deadline, priority = task
    print(f"\n{constants.TASK_ID_STRING}{task_id}"
          f"\n{constants.TASK_TITLE_STRING}{title.title()}"
          f"\n{constants.TASK_DESCRIPTION_STRING}{description}"
          f"\n{constants.TASK_CATEGORY}{category.title()}"
          f"\n{constants.TASK_DEADLINE}{deadline}"
          f"\n{constants.TASK_PRIORITY}{priority}")
