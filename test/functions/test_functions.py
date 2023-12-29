from functions import import_code, import_date
import unitest
import mock


class TestFuncionsNBpy:
    def test_import_code(self):
        with mock.patch('builtins.input', return_value='eur'):
            assert import_code() == 'EUR'
        with mock.patch('builtins.input', return_value='EUR'):
            assert import_code() == 'EUR'
        with mock.patch('builtins.input', return_value='euR'):
            assert import_code() == 'EUR'
        print("test 1 works")

def test_import_date(monkeypatch): #for some reason test didn't work inside class- monkeypatch function are not defined(?)
    inputs = ['2023', '11', '11']
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    result = import_date('EUR')
    assert result == [0, False]
    print("test 2 works")