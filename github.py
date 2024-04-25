#!/usr/bin/python3

import sys

def main(name):
    print("This is {} github script". format(name))


name = "Stephen's"
if len(sys.argv) > 1:
	name = sys.argv[1]
main("Stephen's")
