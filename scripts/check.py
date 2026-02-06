import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--token", required=True)
args = parser.parse_args()

print(f"Check completed (token length: {len(args.token)})")
