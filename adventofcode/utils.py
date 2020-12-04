import os

import requests


def get_cache_folder_path():
    pass


def get_session(session_id: str) -> requests.Session:
    session = requests.Session()
    session.cookies["session"] = session_id
    return session
