from calculator import Calculator

def test_add(calculator: Calculator, hello_str: str):
  assert isinstance(hello_str, str)
  assert hello_str == "hello1"
  assert calculator.add(1, 2) == 3
  assert calculator.add(2, 2) == 4
  
def test_subtract(calculator: Calculator):
  assert calculator.subtract(5, 1) == 4
  assert calculator.subtract(3, 2) == 1
  
def test_multiply(calculator: Calculator):
  assert calculator.multiply(2, 3) == 6
  assert calculator.multiply(1.2, 1.2) == 1.44
  
def test_divide(calculator: Calculator):
  assert calculator.divide(0, 9) == 0
  assert calculator.divide(1, 3) == 1/3