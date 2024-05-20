'''Unit testing the use case: create task'''

import unittest  # Built in testing framework
from util import util
from model import model
from database_manager import database


class TestCreateTask(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.

    It contains one test case, which tests the use case:
    create task
    '''
    def setUp(self):
        '''
        Establishes a connection to a database and creates the necessary
        tables
        '''
        # Task id is 1 as this is the first record which will be created
        # in the database
        self.task_id = 1
        self.current_date = util.DateUtils().full_date()
        self.database_name = 'test_task_manager.db'
        database.DatabaseCreate(self.database_name).create_tables()

    def tearDown(self) -> None:
        '''Removes the task from the database and drops all tables'''
        (database.DatabaseRemove(self.database_name)
         .remove_task(self.task_id))
        conn = database.DatabaseConnector(self.database_name)

        conn.cursor.execute('''DROP TABLE IF EXISTS task;''')
        conn.cursor.execute('''DROP TABLE IF EXISTS category;''')
        conn.cursor.execute('''DROP TABLE IF EXISTS deadline;''')
        conn.cursor.execute('''DROP TABLE IF EXISTS priority;''')

        conn.db.commit()
        conn.db.close()

    def test_if_task_creation_is_successful(self) -> None:
        '''
        Tests if task creation was successful
        '''
        # Create task
        create_task = model.create_task([
            "Coding",
            "Submit task 1",
            "personal",
            self.current_date,
            1
        ])
        # Add to database
        database.DatabaseCreate(self.database_name).add_task(create_task)
        # Get task
        task1 = (database.DatabaseRetrieve(self.database_name)
                .get_task(self.task_id))

        task_id, title, description, category, deadline, priority = task1
        # Check if task was committed to database and if task
        # information was inserted correctly
        self.assertTrue(task_id == 1)
        self.assertTrue(title == "Coding")
        self.assertTrue(description == "Submit task 1")
        self.assertTrue(category == "personal")
        self.assertTrue(deadline == str(self.current_date))
        self.assertTrue(priority == 1)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
