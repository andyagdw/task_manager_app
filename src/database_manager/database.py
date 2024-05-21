'''Manages database connections and operations'''

import sqlite3
from typing import Any

DB_NAME = '../task_manager.db'


class DatabaseConnector:
    '''A class for connecting to a database

    It contains one function:

    1) task_exists - Checks if there are tasks in a database
    '''
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.db = sqlite3.connect(db_name)
        # Enable foreign key constraint
        self.db.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.db.cursor()

    def task_exists(self) -> None | Any:
        '''Checks if there are tasks in a database

        If there are, it returns the tasks.
        If not, it returns None
        '''
        sql_formula = '''SELECT * FROM task;'''
        tasks = self.cursor.execute(sql_formula).fetchall()
        if tasks:
            self.db.close()
            return tasks
        self.db.close()
        return None


class DatabaseCreate(DatabaseConnector):
    '''
    Inherits from the DatabaseConnector class, and is responsible for
    the CRUD operation: create

    It contains two functions:

    1) create_tables - Creates the necessary tables for the task
    manager application
    2) add_task - Creates a new task record
    '''
    def create_tables(self) -> None:
        '''
        Creates the necessary tables for the task manager application
        and commits them to the database if they do not exist

        Tables are:
        1) task
        2) category
        3) deadline
        4) priority
        '''
        # Store deadline as TEXT as SQLite does not have DATE datatype
        task_table = '''CREATE TABLE IF NOT EXISTS task
                (task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                category TEXT,
                deadline TEXT,
                priority INTEGER
                );'''
        self.cursor.execute(task_table)
        self.db.commit()

        category_table = '''CREATE TABLE IF NOT EXISTS category
                (task_id INTEGER,
                category_name TEXT,
                FOREIGN KEY (task_id) REFERENCES task(task_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                PRIMARY KEY (task_id, category_name)
                );'''
        self.cursor.execute(category_table)
        self.db.commit()

        deadline_table = '''CREATE TABLE IF NOT EXISTS deadline
                (task_id INTEGER,
                due_date TEXT,
                FOREIGN KEY (task_id) REFERENCES task(task_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                PRIMARY KEY (task_id, due_date)
                );'''
        self.cursor.execute(deadline_table)
        self.db.commit()

        priority_table = '''CREATE TABLE IF NOT EXISTS priority
                    (task_id INTEGER,
                    priority INTEGER,
                    FOREIGN KEY (task_id) REFERENCES task(task_id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                    PRIMARY KEY (task_id, priority)
                    );'''
        self.cursor.execute(priority_table)
        self.db.commit()

        self.db.close()

    def add_task(self, new_task: Any) -> None:
        '''
        Takes in a new task and adds the new task to the
        database
        '''
        create_task_formula = '''INSERT INTO task(title,
                                description, category, deadline,
                                priority)
                                VALUES(?, ?, ?, date(?), ?);
                                '''
        # Convert to string as SQLite date function requires this
        new_task_deadline = str(new_task.deadline.deadline)
        # Convert to lower to prevent duplicate category names in
        # different formats (e.g., personal, Personal)
        # Remove any trailing or leading whitespace
        new_task_category_name = new_task.category.name.lower().strip()

        self.cursor.execute(create_task_formula,
                            (new_task.title.strip(),
                             new_task.description.strip(),
                             new_task_category_name,
                             new_task_deadline,
                             new_task.priority_id.priority)
                            )
        self.db.commit()

        # Get recently added record task_id
        get_task_id = self.cursor.execute('''SELECT task_id FROM task
                    ORDER BY task_id DESC LIMIT 1;''').fetchone()

        # Destructure tuple to get task_id
        task_id, = get_task_id

        category_table_formula = '''INSERT INTO category
                                (task_id, category_name)
                                VALUES(?, ?);
                                '''
        self.cursor.execute(category_table_formula,
                            (task_id,
                             new_task_category_name))
        self.db.commit()

        deadline_table_formula = '''INSERT INTO deadline
                                (task_id, due_date)
                                VALUES(?, date(?));
                                '''
        self.cursor.execute(deadline_table_formula,
                            (task_id,
                             new_task_deadline)
                            )
        self.db.commit()

        priority_table_formula = '''INSERT INTO priority
                                (task_id, priority)
                                VALUES(?, ?);
                                '''
        self.cursor.execute(priority_table_formula,
                            (task_id,
                             new_task.priority_id.priority))
        self.db.commit()

        self.db.close()


