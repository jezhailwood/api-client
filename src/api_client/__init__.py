"""A lightweight Python library for making HTTP GET requests against REST APIs.

It provides a class that constructs URLs relative to a base endpoint, handles query
parameters and returns parsed JSON responses. Authentication and other session-level
behaviour can be configured at construction time.

See `api_client.core` for full usage details.
"""

from .core import APIClient
