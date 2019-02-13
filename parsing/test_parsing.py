from parsing.system import System


def test_parser():
    configuration_system_json = '{"widgets": [{"title": "System Name","columns": ["Text"],"values": ["Text", "HAL 1000B"]}]}'

    system = System()
    system.deserialize(configuration_system_json)
    result_dict = system.deserialize(configuration_system_json)
    assert type(system.system_name) == str
