'''
Contains functions which keep the user updated on whats happening
within the application
'''


def task_added() -> None:
    '''
    Informs the user that the new task that they have created has been
    successfully added to the database
    '''
    print("\nTask successfully added👍\n")


def task_does_not_exist() -> None:
    '''
    Informs the user that a task does not exist within the database
    '''
    print("\nTask does not exist\n")


def task_removed_successfully() -> None:
    '''
    Informs the user that a task has been removed from the database
    '''
    print("\nTask has been removed successfully 😁\n")


def task_updated() -> None:
    '''Inform the user that a task has been updated'''
    print("\nTask has been updated👌\n")


def no_tasks() -> None:
    '''Informs the user that no tasks has been created yet'''
    print("\nThere are no tasks 😉")


def operation_cancelled() -> None:
    '''Informs the user that an operation has been cancelled'''
    print("\nOperation cancelled\n")


def incorrect_input() -> None:
    '''Informs the user that they have entered an incorrect input'''
    print("\nThere was an error! You have been directed back to the main"
          " screen")


def confirm_choice() -> str:
    '''
    Gets user choice (to remove a task) from the database and returns
    this choice to the controller
    '''
    user_choice = input(
            "\nAre you sure you want to remove this task? 'Yes' or 'No'\n"
            "(Danger Zone: Please note that tasks cannot be retrieved "
            "once deleted):\n"
            )
    return user_choice


def exit_application() -> None:
    '''Prints to the user to "have a good day"'''
    print("Have a good day👋")


def incorrect_priority_level() -> None:
    '''
    Informs the user that the priority level they have entered is
    incorrect
    '''
    print(
        "\nOops🤔. Please enter a priority level that is either "
        "1, 2, or 3"
        )


def incorrect_deadline() -> None:
    '''
    Informs the user that the deadline they have entered is
    incorrect
    '''
    print(
        "\nOops🤔. Please enter a deadline that starts "
        "from today onwards"
        )


def no_input(string: str) -> None:
    '''
    Informs the user that they did not enter an input
    The string represents the part where they failed to provide an input
    '''
    print(f"Oops🤔. Please enter a task {string}")
