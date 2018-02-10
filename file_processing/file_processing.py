import os
import sys
import requests
import shutil
import yaml


class FileProcessor(object):

    def __init__(self):
        self.output_dir = "output"
        self.input_yaml_file = "calgary_weather.yaml"
        self.merged_yaml_file = "merged_yaml_file.yaml"

    @staticmethod
    def __get_current_weather():

        print("Retrieving current weather for Calgary")
        json_data = requests.get("http://api.wunderground.com/api/3ebc563b3a21f044/conditions/q/AB/Calgary.json")

        return json_data.json()

    def __export_to_yaml(self, json_data):

        with open(self.input_yaml_file, 'w') as out_file:
            file_content = yaml.dump(json_data, default_flow_style=False)
            out_file.write(file_content)

        print("Exporting to {}".format(self.input_yaml_file))

    def __create_copies(self):

        if not os.path.exists(self.output_dir):
            print("Created {} directory".format(self.output_dir))
            os.makedirs(self.output_dir)

        for index in range(1, 101):
            shutil.copyfile(self.input_yaml_file, "{}/response{}.yaml".format(self.output_dir, index))
        print("Created 100 copies of {} in {}".format(self.input_yaml_file, self.output_dir))

        print("Removing {}".format(self.input_yaml_file))
        os.remove(self.input_yaml_file)

    def __parse_copied_files(self):
        responses_list = list()
        responses_dict = {"responses": []}

        print("Extracting response from files")
        for file in [f for f in os.listdir(self.output_dir) if f.endswith('.yaml')]:
            in_file_path = "{}/{}".format(self.output_dir, file)
            with open(in_file_path, 'r') as in_file:
                file_content = yaml.load(in_file)
                responses_list.append(file_content)

        responses_dict["responses"] = responses_list
        print("Removing copied files")
        shutil.rmtree(self.output_dir)

        return responses_dict

    def __create_merged_file(self, responses_dict):

        print("Creating {}".format(self.merged_yaml_file))
        with open(self.merged_yaml_file, 'w') as out_file:
            file_content = yaml.dump(responses_dict, default_flow_style=False)
            out_file.write(file_content)

    def process(self):
        json_data = self.__get_current_weather()
        self.__export_to_yaml(json_data)
        self.__create_copies()
        responses_dict = self.__parse_copied_files()
        self.__create_merged_file(responses_dict)


def main(args):
    FileProcessor().process()
    

if __name__ == "__main__":
    main(sys.argv[0])