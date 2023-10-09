import pytest

from app import app

def test_secret_key():
    assert app.config["SECRET_KEY"] = "my_secret_key"