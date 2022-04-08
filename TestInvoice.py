import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    product = {'Peb': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
               'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

def test_CanFindInvoiceClass():
    invoice = Invoice()

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImprurePrice(products)
    assert invoice.totalImprurePrice(products) == 75