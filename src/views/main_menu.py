'''
A view: Displays the main menu where a user can select an option
to perform on the tasks list
'''


def display_menu() -> int:
    '''
    Presents a menu to the user to perform actions on tasks list.
    It returns an integer (representing the users choice) to the
    controller
    '''
    user_choice = int(
        input(
            '''\nWould you like to:

                    1) View tasks
                    2) Create new task
                    3) Remove a task
                    4) Update a task
                    5) View a task
                    6) View priorities
                    7) View categories
                    8) View deadlines
                    9) Exit application

                    Enter selection: '''
        )
    )
    return user_choice
