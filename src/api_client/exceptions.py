"""Exceptions raised by the API client.

Every error raised by the client derives from `APIError`, so a caller can catch that
single base to handle any failure. Beneath it sit two subclasses that mirror where a
request can fail: `RequestError`, when no usable response is obtained, and
`HTTPStatusError`, when a response comes back with a 4xx or 5xx status.
"""

import requests


class APIError(Exception):
    """Base class for all errors raised by the client.

    Catch this to handle any client error. It is not raised directly; every failure
    surfaces as one of its subclasses, `RequestError` or `HTTPStatusError`.
    """


class RequestError(APIError):
    """Raised when a request does not produce a usable response.

    Nothing comes back to inspect: the connection cannot be made, the request times out,
    or the server redirects in a loop, among others. It covers every request-side
    failure except a 4xx or 5xx status code, which raises `HTTPStatusError` instead. The
    underlying `requests` exception is available via `__cause__`.
    """


class HTTPStatusError(APIError):
    """Raised when the server returns a 4xx or 5xx status code.

    The request reaches the server and a response comes back; only its status code
    indicates failure. The response is always available via the `response` attribute, so
    callers can inspect the status code, headers or body.

    Attributes:
        response: The `requests.Response` carrying the error status.

    Example:
        try:
            response = client.get("users", 123)
        except HTTPStatusError as e:
            print(e.response.status_code)
    """

    def __init__(self, message: str, *, response: requests.Response) -> None:
        """Initialise the error with a message and the originating response.

        Args:
            message: Human-readable description of the failure.
            response: The `requests.Response` carrying the error status.
        """
        super().__init__(message)
        self.response = response
