'''Unit testing the use case: remove task'''

import unittest  # Built in testing framework
from util import util
from model import model
from database_manager import database


class TestRemoveTask(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.

    It contains one test case, which tests the use case:
    remove task
    '''
    def setUp(self):
        '''
        Establishes a connection to a database and creates the necessary
        tables
        '''
        # Task id is 1 as this is the first record which will be created
        # in the database
        self.task_id = 1
        self.database_name = 'test_task_manager.db'
        database.DatabaseCreate(self.database_name).create_tables()

    def tearDown(self) -> None:
        '''Drops all tables'''
        conn = database.DatabaseConnector(self.database_name)

        conn.cursor.execute('''DROP TABLE IF EXISTS task;''')
        conn.cursor.execute('''DROP TABLE IF EXISTS category;''')
        conn.cursor.execute('''DROP TABLE IF EXISTS deadline;''')
        conn.cursor.execute('''DROP TABLE IF EXISTS priority;''')

        conn.db.commit()
        conn.db.close()

    def test_if_task_removal_is_successful(self) -> None:
        '''
        Tests if task removal is successful
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
        # Check if task has been added to database
        task1 = (
            database.DatabaseRetrieve(self.database_name)
            .get_task(self.task_id))
        self.assertIsNotNone(task1)

        # delete task
        (database.DatabaseRemove(self.database_name)
         .remove_task(self.task_id))
        # Check if task has been deleted from database
        task1_removed = (
            database.DatabaseRetrieve(self.database_name)
            .get_task(self.task_id)
        )
        self.assertIsNone(task1_removed)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
