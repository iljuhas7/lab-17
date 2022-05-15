import argparse

parser = argparse.ArgumentParser(description='Great Description To Be Here')

parser.add_argument('-n', action='store', dest='n', help='Simple value')

print(parser.parse_args(['-n', '3']))
print(parser.parse_args([]))
print(parser.parse_args(['-a', '3']))