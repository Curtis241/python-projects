from test_automation.adapter.mdu_gateway_adapter import MduGatewayAdapter


class MduGatewayTestCases:

    def __init__(self, ip_address):
        self.adapter = MduGatewayAdapter(ip_address)

    def check_system_name(self):
        if len(self.adapter.get_system_name()) > 0:
            return True
        return False
