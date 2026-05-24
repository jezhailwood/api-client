# api-client

A lightweight Python library for making HTTP GET requests against REST APIs. It provides a class that constructs URLs relative to a base endpoint, handles query parameters and returns `requests.Response` objects. Authentication and other session-level behaviour can be configured at construction time.

## Installation

Install from GitHub using pip:

```shell
pip install "api-client @ git+https://github.com/jezhailwood/api-client.git@v0.2.0"
```

Alternatively, add as a dependency in `pyproject.toml`:

```toml
dependencies = [
    "api-client @ git+https://github.com/jezhailwood/api-client.git@v0.2.0",
]
```

Replace `v0.2.0` with the [latest release tag](https://github.com/jezhailwood/api-client/tags).

## Quickstart

```python
from api_client import APIClient

client = APIClient("https://api.example.com")

# GET https://api.example.com/users/123
response = client.get("users", 123)
user = response.json()

# GET https://api.example.com/users/123?profile=full
response = client.get("users", 123, params={"profile": "full"})
user = response.json()
```

## API reference

Full documentation is available at [jezhailwood.github.io/api-client](https://jezhailwood.github.io/api-client).

## Licence

Released under the [MIT Licence](LICENSE).
