#!/usr/bin/env python3
""" Auth Module
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Module Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ requires the given auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ requires the given auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ requires the given auth user
        """
        return None
