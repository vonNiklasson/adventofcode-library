import requests

from . import utils


class Question:
    def __init__(self, base_url: str, session_id: str, working_dir: str, year: int, day: int, part_two: bool = False):
        self.base_url = base_url
        self.session_id = session_id
        self.working_dir = working_dir
        self.year = year
        self.day = day
        self.part_two = part_two

    @property
    def input_url(self):
        return (self.base_url + "/%d/day/%d/input") % (self.year, self.day)

    @property
    def answer_url(self):
        return (self.base_url + "/%d/day/%d/answer") % (self.year, self.day)
