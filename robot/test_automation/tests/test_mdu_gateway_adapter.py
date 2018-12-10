import pytest
from test_automation.adapter.mdu_gateway_adapter import MduGatewayAdapter


def test_get_system_name():
    system_name = MduGatewayAdapter("localhost").get_system_name()
    assert type(system_name) == str



