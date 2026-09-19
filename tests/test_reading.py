import pandas as pd

from unittest.mock import patch

from src.reading import reading_csv, reading_excel


@patch('csv.DictReader')
def test_reading_csv(mock_csv_reader):
    mock_csv_reader.return_value = [{'id': 12346578, 'state': 'EXECUTED'}]
    assert reading_csv('data/transactions.csv') == [{'id': 12346578, 'state': 'EXECUTED'}]
    mock_csv_reader.call_once([{'id': 12346578, 'state': 'EXECUTED'}])


@patch('pandas.read_excel')
def test_reading_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([{'id': 12346578, 'state': 'EXECUTED'}])
    assert reading_excel('data/transactions_excel.xlsx') == [{'id': 12346578, 'state': 'EXECUTED'}]
    mock_read_excel.call_once([{'id': 12346578, 'state': 'EXECUTED'}])
