#!/usr/bin/env python
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

from user import User

import random

class Teacher(User):

    #pulls attributes from parent
    def __init__(self, first_name, last_name, knowledge = knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    #picks random element from list to "teach"
    def teach(self):
        return self.knowledge[random.randint(0,(len(knowledge) - 1))]