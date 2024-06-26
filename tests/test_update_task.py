'''Unit testing the use case: update task'''

import unittest  # Built in testing framework
import datetime
from util import util
from services import services
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
        self.current_date = util.DateUtils().full_date()
        self.date_in_two_weeks_time = (
            self.current_date + datetime.timedelta(weeks=2))
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
        create_task = services.create_new_task([
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
        (task_id1,
         title1,
         description1,
         category1,
         deadline1,
         priority1) = task1

        # Check if task has been inserted correctly
        self.assertTrue(task_id1 == self.task_id)
        self.assertTrue(title1 == "Coding")
        self.assertTrue(description1 == "Submit task 1")
        self.assertTrue(category1 == "personal")
        self.assertTrue(deadline1 == str(self.current_date))
        self.assertTrue(priority1 == 1)

        # Update task
        (database.DatabaseUpdate(self.database_name)
         .update_task(self.task_id, [
             "Bootcamp",
             "Submit all tasks",
             "coding",
             self.date_in_two_weeks_time,
             2
         ]))

        # Get task
        task1_updated = (database.DatabaseRetrieve(self.database_name)
                    .get_task(self.task_id))
        (task_id2,
         title2,
         description2,
         category2,
         deadline2,
         priority2) = task1_updated

        # Check if task has been updated
        self.assertTrue(task_id2 == self.task_id)
        self.assertTrue(title2 == "Bootcamp")
        self.assertTrue(description2 == "Submit all tasks")
        self.assertTrue(category2 == "coding")
        self.assertTrue(deadline2 == str(self.date_in_two_weeks_time))
        self.assertTrue(priority2 == 2)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
