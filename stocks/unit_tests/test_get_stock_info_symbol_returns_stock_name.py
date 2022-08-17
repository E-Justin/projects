def test_get_stock_info_correct_name_from_stock_symbol_DIS():
    assert 'Disney' in get_stock_info('DIS')

def test_get_stock_info_correct_name_from_stock_symbol_AAPL():
    assert 'Apple' in get_stock_info('AAPL')

def test_get_stock_info_correct_name_from_stock_symbol_AAPL():
    assert 'NVIDIA' in get_stock_info('NVDA')

def test_get_stock_info_correct_name_from_stock_symbol_MSFT():
    assert 'Microsoft' in get_stock_info('MSFT')

def test_get_stock_info_correct_name_from_stock_symbol_F():
    assert 'Ford' in get_stock_info('F')

def test_get_stock_info_correct_name_from_stock_symbol_LEVI():
    assert 'Levi' in get_stock_info('LEVI')
