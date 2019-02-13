from pdf_parsing.pdf_parsing.extract_pdf import RphySpecPdfFile


def test_tlv_column():
    pdf_file = RphySpecPdfFile()
    assert pdf_file.validate_tlv_name("SerialNumber") is True
    assert pdf_file.validate_tlv_name("12345") is False


def test_tlv_type_column():
    pdf_file = RphySpecPdfFile()
    assert pdf_file.validate_tlv_type("50.1.1") is True
    assert pdf_file.validate_tlv_type("50") is True
    assert pdf_file.validate_tlv_type("93.4.10.4") is True

