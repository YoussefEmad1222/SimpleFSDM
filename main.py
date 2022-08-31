from ParseInput import parse_args
import os
import sys
from command_factory import CommandFactory

sys.path.append(os.path.join(os.getcwd(), "commands"))

if __name__ == "__main__":
    args = parse_args()
    CommandFactory().create(args)
