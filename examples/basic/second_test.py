class TestClass:
  def test_a(self):
    x = "Hello, hi"
    assert "h" in x
    
  def test_b(self):
    x = "what"
    assert hasattr(x, "who")
    
  def test_c(self):
    a = 1
    assert a == 2