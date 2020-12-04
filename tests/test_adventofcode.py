import pytest
import os

from adventofcode import AdventOfCode
from adventofcode.exceptions import MissingSessionIdException


class TestInitialisation:

    def test_provided_session_id(self):
        """
        Make sure an exception is not raised when Session ID is provided directly
        """
        aoc = AdventOfCode('valid session id')

    def test_environ_session_id(self, monkeypatch):
        """
        Make sure an exception is not raised when Session ID is provided from environ
        """
        monkeypatch.setenv('session_id', 'valid_session_id')
        aoc = AdventOfCode()

    def test_raises_exception_on_no_session_id(self):
        """
        Make sure an exception is raised when no Session Id is provided
        """
        with pytest.raises(MissingSessionIdException):
            aoc = AdventOfCode()


class TestValidSession:

    def test_valid_session_with_valid_session_id(self, requests_mock):
        requests_mock.get(AdventOfCode.BASE_URL, text='Body text here and a [Log Out] button')
        aoc = AdventOfCode('valid_session')
        assert aoc.validate_session() is True

    def test_valid_session_with_invalid_session_id(self, requests_mock):
        requests_mock.get(AdventOfCode.BASE_URL, text='Body text here without any button')
        aoc = AdventOfCode('invalid_session')
        assert aoc.validate_session() is False
