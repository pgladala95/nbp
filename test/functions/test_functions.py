from functions import import_code, import_date
import unittest
import mock

class TestFuncionsNBpy:
    def test_import_code(self):
        with mock.patch('builtins.input', return_value='eur'):
            assert import_code() == 'EUR'
        with mock.patch('builtins.input', return_value='EUR'):
            assert import_code() == 'EUR'
        with mock.patch('builtins.input', return_value='euR'):
            assert import_code() == 'EUR'

    def test_import_date(monkeypatch):
        inputs = iter(['2023', '11', '11'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = import_date('EUR')
        assert result == [0, False]