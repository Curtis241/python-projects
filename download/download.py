import wget
import tarfile
import os
import uuid
from urllib.parse import urlparse


class FileMgr:

    def __init__(self, container_url):
        self.container_tmp_dir = "/tmp/container-{}".format(uuid.uuid4())
        self.container_url = container_url
        #https://docs.python.org/2/library/urlparse.html
        parsed_url = urlparse(container_url)
        self.container_tar_file = str(parsed_url.path).rsplit("/",1)[1]
        self.container_tar_path = "{}/{}".format(self.container_tmp_dir, self.container_tar_file)

    def __download(self):
        try:
            # https://bitbucket.org/techtonik/python-wget/src
            print("Downloading container from {} to {}".format(self.container_url, self.container_tmp_dir))
            wget.download(self.container_url, out=self.container_tmp_dir)
        except Exception as ex:
            print("Error occurred downloading file")

    def __create_tmp_dir(self):
        try:
            os.makedirs(self.container_tmp_dir)
        except os.error:
            print("Could not create tmp directory")

    def __extract(self):
        #https://docs.python.org/2/library/tarfile.html
        if tarfile.is_tarfile(self.container_tar_path):
            tar = tarfile.open(self.container_tar_path)
            self.rootfs_dir = "{}/rootfs".format(self.container_tmp_dir)
            print("Extracted {} to {}".format(self.container_tar_file, self.rootfs_dir))
            tar.extractall(path=self.rootfs_dir)
            tar.close()

    def get_file(self):
        self.__create_tmp_dir()
        self.__download()
        self.__extract()

if __name__ == "__main__":
    mgr = FileMgr("http://localhost/files/container.tar.gz")
    mgr.get_file()