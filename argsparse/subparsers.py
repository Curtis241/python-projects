import argparse

def my_stop(args):
    if args.gracefully:
        print("Let's try to stop...")
    else:
        print('Stop, now!')

parser = argparse.ArgumentParser(prog='mydaemon')

graceful = argparse.ArgumentParser(add_help=False)
graceful.add_argument('-g', '--gracefully', action='store_true', help='tries to terminate the process gracefully')
sp = parser.add_subparsers()
sp_start = sp.add_parser('start', help='Starts %(prog)s daemon')
sp_stop = sp.add_parser('stop', parents=[graceful],
                    description='Stops the daemon if it is currently running.',
                    help='Stops %(prog)s daemon')
sp_restart = sp.add_parser('restart', parents=[graceful], help='Restarts %(prog)s daemon')

sp_stop.set_defaults(func=my_stop)

args = parser.parse_args()
args.func(args)