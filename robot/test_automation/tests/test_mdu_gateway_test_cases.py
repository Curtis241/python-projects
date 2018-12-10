from test_automation.test_suites.test_cases.MduGatewayTestCases import MduGatewayTestCases


def test_check_system_name():
    assert MduGatewayTestCases().check_system_name() is True
