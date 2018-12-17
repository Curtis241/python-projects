import PyPDF2
import os
import re
import pathlib


class TlvTables:

    def __init__(self):
        self.table_list = [
            TlvTable(1, 158, 'RpdCapabilities', 'SerialNumber'),
            TlvTable(2, 159, 'UsBurstReceiverVendorId', 'DeviceLocation'),
            TlvTable(3, 160, 'DeviceLocationDescription', 'SupportsPspNdfPw'),
            TlvTable(4, 161, 'SupportsPspNdrPw', 'SupportedTrigChanTypes'),
            TlvTable(5, 162, 'PwType', 'MinScanningRepeatPeriod'),
            TlvTable(6, 162, 'EvCfg', 'CoreName'),
            TlvTable(7, 163, 'VendorId', 'PowerAdjust'),
            TlvTable(8, 164, 'DsOfdmChannelConfig', 'PreambleOffsett'),
            TlvTable(9, 165, 'PreambleModType', 'Guardband'),
            TlvTable(10, 166, 'UsOfdmaFineRangingIuc', 'ResponseScQamScramblerSeed'),
            TlvTable(11, 167, 'ResponseScQamGuardTime', 'StaticPwStatus'),
            TlvTable(12, 168, 'CommonStaticPwStatus', 'L2TPv3'),
            TlvTable(13, 168, 'DsRfPortPerf', 'outPackets'),
            TlvTable(14, 169, 'discontinuityTime', 'UsIuc'),
            TlvTable(15, 170, 'ScheduledGrants', 'IllegalMaps'),
            TlvTable(16, 171, 'DiscardedRequests', 'operStatusNdr'),
            TlvTable(17, 171, 'RpdCtrl', 'ScCfgTrigMinislotCount'),
            TlvTable(18, 172, 'ScCfgTrigSid', 'SwImageIndex'),
            TlvTable(19, 172, 'DsOob55d1', 'SfAdminState'),
            TlvTable(20, 173, 'SfRfMute', 'TargetRxPowerAdjust'),
            TlvTable(21, 173, 'Oob55d2Config', 'RfMute'),
            TlvTable(22, 174, 'RdtiConfig', 'RpdPtpPortClockSelectAlternateSourceFirst'),
            TlvTable(23, 175, 'RpdPtpPortTransportType', 'RpdPtpPortClockAltSrcGw'),
            TlvTable(24, 175, 'RpdInfo', 'PendingOrLocalLog'),
            TlvTable(25, 176, 'EvFirstTime', 'DsRfPortStart'),
            TlvTable(26, 177, 'DsRfPortEnd', 'ResourceAllocationCheck')
        ]

    def get_table(self, page_number): 
        for table in self.table_list:
            if int(table.page_number) == int(page_number):
                return table
        return None


class TlvTable:

    def __init__(self, index, page_number, start_tlv, end_tlv):
        self.index = index
        self.start_tlv = start_tlv
        self.end_tlv = end_tlv
        self.page_number = page_number
        self.columns = [
            ObjectTypeColumn(),
            ConstraintsColumn(),
            TlvTypeColumn(),
            FieldLengthColumn(),
            AttributeTlvNameColumn(),
            CommentsColumn()
        ]

    def validate(self, value):

        for column in self.columns:
            if column.validate(value):
                column_name = column.get_column_name()
                print(f"Validation ok on value {value} for {column_name}")
                return column

    def get_value_dict(self, value):
        column = self.validate(value)
        return column.to_dict(value)
       
    def get_column_titles(self):
        column_titles = []
        for column in self.columns:
            column_titles.append(column.get_column_title())
        return column_titles

class Column:

    def __init__(self, column_name):
        self.column_name = column_name

    def validate(self, value): pass

    def to_dict(self, value):
        return {"column_name": self.column_name, "value": value}

    def get_column_name(self):
        return self.column_name

    def get_column_title(self): pass

class AttributeTlvNameColumn(Column):

    def __init__(self):
        super(AttributeTlvNameColumn, self).__init__("tlv_name")
        self.minimum_length = 4

    def validate(self, value):

        if len(value) >= self.minimum_length:
            # ie. VendorName
            pattern = re.compile("^[a-zA-Z]+") 
            result = pattern.fullmatch(value)
            if result is not None:
                return True
        return False

    def get_column_title(self):
        return "Attribute/TLV Name"


class ObjectTypeColumn(Column):

    def __init__(self):
        super(ObjectTypeColumn, self).__init__("object_type")
        self.object_types =  ["Complex TLV",
                              "UnsignedShort",
                              "Boolean",
                              "UnsignedByte",
                              "String",
                              "MacAddress"]

    def validate(self, value):
        return value in self.object_types

    def get_column_title(self):
        return "Object Type"


