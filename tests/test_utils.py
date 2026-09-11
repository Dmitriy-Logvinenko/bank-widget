import json
from unittest.mock import Mock, patch

from mypy.types import Any

from src.utils import financial_transaction_data


@patch("json.load")
def test_financial_transaction_data(mock_get: Any) -> None:
    mock_get.return_value = []
    assert financial_transaction_data("filename.json") == []


def test_financial_transaction_data_with_mock() -> None:
    mock_value = Mock(return_value=[])
    json.load = mock_value
    assert financial_transaction_data("filename.json") == []
