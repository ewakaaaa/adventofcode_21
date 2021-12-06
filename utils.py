import os
import requests
from bs4 import BeautifulSoup

def download_test_puzzle(day_number):
    URL = f"https://adventofcode.com/2021/day/{day_number}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    puzzle_test = soup.find('pre') 
    puzzle_test = str(puzzle_test).replace("<pre><code>","").replace("</code></pre>","")[:-1]
    with open(f"day{day_number}/puzzle_test.txt", "w") as f:
        f.write(puzzle_test)

def make_folder(day_number):
    os.mkdir(os.getcwd()+f"/day{day_number}")
    with open(f'day{day_number}/day{day_number}.py', 'w') as f:
        f.write(f"""from utils import read_file \npuzzle = read_file({day_number})""") 

def read_file(day_number):
    file_name = os.getcwd() + f'day{day_number}/puzzle.txt'
    puzzle = open(file_name,'r') 
    return  puzzle.readlines()