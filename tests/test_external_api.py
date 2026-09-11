from unittest.mock import patch

from mypy.types import Any

from src.external_api import amount_transaction


@patch("requests.get")
def test_amount_transaction(mock_get: Any, transaction: dict) -> None:
    mock_get.return_value.json.return_value = {"result": 100.00}
    assert amount_transaction(transaction) == 100.00


@patch("requests.get")
def test_amount_transaction_rus(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = "221.37"
    assert (
        amount_transaction({"operationAmount": {"amount": "221.37", "currency": {"name": "RUS", "code": "RUS"}}})
        == "221.37"
    )
