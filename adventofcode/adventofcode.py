import os

import requests

from . import utils
from .exceptions import MissingSessionIdException
from .question import Question


class AdventOfCode:

    BASE_URL = "https://adventofcode.com"

    def __init__(self, session_id: str = None, working_dir: str = None):
        session_id = os.getenv("session_id", None) if session_id is None else session_id
        if session_id is None:
            raise MissingSessionIdException()

        working_dir = os.getcwd() if working_dir is None else working_dir

        self.session_id = session_id
        self.working_dir = working_dir

    def get_question(self, year: int, day: int, part_two: bool = False) -> Question:
        return Question(
            base_url=self.BASE_URL,
            session_id=self.session_id,
            working_dir=self.working_dir,
            year=year,
            day=day,
            part_two=part_two,
        )

    def validate_session(self):
        session = utils.get_session(self.session_id)
        session = session.get(self.login_url)

    @property
    def login_url(self):
        return self.BASE_URL + "/login"
