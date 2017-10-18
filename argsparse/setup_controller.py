import argparse

parser = argparse.ArgumentParser()

username = argparse.ArgumentParser(add_help=False)
username.add_argument('-u', '--username', help='open stack username', required=True)

password = argparse.ArgumentParser(add_help=False)
password.add_argument('-p', '--password', help='open stack password', required=True)

cluster_name = argparse.ArgumentParser(add_help=False)
cluster_name.add_argument('-c', '--cluster_name', help='open stack cluster name', required=True)

image_name = argparse.ArgumentParser(add_help=False)
image_name.add_argument('-i', '--image_name', help='open stack image name', required=True)

package_url = argparse.ArgumentParser(add_help=False)
package_url.add_argument('-r', '--package_url', help='package url', required=True)

package_name = argparse.ArgumentParser(add_help=False)
package_name.add_argument('-n', '--package_name', help='package name', required=True)

floating_ip = argparse.ArgumentParser(add_help=False)
floating_ip.add_argument('-f', '--floating_ip', help='open stack floating ip for controller master', required=True)

sp = parser.add_subparsers()
deploy_all = sp.add_parser('deploy_all', parents=[username, password, cluster_name, image_name, package_url, package_name], help='deploys stack, containers, services, and data')
deploy_stack = sp.add_parser('deploy_stack', parents=[username, password, cluster_name], help='deploys stack only')
delete_stack = sp.add_parser('delete_stack', parents=[username, password, cluster_name], help='delete existing stack')

args = parser.parse_args()
args.func(args)


#
# import argparse
#
# parser = argparse.ArgumentParser(add_help=False)
# subparsers = parser.add_subparsers(help='sub-behavioral help')
#
# deploy_all = subparsers.add_parser('deploy_all', help='deploys stack, containers, custom services, and default data')
# deploy_all.add_argument('-u','--username', help='open stack username')
# deploy_all.add_argument('-p','--password', help='open stack password')
# deploy_all.add_argument('-c', '--clustername',help='open stack cluster name')
# deploy_all.add_argument('-i', '--imagename',help='open stack image name')
# deploy_all.add_argument('-r', '--packageurl',help='package url')
# deploy_all.add_argument('-n','--packagename',help='package name')
#
# deploy_stack = subparsers.add_parser('deploy_stack', help='deploys stack only')
# deploy_stack.add_argument('-u','--username', help='open stack username')
# deploy_stack.add_argument('-p','--password', help='open stack password')
# deploy_stack.add_argument('-c', '--clustername',help='open stack cluster name')
#
# # parent_parser.add_argument('operation', choices=['deploy_all', 'delete_stack'])
# # parent_parser.add_argument('username')
# # parent_parser.add_argument('password')
# #
# # deploy_all_parser = argparse.ArgumentParser(parents=[parent_parser])
# # deploy_all_parser.add_argument('-c', '--clustername')
# # deploy_all_parser.add_argument('-i', '--imagename')
#
#
# parser.print_help()

