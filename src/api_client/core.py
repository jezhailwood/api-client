"""Minimal REST API client.

This module provides `APIClient`, a helper for constructing URLs relative to a base API
endpoint and making HTTP requests using the `requests` library. Responses are returned
as `requests.Response` objects.
"""

from urllib.parse import quote

import requests

from .exceptions import APIError

type QueryParams = dict[str, str | int | float | bool | None]


class APIClient:
    """HTTP client for making requests against a REST API.

    The client constructs request URLs by appending path segments to a configured base
    URL and performs HTTP requests, returning `requests.Response` objects for the caller
    to handle. Each segment is converted to a string, stripped of leading and trailing
    slashes and percent-encoded.

    This client does not currently handle retries. Authentication and custom headers can
    be configured by passing a pre-configured `requests.Session` instance. Network
    errors and non-2xx responses are raised as `APIError`.

    Examples:
        Basic usage:

            client = APIClient("https://api.example.com")
            response = client.get("users", 123, params={"profile": "full"})
            data = response.json()

        Bearer token:

            session = requests.Session()
            session.headers["Authorization"] = "Bearer <token>"
            client = APIClient("https://api.example.com", session=session)

        Header key:

            session = requests.Session()
            session.headers["X-API-Key"] = "<key>"
            client = APIClient("https://api.example.com", session=session)

        Query parameter key:

            session = requests.Session()
            session.params = {"api_key": "<key>"}
            client = APIClient("https://api.example.com", session=session)

        OAuth 2.0 with automatic token refresh (requires `authlib`):

            from authlib.integrations.requests_client import OAuth2Session
            session = OAuth2Session("<client_id>", "<client_secret>")
            session.fetch_token("https://api.example.com/oauth/token")
            client = APIClient("https://api.example.com", session=session)
    """

    def __init__(
        self,
        base_url: str,
        *,
        timeout: float = 10.0,
        session: requests.Session | None = None,
    ) -> None:
        """Initialise the client with a base API URL.

        The base URL is normalised to always end with exactly one trailing slash to
        ensure consistent URL joining.

        Args:
            base_url: Root URL of the API, eg `"https://api.example.com"`.
            timeout: Default timeout in seconds applied to requests, unless overridden
                per call.
            session: Optional pre-configured `requests.Session` instance. If not
                provided, a plain session is created. Pass a custom session to inject
                authentication or other session-level behaviour. See the class-level
                examples for common patterns.
        """
        self.base_url = base_url.strip().rstrip("/") + "/"
        self.timeout = timeout
        self._session = session if session is not None else requests.Session()

    def _request(
        self,
        method: str,
        *path_segments: str | int,
        params: QueryParams | None = None,
        timeout: float | None = None,
    ) -> requests.Response:
        """Build the URL, send the request and re-raise errors as `APIError`."""
        path = "/".join(quote(str(p).strip("/"), safe="") for p in path_segments)
        url = self.base_url + path
        effective_timeout = self.timeout if timeout is None else timeout
        try:
            response = self._session.request(
                method, url, params=params, timeout=effective_timeout
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise APIError(str(e)) from e

    def get(
        self,
        *path_segments: str | int,
        params: QueryParams | None = None,
        timeout: float | None = None,
    ) -> requests.Response:
        """Make a GET request and return the response.

        Args:
            *path_segments: Path segments to append to the base URL,
                eg `("users", 123)` -> `.../users/123`.
            params: Optional query string parameters.
            timeout: Optional timeout override in seconds. If not provided, the client
                default is used.

        Returns:
            A `requests.Response` object.

        Raises:
            APIError: If a network or HTTP error occurs.
        """
        return self._request("GET", *path_segments, params=params, timeout=timeout)
