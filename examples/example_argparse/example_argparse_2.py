import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--LifetheUniverseandEverything', action='store_const', const=42)
print(parser.parse_args(['--LifetheUniverseandEverything']))