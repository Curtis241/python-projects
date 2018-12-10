from tabulate import tabulate

scenarios = [{"id": 1, "name": "default scenario 1", "description": "Description for scenario 1", "source": "default"},
              {"id": 2, "name": "default scenario 2", "description": "Description for scenario 2", "source": "default"},
              {"id": 3, "name": "default scenario 3", "description": "Description for scenario 3", "source": "default"},
              {"id": 4, "name": "user defined scenario 1", "description": "Description for scenario 4", "source": "user_defined", "file_name": "default_scenario_name_1.py"}]


default_scenario_headers = ["id", "name", "description"]
default_scenario_table_data = []

user_defined_headers = ["id", "name", "description", "file_name"]
user_defined_table_data = []

for scenario in scenarios:
    if scenario["source"] == "default":
        default_scenario_table_data.append([scenario["id"], scenario["name"], scenario["description"]])
    if scenario["source"] == "user_defined":
        user_defined_table_data.append([scenario["id"], scenario["name"], scenario["description"], scenario["file_name"]])


print(tabulate(default_scenario_table_data, headers=default_scenario_headers, tablefmt="fancy_grid"))

print(tabulate(user_defined_table_data, headers=user_defined_headers, tablefmt="fancy_grid"))