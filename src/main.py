'''
This module is the main entry point of the application
It imports the start_application function from the main_controller
module, which starts the task manager application
'''

from controller import main_controller

# Only call the function when the script is executed directly
if __name__ == "__main__":

    main_controller.start_application()
