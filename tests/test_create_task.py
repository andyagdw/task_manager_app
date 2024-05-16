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
        # Task id is 1 as this is the first record in database
        self.task_id = 1
        self.database_name = 'test_task_manager.db'
        database.DatabaseCreate(self.database_name).create_tables()

    def tearDown(self) -> None:
        '''Removes the task from the database and drops all tables'''
        (database.DatabaseRemove(self.database_name)
         .remove_task(self.task_id))
        conn = database.DatabaseConnector(self.database_name)

        conn.cursor.execute('''DROP TABLE IF EXISTS task''')
        conn.cursor.execute('''DROP TABLE IF EXISTS category''')
        conn.cursor.execute('''DROP TABLE IF EXISTS deadline''')
        conn.cursor.execute('''DROP TABLE IF EXISTS priority''')

        conn.db.commit()
        conn.db.close()

    def test_if_task_creation_was_success(self) -> None:
        '''
        Tests if task creation was successful
        '''
        # Create task
        create_task = model.create_task([
            "Coding",
            "Submit task 1",
            "personal",
            util.full_date(),
            1
        ])
        # Add to database
        database.DatabaseCreate(self.database_name).add_task(create_task)
        # Get task
        task = (database.DatabaseRetrieve(self.database_name)
                .get_task(self.task_id))

        task_id, title, description, category, deadline, priority = task
        # Check if task was committed to database and if task
        # information was inserted correctly
        self.assertEqual(task_id, 1)
        self.assertEqual(title, "Coding")
        self.assertEqual(description, "Submit task 1")
        self.assertEqual(category, "personal")
        self.assertEqual(deadline, str(util.full_date()))
        self.assertEqual(priority, 1)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
