import pytest
from src.order_io import load_order, write_receipt

def test_full_order_processing(tmp_path):
    input_file = tmp_path / "order.csv"
    output_file = tmp_path / "receipt.txt"

    csv_content = (
        "Widget A, $10.00\n"
        "Gizmo B, 5.50\n"
    )
    input_file.write_text(csv_content, encoding="utf-8")

    items = load_order(input_file)

    # 10% discount and 10% tax for the test case
    write_receipt(output_file, items, discount_percent=10, tax_rate=0.10)

    output_text = output_file.read_text(encoding="utf-8")

    assert "Widget A: $10.00" in output_text
    assert "Gizmo B: $5.50" in output_text
    # Expected total is $15.35 (15.50 subtotal - 10% discount + 10% tax)
    assert "TOTAL: $15.35" in output_text
