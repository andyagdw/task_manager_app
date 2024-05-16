'''This module contains the controller (i.e., the start_application
function). It recieves user input from the views, interacts with the
models to process the input, and updates the views accordingly.
'''
from controller import (remove_task,
                        update_task,
                        create_task,
                        read_task)
from views import main_menu
from communications import communications
from database_manager import database


def start_application() -> None:
    '''
    The main controller. Interacts with other controllers and allows a
    user to perform actions on the tasks list
    '''
    # Create the necessary tables if they don't exist
    database.DatabaseCreate(database.DB_NAME).create_tables()
    # Stores tasks, if any
    tasks = database.DatabaseConnector(database.DB_NAME).task_exists()

    try:
        user_choice = main_menu.display_menu()
    except ValueError:  # Catch inputs that are not integers
        communications.incorrect_input()
        return start_application()

    match user_choice:
        case 1 | 5 | 6 | 7 | 8:  # Read a task or tasks
            action = 'view'
            read_task.read_controller(user_choice, tasks, action)
        case 2:  # Create new task
            create_task.create_controller()
        case 3:  # Remove a task
            action = 'remove'
            remove_task.remove_controller(tasks, action)
        case 4:  # Update a task
            action = 'update'
            update_task.update_controller(tasks, action)
        case 9:  # Exit application
            communications.exit_application()
            return None
        case _:  # Options that do not match the above
            communications.incorrect_input()
            return start_application()

    return start_application()
