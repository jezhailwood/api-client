# api-client

A lightweight Python library for making HTTP requests against REST APIs. It provides a class that constructs URLs relative to a base endpoint, supports the common HTTP methods (GET, POST, PUT, PATCH and DELETE) with JSON request bodies and query parameters, and returns `requests.Response` objects. Authentication and other session-level behaviour can be configured at construction time.

## Installation

Install from GitHub using pip:

```shell
pip install "api-client @ git+https://github.com/jezhailwood/api-client.git@v0.5.0"
```

Alternatively, add as a dependency in `pyproject.toml`:

```toml
dependencies = [
    "api-client @ git+https://github.com/jezhailwood/api-client.git@v0.5.0",
]
```

Replace `v0.5.0` with the [latest release tag](https://github.com/jezhailwood/api-client/tags).

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

## API reference

Full documentation is available at [jezhailwood.github.io/api-client](https://jezhailwood.github.io/api-client).

## Licence

Released under the [MIT Licence](LICENSE).
