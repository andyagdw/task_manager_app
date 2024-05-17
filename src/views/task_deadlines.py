'''A view: Displays tasks grouped according to task deadlines'''

from typing import Any
from datetime import date
import datetime
from util import util
from util.constants import constants


def view_deadlines(tasks: Any):
    '''
    Takes in tasks (records from a database). Tasks are then printed out
    grouped by their deadline date

    The deadline dates are:

    1. Passed Deadline
    2. Due Today
    3. Due Tomorrow
    4. Due Later On
    '''
    deadlines_dict = {"Passed Deadline": [],
                      "Due Today": [],
                      "Due Tomorrow": [],
                      "Due Later On": []
                      }

    today = date.today()
    tomorrow = today + datetime.timedelta(days=1)

    for task in tasks:
        # Retrieve only the deadline
        _, _, _, _, due_date, _ = task
        deadline = util.ymd_to_datetime_date(due_date)
        if deadline < today:
            deadlines_dict["Passed Deadline"].append(task)
        elif deadline == today:
            deadlines_dict["Due Today"].append(task)
        elif deadline == tomorrow:
            deadlines_dict["Due Tomorrow"].append(task)
        else:
            deadlines_dict["Due Later On"].append(task)

    for deadline_date, deadline_tasks in deadlines_dict.items():
        print(f"\n********* {deadline_date} *********")
        if deadline_tasks:  # Check if key is empty
            for task in deadline_tasks:
                (task_id,
                 title,
                 _,
                 _,
                 deadline,
                 _) = task
                task_info = (
                    f"\n{constants.TASK_ID_STRING}{task_id}"
                    f"\n{constants.TASK_TITLE_STRING}{title.title()}"
                    )
                # Show deadline for dates that are passed or due later
                if deadline_date in ('Passed Deadline', 'Due Later On'):
                    print(
                        f"{task_info}\n{constants.TASK_DEADLINE}"
                        f"{deadline}\n"
                        )
                else:
                    print(task_info)
        else:
            print("No tasks due\n")
