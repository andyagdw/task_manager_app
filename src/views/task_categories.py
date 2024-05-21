'''Displays tasks grouped according to categories'''

from typing import Any
from util.constants import constants


def view_categories(tasks: Any):
    '''
    Takes in tasks (records from a database). Tasks are then printed out
    grouped by their category name
    '''
    categories_dict = {}

    for task in tasks:
        _, _, _, category, _, _ = task
        if category not in categories_dict:
            categories_dict[category] = [task]
        else:
            categories_dict[category].append(task)

    for category_name, category_tasks in sorted(categories_dict.items()):
        print(f"\n*********** {category_name.title()} ***********")
        for task in category_tasks:
            task_id, title, _, _, _, _ = task
            print(
                f"\n{constants.TASK_ID_STRING}{task_id}"
                f"\n{constants.TASK_TITLE_STRING}{title.title()}"
                )
