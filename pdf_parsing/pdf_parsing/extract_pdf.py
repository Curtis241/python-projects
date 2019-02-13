import tabula
import os
import re
import pathlib
import yaml
import dpath
import csv


class Table:

    def __init__(self, index, page_number, start_tlv, end_tlv):
        self.index = index
        self.start_tlv = start_tlv
        self.end_tlv = end_tlv
        self.page_number = page_number


class Column:

    def __init__(self, name, title):
        self.name = name
        self.title = title


class PdfProperties:

    def __init__(self):
        self.input_dir = "resources"
        self.properties_file = "pdf_properties.yaml"
        self.properties_dict = self.__load()

    def __load(self):
        current_dir = pathlib.Path(__file__).parent
        properties_file = f"{current_dir}/{self.input_dir}/{self.properties_file}"
        with open(properties_file, 'r') as file_stream:
            properties_dict = yaml.load(file_stream)
            return properties_dict

    def get_file_path(self):
        current_dir = pathlib.Path(__file__).parent
        pdf_file_name = dpath.get(self.properties_dict, "file/name")
        return f"{current_dir}/resources/{pdf_file_name}"

    def get_columns(self, column_type=None):
        if column_type is not None:
            columns_list = dpath.get(self.properties_dict, f"file/{column_type}")
            column_object_list = []

            for column_dict in columns_list:
                name = dpath.get(column_dict, "column/name")
                title = dpath.get(column_dict, "column/title")
                column_object_list.append(Column(name, title))

            return column_object_list
        else:
            return []

    def get_export_columns(self):
        return self.get_columns("export_columns")

    def get_import_columns(self):
        return self.get_columns("import_columns")

    def get_tables(self):
        table_list = dpath.get(self.properties_dict, "tables")
        table_object_list = []

        index = 1
        for table_dict in table_list:
            page_number = dpath.get(table_dict, "table/page_number")
            start_tlv = dpath.get(table_dict, "table/start_tlv")
            end_tlv = dpath.get(table_dict, "table/end_tlv")
            table_object_list.append(Table(index, page_number, start_tlv, end_tlv))
            index += 1

        return table_object_list


class RphySpecPdfFile:

    def __init__(self):
        self.properties = PdfProperties()
        self.minimum_length = 3

    def get_path(self):
        return self.properties.get_file_path()

    def get_import_columns(self):
        return self.properties.get_import_columns()

    def get_export_columns(self):
        return self.properties.get_export_columns()

    def validate_tlv_type(self, value):
        # Expected 50, 23.1, 22.2.1, 153.1.2.1
        if str(value).isdigit():
            return True
        else:
            pattern = re.compile("^[0-9]{0,3}.[0-9]{0,2}.[0-9]{0,2}.[0-9]{0,2}")
            result = pattern.fullmatch(value)
            if result is not None:
                return True
        return False

    def validate_tlv_name(self, value):
        if len(value) >= self.minimum_length:
            # ie. VendorName
            pattern = re.compile("^[a-zA-Z]+") 
            result = pattern.fullmatch(value)
            if result is not None:
                return True
        return False

    def get_tables(self):
        return self.properties.get_tables()

    def get_table(self, page_number): 
        for table in self.get_tables():
            if int(table.page_number) == int(page_number):
                return table
        return None


class CsvExporter:

    def __init__(self, pdf):
        self.output_dir = "output"

        assert type(pdf) == RphySpecPdfFile
        self.pdf = pdf

    def __make_output_dir(self):

        try:
            os.mkdir(self.output_dir)
        except Exception as ex:
            print(f"Failed to create output directory. {ex}")

    def export(self):
        self.__make_output_dir()
        for table in self.pdf.get_tables():
            print(table.page_number)
            csv_file_path = self.__get_csv_file_path(table)
            pdf_file_path = self.pdf.get_path()
            tabula.convert_into(pdf_file_path, guess=True, encoding='utf-8',
                               pages=table.page_number, output_path=csv_file_path, output_format="csv")

    def __get_csv_file_path(self, table):
        assert type(table) is Table
        file_name = f"{table.index}_pg{table.page_number}"
        return f"{self.output_dir}/{file_name}.csv"

    def merge(self):

        # with open(csv_file_path, mode='w') as csv_file:
        #     csv_writer = csv.writer(csv_file_path, delimiter=',', quotechar='"')
        #     csv_writer.writerow(table.get_column_titles())

        for table in self.pdf.get_tables():
            start_tlv = table.start_tlv
            end_tlv = table.end_tlv
            csv_input_file_path = self.__get_csv_file_path(table)
            with open(csv_input_file_path, "r") as csv_input_file:
                csv_reader = csv.reader(csv_input_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if row[0] == start_tlv:
                        start_tlv_index = line_count
                    if row[0] == end_tlv:
                        end_tlv_index = line_count
                    line_count += 1

                print(f"start_tlv_index: {start_tlv_index} for {start_tlv}, end_tlv_index: {end_tlv_index} for {end_tlv}")

                line_count = 0
                for row in csv_reader:
                    # if line_count in range(start_tlv_index, end_tlv_index):
                    with open("output.csv", "w") as csv_output_file:
                        csv_writer = csv.writer(csv_output_file, delimiter=',', quotechar='"')
                        csv_writer.writerow(row)
                    line_count += 1



if __name__ == "__main__":
    pdf = RphySpecPdfFile()
    #CsvExporter(pdf).export()
    CsvExporter(pdf).merge()

