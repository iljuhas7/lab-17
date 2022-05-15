import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--verbose', '-v', action='count')
print(parser.parse_args('-vvv'.split()))