class ConstraintsColumn(Column):

    def __init__(self):
        super(ConstraintsColumn, self).__init__("constraints")
        self.contstraint_types = ["R","R/W","N/A"]

    def validate(self, value):
        return value in self.contstraint_types

    def get_column_title(self):
        return "Constraints"


class TlvTypeColumn(Column):

    def __init__(self):
        super(TlvTypeColumn, self).__init__("tlv_type")
        self.min = int(9)
        self.max = int(154)
        
    def validate(self, value):
        # Expected 50, 23.1, 22.2.1, 153.1.2.1

        if str(value).isdigit() and int(value) in range(self.min, self.max):
            return True
        else:
            pattern = re.compile("^[0-9]{0,3}.[0-9]{0,2}.[0-9]{0,2}.[0-9]{0,2}")
            result = pattern.fullmatch(value)
            if result is not None:
                return True
        return False

    def get_column_title(self):
        return "TLV Type"


class FieldLengthColumn(Column):

    def __init__(self):
        super(FieldLengthColumn, self).__init__("field_length")
        self.field_lengths = ["variable","1","2","0-255","6","3-16","5-16","3-32","5-32","0-32","0-16","8|11","4|16"]

    def validate(self, value):
        return str(value) in self.field_lengths

    def get_column_title(self):
        return "TLV Value Field Length"


class CommentsColumn(Column):
    
    def __init__(self):
        super(CommentsColumn, self).__init__("comments")

    def validate(self, value):
        return True

    def get_column_title(self):
        return "Comments"


class FileExporter:

    def __init__(self, table):

        assert type(table) is TlvTable

        current_dir = pathlib.Path(__file__).parent
        self.output_dir = "output"
        self.file_name = f"{table.index}_pg{table.page_number}"

    def __make_output_dir(self):

        try:
            os.mkdirs(self.output_dir, exist_ok=True)
        except Exception as ex:
            print("Failed to create output directory")

    def export_list(self, file_content):
 
        assert type(file_content) is list

        self.__make_output_dir()
        txt_file_name = f"{self.file_name}.txt"
        txt_file_path = f"{self.output_dir}/{txt_file_name}"
        os.system(f"cd {self.output_dir}; touch {txt_file_name}")
        print(f"Created file {txt_file_path}")
        with open(txt_file_path, mode='w+') as txt_file:
            txt_file.write(file_content)

    def export_csv(self, table, file_content): 
        
        assert type(table) is TlvTable
        assert type(file_content) is list
        assert type(file_content[0]) is list
        
        self.__make_output_dir()
        csv_file_path = f"{self.output_dir}/{self.file_name}.csv"
        with open(csv_file_path, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file_path, delimiter=',', quotechar='"')
            csv_writer.writerow(table.get_column_titles())


class RphySpecPdf:

    def __init__(self):
        current_dir = pathlib.Path(__file__).parent
        self.pdf_file_path = f"{current_dir}/CM-SP-R-PHY-I10-180509.pdf"

    def get_page(self, page_number):

        assert type(page_number) == int

        pdfFileObj = open(self.pdf_file_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        try:
            return pdfReader.getPage(page_number)
        except Exception as ex:
            print(ex.message)

    def __clean_text(self, extracted_text):

        assert type(extracted_text) is str

        # Split the raw text into a list
        text_list = str(extracted_text).splitlines()
        # Remove empty list items and convert back to list
        text_list = list(filter(None, text_list))
        clean_list = []
        for value in text_list:
            # Strip off the empty spaces from each end.
            value = str(value).strip()
            # If there still are spaces then it needs to be parsed.
            if value != "Complex TLV" and str(value).count(" ") > 0:
                # Strip off the empty spaces again.
                value = str(value).strip()
                # Split the string into a list.
                values_list = str(value).split(" ")
                # Remove the empty items from the list.
                values_list = list(filter(None, values_list))
                print(f"Splitting {value} into {values_list}")
                # Add the values to the list.
                for value in values_list:
                    clean_list.append(value)
            else:
                print(f"Adding {value}")
                clean_list.append(value)

        return clean_list
        
    def parse_text(self, table):

        assert type(table) is TlvTable

        page = self.get_page(table.page_number)
        clean_list = self.__clean_text(page.extractText())
        
        assert type(clean_list) is list

        start_index = clean_list.index(table.start_tlv)
        print(f"Start index for {table.start_tlv} is {start_index}")
        end_index = clean_list.index(table.end_tlv)
        print(f"End index for {table.end_tlv} is {end_index}")

        filtered_list = []
        current_index = 0
        for value in clean_list:
            if current_index >= start_index:
                filtered_list.append(value)
            current_index += 1

        return filtered_list
 
    def to_dict(self, content_list): pass

if __name__ == "__main__":
    for table in TlvTables().table_list:
        text_list = RphySpecPdf().parse_text(table)
        FileExporter(table).export_list(text_list)
