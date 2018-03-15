import urllib.parse
import os


class UrlParser(object):

    def __init__(self, url, prefix=None):
        self.url = urllib.parse.urlparse(url)
        self.prefix = prefix

    def get_version(self):
        ext = self.get_ext()
        base_name = self.get_basename()
        return base_name.rstrip(ext).lstrip(self.prefix)

    def get_ext(self):

        def extract_ext(path):
            return os.path.splitext(path)[1]

        ext = extract_ext(self.url.path)

        if self.url.path.count(".") == 2:
            path = str(self.url.path).rstrip(ext)
            ext1 = extract_ext(path)
            return "{}{}".format(ext1, ext)
        else:
            return ext

    def get_basename(self):
        return os.path.basename(self.url.path)




url_string = 'http://192.168.220.115/tftpboot/52_Dorado/releases/ENTRA_RELEASE_1_1_1.bin'

parser = UrlParser(url_string, "ENTRA_RELEASE_")
print("Basename: {}".format(parser.get_basename()))
print("Ext: {}".format(parser.get_ext()))
print("Version: {}".format(parser.get_version()))










