from pdf_parsing.pdf_parsing.extract_pdf import *


def test_tlv_column():
    column = AttributeTlvNameColumn()
    assert column.validate("SerialNumber") is True
    assert column.validate("12345") is False


def test_constraint_column():
    column = ConstraintsColumn()
    assert column.validate("R") is True
    assert column.validate("R/W") is True
    assert column.validate("N/A") is True

def test_tlv_type_column():
    column = TlvTypeColumn()
    assert column.validate("50.1.1") is True
    assert column.validate("50") is True
    assert column.validate("93.4.10.4") is True

def test_field_length_column():
    column = FieldLengthColumn()
    assert column.validate("1") is True
    assert column.validate("variable") is True
    assert column.validate("0-255") is True

