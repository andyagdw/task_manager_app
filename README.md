# Task Manager Application 💥

A Python-based Task Manager application employing the
'Model-View-Controller' pattern 😁. It facilitates users to
effortlessly create, update, remove, or view tasks, deadlines,
priorities, and categories.

## Features ✨

1. Create a new task: Easily add new tasks to a database
2. Update a task: Modify existing tasks as needed
3. Remove a task: Delete tasks that are no longer relevant
4. View task(s): Dive into detailed information about specific tasks or get an overview of all tasks.
5. View deadlines: Stay on top of your deadlines
6. View priorities: Prioritise tasks based on their importance
7. View categories: Organise tasks effortlessly into different categories

## Getting started ✅

Follow these simple steps to get started with the Task Manager Application:

1. Clone the repository to your local machine <br />
   `git clone https://github.com/andyagdw/bootcamp_coding_tasks.git`
2. Navigate to the project directory <br />
   `cd bootcamp_coding_tasks/task_manager`
3. Open Visual Studio Code <br />
   `code .`
4. Set up a virtual environment in Visual Studio Code terminal. <br />
   Make sure you are in the project directory.

   Using venv:

   `python -m venv venv` <br />
   For Python 3.3 or newer: <br />
   `python3 -m venv venv`

   Using virtualenv:

   ```
   pip install virtualenv
   virtualenv venv
   ```

5. Activate the virtual environment

   Using venv:

   Windows: <br />
   `venv\Scripts\activate` <br />
   Unix\Mac: <br />
   `source venv/bin/activate`

   Using virtualenv: <br />

   Windows: <br />
   `venv\Scripts\activate` <br />
   Unix\Mac: <br />
   `source venv/bin/activate`

6. Ensure project dependencies are installed: <br />

```
- flake8==7.0.0
- mccabe==0.7.0
- pycodestyle==2.11.1
- pyflakes==3.2.0
```

7. In the project directory, run the main script using: <br />
   `python src\main.py`

## Accessing the Database 📊

If you want to explore the database, I suggest using DB Browser. Why? Not only is it a high quality,
and visual tool, it is free! Follow these steps:

1. Download DB Browser: <br />
   If you haven't already, download and install DB Browser for SQLite (Add link)

2. Open database with DB Browser: <br />
   Locate and open the database file using the 'Open Database' option in the File menu - it should be inside the project directory.

3. Explore the Database
   Once the database is opened, you can browse through the tables and data using the intuitive interface of DB Browser.

You're all set! Start managing your tasks efficiently with the Task Manager Application. 🚀
