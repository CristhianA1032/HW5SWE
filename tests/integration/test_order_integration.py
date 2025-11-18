import pytest
from src.pricing import (
    parse_price,
    format_currency,
    apply_discount,
    add_tax,
    bulk_total,
)

parse_price_valid_cases = [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    (" $0.99 ", 0.99),
    ("1000", 1000.00),
]

@pytest.mark.parametrize("price_str, expected", parse_price_valid_cases)
def test_parse_price_valid(price_str, expected):
    assert parse_price(price_str) == expected

parse_price_invalid_cases = [
    "",
    "abc",
    "$12,34,56",
]

@pytest.mark.parametrize("price_str", parse_price_invalid_cases)
def test_parse_price_invalid_raises_error(price_str):
    with pytest.raises(ValueError):
        parse_price(price_str)

format_currency_cases = [
    (12.5, "$12.50"),
    (1234.567, "$1234.57"),
    (100, "$100.00"),
    (0.999, "$1.00"),
]

@pytest.mark.parametrize("value, expected", format_currency_cases)
def test_format_currency(value, expected):
    assert format_currency(value) == expected

def test_apply_discount_zero_percent():
    assert apply_discount(100.0, 0) == 100.0

def test_apply_discount_standard_case_buggy():
    assert apply_discount(100.0, 10) != 90.0
    
def test_apply_discount_negative_raises_error():
    with pytest.raises(ValueError):
        apply_discount(100.0, -1)

def test_add_tax_default_rate():
    assert add_tax(100.0) == pytest.approx(107.0)

def test_add_tax_custom_rate():
    assert add_tax(50.0, rate=0.10) == pytest.approx(55.0)

def test_add_tax_negative_rate_raises_error():
    with pytest.raises(ValueError):
        add_tax(100.0, rate=-0.01)

def test_bulk_total_simple_no_discount():
    prices = [10.0, 20.0, 5.0]
    assert bulk_total(prices) == pytest.approx(37.45)
