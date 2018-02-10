# Reference: http://dontfragment.com/using-python-yaml-and-jinja2-to-generate-config-files/

import yaml
import os
from jinja2 import Environment, FileSystemLoader


def process_file():
    base_path = os.getcwd()
    source_file_path = "{0}/source.yml".format(base_path)
    source_file_dict = yaml.load(open(source_file_path, 'rb').read())

    env = Environment(loader=FileSystemLoader(base_path), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("template.txt")

    # Render the template with data and print the output
    print(template.render(source_file_dict))

if __name__ == '__main__':
    process_file()