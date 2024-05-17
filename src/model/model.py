'''This module contains the models.'''

import datetime
from typing import Any


class Category:
    '''A class to represent a category name'''

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        '''Returns a category name'''
        return f"Category: {self.name}"


##########################
class Priority:
    '''A class to represent a priority level'''

    def __init__(self, priority: int) -> None:
        self.priority = priority

    def __str__(self) -> str:
        '''Returns a priority level'''
        return f"Priority: {self.priority}"


##########################
class Deadline:
    '''A class to represent a date'''

    def __init__(self, deadline: datetime.date) -> None:
        self.deadline = deadline

    def __str__(self) -> str:
        '''Returns a date'''
        return f"Deadline: {self.deadline}"


##########################
class Task:
    '''A class to represent a task'''

    def __init__(self,
                 title: str,
                 description: str,
                 category: Category,
                 deadline: Deadline,
                 priority_id: Priority) -> None:

        self.title = title
        self.description = description
        self.category = category
        self.deadline = deadline
        self.priority_id = priority_id

    def __str__(self) -> str:
        '''Returns all the information about a task'''
        return (
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"{self.category}\n"
            f"{self.deadline}\n"
            f"{self.priority_id}\n"
        )


##########################
def create_task(task_information: list) -> Any:
    '''
    Receives task information and creates a new task. It then returns
    the new task to the controller
    '''
    title, description, category, deadline, priority = task_information

    new_task = Task(
        title,
        description,
        Category(category),
        Deadline(deadline),
        Priority(priority)
    )
    return new_task
