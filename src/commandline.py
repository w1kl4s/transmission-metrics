import argparse
import src 

parser = argparse.ArgumentParser(description="Run transmission metrics daemon/exporter")
parser.add_argument("-m", "--mode", metavar="MODE", action='store', default='pull', help='')

def main():
    args = parser.parse_args()
    print(args)
