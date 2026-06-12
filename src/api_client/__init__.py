"""A lightweight Python library for making HTTP requests against REST APIs.

It provides a class that constructs URLs relative to a base endpoint, supports the
common HTTP methods (GET, POST, PUT, PATCH and DELETE) with JSON request bodies and
query parameters, and returns `requests.Response` objects. Authentication and other
session-level behaviour can be configured at construction time.
"""

from .client import APIClient
from .exceptions import APIError, HTTPStatusError, RequestError

__all__ = ["APIClient", "APIError", "HTTPStatusError", "RequestError"]
