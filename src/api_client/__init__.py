"""A lightweight Python library for making HTTP requests against REST APIs.

It provides a class that constructs URLs relative to a base endpoint, handles query
parameters and returns `requests.Response` objects. Authentication and other
session-level behaviour can be configured at construction time.
"""

from .client import APIClient
from .exceptions import APIError

__all__ = ["APIClient", "APIError"]
