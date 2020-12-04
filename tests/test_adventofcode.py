import pytest

from adventofcode import AdventOfCode
from adventofcode.exceptions import MissingSessionIdException


def test_exception_on_no_session_id():
    with pytest.raises(MissingSessionIdException):
        aoc = AdventOfCode()
