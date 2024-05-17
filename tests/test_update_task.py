'''Unit testing the use case: update task'''

import unittest  # Built in testing framework
from util import util
from model import model
from database_manager import database


class TestUpdateTask(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.

    It contains one test case, which tests the use case:
    update task
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

    def test_if_task_update_is_successful(self) -> None:
        '''
        Tests if updating a task is successful
        '''
        # Create task
        current_date = util.full_date()
        create_task = model.create_task([
            "Coding",
            "Submit task 1",
            "personal",
            current_date,
            1
        ])
        # Add to database
        database.DatabaseCreate(self.database_name).add_task(create_task)

        # Get task
        current_task = (database.DatabaseRetrieve(self.database_name)
                        .get_task(self.task_id))
        (task_id1,
         title1,
         description1,
         category1,
         deadline1,
         priority1) = current_task

        # Check if task has been inserted correctly
        self.assertTrue(task_id1 == self.task_id)
        self.assertTrue(title1 == "Coding")
        self.assertTrue(description1 == "Submit task 1")
        self.assertTrue(category1 == "personal")
        self.assertTrue(deadline1 == str(current_date))
        self.assertTrue(priority1 == 1)

        # Update task
        new_date = util.dmy_to_datetime_date('01-01-2030')

        (database.DatabaseUpdate(self.database_name)
         .update_task(self.task_id, [
             "Bootcamp",
             "Submit all tasks",
             "coding",
             new_date,
             2
         ]))

        # Get task
        new_task = (database.DatabaseRetrieve(self.database_name)
                    .get_task(self.task_id))
        (task_id2,
         title2,
         description2,
         category2,
         deadline2,
         priority2) = new_task

        # Check if task has been updated
        self.assertTrue(task_id2 == self.task_id)
        self.assertTrue(title2 == "Bootcamp")
        self.assertTrue(description2 == "Submit all tasks")
        self.assertTrue(category2 == "coding")
        self.assertTrue(deadline2 == str(new_date))
        self.assertTrue(priority2 == 2)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
