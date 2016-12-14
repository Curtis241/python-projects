import subprocess

def is_up(ip):
    return subprocess.call(["ping","-c1","-w120",ip]) == 0

is_up("ec2-52-43-40-36.us-west-2.compute.amazonaws.com")