class DatabaseRemove(DatabaseConnector):
    '''
    Inherits from the DatabaseConnector class, and is responsible for
    the CRUD operation: remove

    It contains one function:

    1) remove_task - Removes a task from the database
    '''
    def remove_task(self, task_id: int) -> None:
        '''Removes a task from the database'''
        delete_task_formula = '''DELETE FROM task WHERE task_id=?;'''
        self.cursor.execute(delete_task_formula, (task_id,))
        self.db.commit()
        self.db.close()


class DatabaseRetrieve(DatabaseConnector):
    '''
    Inherits from the DatabaseConnector class, and is responsible for
    the CRUD operation: read

    It contains two functions:

    1) get_tasks - Retrieves tasks from the database
    2) get_task - Retrieves a task from the database
    '''
    def get_tasks(self) -> Any:
        '''Retrieves tasks from the database'''
        retrieve_tasks_formula = '''SELECT * FROM task;'''
        tasks = self.cursor.execute(retrieve_tasks_formula).fetchall()
        self.db.close()
        return tasks

    def get_task(self, task_id: int) -> Any:
        '''Retrieves a task from the database'''
        retrieve_task_formula = '''SELECT * FROM task WHERE task_id=?;
                                '''
        task = (
            self.cursor.execute(retrieve_task_formula, (task_id,))
            .fetchone())
        self.db.close()
        return task

    def get_task_categories(self) -> list:
        '''
        Retrieves task categories from the database and returns
        a unique list
        '''
        retrieve_task_categories_formula = '''
                                SELECT DISTINCT category FROM task
                                ORDER BY category;
                                '''
        task_categories = (self.cursor
                           .execute(retrieve_task_categories_formula)
                           .fetchall())
        category_list = []
        for task in task_categories:
            category, = task
            category_list.append(category)
        self.db.close()
        return category_list


class DatabaseUpdate(DatabaseConnector):
    '''
    Inherits from the DatabaseConnector class, and is responsible for
    the CRUD operation: update

    It contains one function:

    1) update_task - Updates a task from the database
    '''
    def update_task(self, task_id: int, new_task_details: list) -> None:
        '''Updates a task from the database'''
        update_task_formula = '''UPDATE task SET
                            title=?,
                            description=?,
                            category=?,
                            deadline=date(?),
                            priority=?
                            WHERE task_id=?;'''

        title, description, category, due_date, priority = new_task_details
        # Convert to string from datetime.date as SQLite date function
        # requires this
        deadline = str(due_date)
        # Convert to lower to prevent duplicate category names in
        # different formats (e.g., personal, Personal)
        # Remove any trailing or leading whitespace
        category_name = category.lower().strip()

        self.cursor.execute(update_task_formula,
                            (title.strip(),
                             description.strip(),
                             category_name,
                             deadline,
                             priority,
                             task_id))
        self.db.commit()

        category_formula = '''UPDATE category SET category_name=?
                            WHERE task_id=?;'''
        self.cursor.execute(category_formula,
                            (category_name,
                             task_id)
                            )
        self.db.commit()

        deadline_formula = '''UPDATE deadline SET due_date=date(?)
                            WHERE task_id=?;'''
        self.cursor.execute(deadline_formula,
                            (deadline,
                             task_id))
        self.db.commit()

        priority_formula = '''UPDATE priority SET priority=?
                        WHERE task_id=?;'''
        self.cursor.execute(priority_formula,
                            (priority,
                             task_id))
        self.db.commit()
        self.db.close()
