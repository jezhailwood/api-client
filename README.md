# api-client

A lightweight Python library for making HTTP requests against REST APIs. It provides a class that constructs URLs relative to a base endpoint, supports the common HTTP methods (GET, POST, PUT, PATCH and DELETE) with JSON request bodies and query parameters, and returns `requests.Response` objects. Authentication and other session-level behaviour can be configured at construction time.

## Installation

Install from GitHub using pip:

```shell
pip install "api-client @ git+https://github.com/jezhailwood/api-client.git@v0.6.0"
```

Alternatively, add as a dependency in `pyproject.toml`:

```toml
dependencies = [
    "api-client @ git+https://github.com/jezhailwood/api-client.git@v0.6.0",
]
```

Replace `v0.6.0` with the [latest release tag](https://github.com/jezhailwood/api-client/tags).

## Quickstart

```python
from api_client import APIClient

client = APIClient("https://api.example.com")

# GET https://api.example.com/users
response = client.get("users")
users = response.json()

# GET https://api.example.com/users/123?profile=full
response = client.get("users", 123, params={"profile": "full"})
user = response.json()

# POST https://api.example.com/users
response = client.post("users", json={"name": "Ada"})
created = response.json()

# PUT https://api.example.com/users/123
client.put("users", 123, json={"name": "Ada", "email": "ada@example.com"})

# PATCH https://api.example.com/users/123
client.patch("users", 123, json={"email": "new@example.com"})

# DELETE https://api.example.com/users/123
client.delete("users", 123)
```

## Error handling

When a request fails, the client raises one of two exceptions, both subclasses of `APIError`:

- `RequestError` — the request never produced a usable response (the connection failed, the request timed out, the server redirected in a loop, and so on).
- `HTTPStatusError` — the server responded, but with a 4xx or 5xx status code. The response is attached as `.response`, so you can inspect the status code, headers and body.

```python
from api_client import APIClient, HTTPStatusError, RequestError

client = APIClient("https://api.example.com")

try:
    response = client.get("users", 123)
except RequestError as e:
    print(f"Could not reach the API: {e}")
except HTTPStatusError as e:
    print(f"Request failed with {e.response.status_code}: {e.response.text}")
```

If you don't need to tell the two apart, catch `APIError` to handle either:

```python
from api_client import APIError

try:
    response = client.get("users", 123)
except APIError as e:
    print(f"Request to the API failed: {e}")
```

## API reference

Full documentation is available at [jezhailwood.github.io/api-client](https://jezhailwood.github.io/api-client).

## Licence

Released under the [MIT Licence](LICENSE).
