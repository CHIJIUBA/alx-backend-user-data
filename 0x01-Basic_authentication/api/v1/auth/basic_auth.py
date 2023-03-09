#!/usr/bin/env python3
""" Basic Auth Module
"""
from flask import request
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the base64 encoded string
        Args:
            base64_authorization_header: base64 encoded string
        Returns:
            decoded base64 encoded string
        Raises:
            Exception: if base64_authorization_header
            is not a valid base64 encoded string
        """
        if not base64_authorization_header or \
                type(base64_authorization_header) is not str:
            return None
        try:
            encode_string = base64_authorization_header.encode("utf-8")
            decoded_str = base64.b64decode(encode_string)
            return decoded_str.decode("utf-8")
        except Exception:
            return None
