# tests/regression/test_apply_discount_bug.py
from src.pricing import apply_discount

def test_apply_discount_regression():
   
    result = apply_discount(100.0, 10)
    # Expected correct result is 90.0
    assert result == 90.0
