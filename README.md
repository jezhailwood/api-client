# api-client

A lightweight Python library for making HTTP GET requests against REST APIs. It provides a class that constructs URLs relative to a base endpoint, handles query parameters and returns parsed JSON responses. Authentication and other session-level behaviour can be configured at construction time.

## Installation

Install from GitHub using pip:

```bash
pip install "api-client @ git+https://github.com/jezhailwood/api-client.git"
```

Alternatively, add as a dependency in `pyproject.toml`:

```toml
dependencies = [
    "api-client @ git+https://github.com/jezhailwood/api-client.git",
]
```

## Quickstart

```python
from api_client import APIClient

client = APIClient("https://api.example.com")

# GET https://api.example.com/users/123
user = client.get("users", 123)

# GET https://api.example.com/users/123?profile=full
user = client.get("users", 123, params={"profile": "full"})
```

## API reference

Full documentation is available via Python's built-in help:

```python
from api_client import APIClient
help(APIClient)
```
