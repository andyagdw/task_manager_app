'''A view: Displays tasks grouped according to task priorities'''

from typing import Any
from util.constants import constants


def view_priorities(tasks: Any):
    '''
    Takes in tasks (records from a database). Tasks are then grouped
    together according to their priority level

    They are then printed out in descending order - from highest
    priority to lowest

    The priority levels are:
    1 (High Priority)
    2 (Medium Priority)
    3 (Low Priority)
    '''
    priorities_dict = {1: [], 2: [], 3: []}

    for value in tasks:
        *_, priority = value  # Retrieve only priority
        priorities_dict[priority].append(value)

    for priority_key, priority_tasks in priorities_dict.items():
        priority_str = (
            "High" if priority_key == 1
            else ("Medium" if priority_key == 2 else "Low")
        )
        print(f"\n********* {priority_str} Priority *********")
        if priority_tasks:  # Check if empty
            for task in priority_tasks:
                (task_id, title, description, category,
                 deadline, priority) = task
                print(f"\n{constants.TASK_ID_STRING}{task_id}"
                      f"\n{constants.TASK_TITLE_STRING}{title.title()}"
                      f"\n{constants.TASK_DESCRIPTION_STRING}{description}"
                      f"\n{constants.TASK_CATEGORY}{category.title()}"
                      f"\n{constants.TASK_DEADLINE}{deadline}"
                      )
        else:
            print("No task with this priority\n")
