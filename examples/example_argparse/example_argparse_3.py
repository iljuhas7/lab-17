import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--l', action='append')
print(parser.parse_args('--l a --l b --l Y'.split()))
