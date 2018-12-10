import dpath
from test_automation.core.util import Util
from test_automation.core.web_service.web_service_client import WebServiceClient


class InvalidIpAddress(Exception): pass


class MduGatewayAdapter:

    def __init__(self, ip_address=None):
        self.ip_address = ip_address

        if self.ip_address is not None:
            if Util().ping(ip_address):
                self.url = "http://{}:5000/".format(ip_address)
            else:
                raise ConnectionError("Unable to ping {}".format(ip_address))
        else:
            raise InvalidIpAddress("Provided ip address {} is invalid".format(ip_address))

    def get_system_name(self):
        if self.url is not None:
            client = WebServiceClient(self.url)
            response_dict = client.get()
            return dpath.get(response_dict, "/gateway/name")

