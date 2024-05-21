'''
Displays to the user an interface where they can enter a task
id
'''


def get_task_id(action: str) -> int:
    '''
    Takes in an action (an operation a user wants to perform on a task)
    and returns a task_id back to the controller
    '''
    question = f"\nWhat task do you want to {action}? Enter ID:\n"

    task_id = int(input(question))
    return task_id
