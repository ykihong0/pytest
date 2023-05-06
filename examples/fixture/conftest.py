import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
  calculator = Calculator()
  return calculator

@pytest.fixture
def hello_str():
  return "hello"