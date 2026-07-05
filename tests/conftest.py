"""Test configuration for Documentation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "documentation-agent", "category": "Software Engineering"}
