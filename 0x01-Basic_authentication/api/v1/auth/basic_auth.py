#!/usr/bin/env python3
""" Basic Auth Module
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Auth Module Class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the base64 encoded string from the
        authorization header
        Args:
            authorization_header: authorization header
        Returns:
            base64 encoded string
        Raises:
            ValueError: if authorization_header
            is not a valid string
        """
        if not authorization_header or \
                type(authorization_header) is not str or \
                authorization_header.split()[0].lower() != "basic":
            return None
        return authorization_header.split(" ")[1]
