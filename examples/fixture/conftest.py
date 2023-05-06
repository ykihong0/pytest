import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
  calculator = Calculator()
  return calculator

@pytest.fixture
def hello_str():
  return "hello"

@pytest.fixture
def order():
  return []

@pytest.fixture
def top(order, innermost):
  order.append("top")