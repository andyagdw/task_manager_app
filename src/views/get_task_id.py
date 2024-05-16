'''
A view: displays to the user a screen where they can enter a task
id
'''


def get_task_id(action: str) -> int:
    '''
    Takes in an action (an operation they want to perform on a task)
    and returns a task_id back to the controller
    '''
    match action:
        case 'update':
            question = (
                "\nWhat task do you want to update? Enter ID:\n")
        case 'remove':
            question = (
                "\nWhat task do you want to remove: Enter ID:\n"
            )
        case 'read':
            question = (
                "\nWhat task do you want to view? Enter ID:\n"
            )

    task_id = int(input(question))
    return task_id
