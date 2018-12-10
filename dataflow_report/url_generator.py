import sys
import argparse
from argparse import RawDescriptionHelpFormatter
import json
import flatdict
import re

def get_json_file_contents(args):
    if args.file_path is not "None":
        json_file = open(args.file_path).read()
        return json.loads(json_file)

def make_urls_list(args):
        count = 0
        for i in flatdict.FlatDict(get_json_file_contents(args), delimiter='/'):
            print(i)
            count += 1
        print(count)

def append_unique_list(url, unique_url_list):

    if url not in unique_url_list:
        unique_url_list.append(url)

    return unique_url_list

def make_unique_urls_list(args):
    unique_url_list = list()
    if args.file_path is not "None":
        for raw_url in flatdict.FlatDict(get_json_file_contents(args), delimiter='/'):
            url_parts = str(raw_url).split("/")

            for url_part in url_parts:
                if str(url_part).isdigit():
                    index = url_parts.index(url_part)
                    url_parts.pop(index)
            url = list()
            for url_part in url_parts:
                url.append(url_part)

            append_unique_list(url, unique_url_list)
        #    num_test = re.search('[0-9][0-9]',url)
        #    if num_test:
        #        remove_string = "{}/".format(num_test.group(0))
        #        url = str(url).replace(remove_string,"")
        #        append_unique_list(url, unique_url_list)
        #    else:
        #        append_unique_list(url, unique_url_list)
        #
        for i in unique_url_list:
            print(i)

        print(len(unique_url_list))

def parse_input_parameters():
    parser = argparse.ArgumentParser(description="""
              Parse json file and create a csv file.
              """, formatter_class=RawDescriptionHelpFormatter)

    file_path_p = argparse.ArgumentParser(add_help=False)
    file_path_p.add_argument('--file_path', '-f', metavar='<file_path>',
                                     help="Set the file path.",
                                     required=True)

    sp = parser.add_subparsers()
    sp.add_parser('full_list', parents=[file_path_p],
                  help='Make list of urls using provided json file ')

    return parser


def main(argv):
    parser = parse_input_parameters()
    args = parser.parse_args()
    make_unique_urls_list(args)



if __name__ == "__main__":
    main(sys.argv[1:])