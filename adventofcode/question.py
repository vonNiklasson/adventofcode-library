import requests
import warnings

from . import utils


class Question:
    def __init__(self, base_url: str, session_id: str, working_dir: str, year: int, day: int, part_two: bool = False):
        # Raise a warning if the year is not in a tested year.
        if year != 2020:
            warnings.warn('adventofcode-library has only been tested with 2020 years calendar. Use at your own risk.')

        # Make sure the day is within bounds.
        if not 1 <= day <= 25:
            raise IndexError('Day must be between 1 and 25 (inclusive).')

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
