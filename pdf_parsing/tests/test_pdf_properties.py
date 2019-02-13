from pdf_parsing.pdf_parsing.extract_pdf import PdfProperties


class TestPdfProperties:

    def test_get_file_path(self):
        file_path = PdfProperties().get_file_path()
        assert type(file_path) == str
        assert len(file_path) > 0

    def test_get_tables(self):
        tables = PdfProperties().get_tables()
        assert type(tables) == list
        assert len(tables) == 26

    def test_get_import_columns(self):
        import_columns = PdfProperties().get_import_columns()
        assert type(import_columns) == list

    def test_get_export_columns(self):
        export_columns = PdfProperties().get_export_columns()
        assert type(export_columns) == list



