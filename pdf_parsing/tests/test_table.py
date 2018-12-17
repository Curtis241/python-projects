from pdf_parsing.pdf_parsing.extract_pdf import TlvTable


def test_table_value_detection():
    table = TlvTable(1, "empty", "empty")
    value_dict = table.get_value_dict("VendorSpecific")
    assert value_dict["column_name"] == "tlv_name"


def test_get_titles():
    table = TlvTable(1, "empty", "empty")
    column_list = table.get_column_titles()
    assert len(column_list) == 6

