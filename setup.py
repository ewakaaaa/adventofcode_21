import argparse
from utils import make_folder, download_test_puzzle

parser = argparse.ArgumentParser()
parser.add_argument("--day", type=int)
args = parser.parse_args()

make_folder(args.day)
download_test_puzzle(args.day)

