import os
import requests
from bs4 import BeautifulSoup
import re


def download_test_puzzle(day_number):
    URL = f"https://adventofcode.com/2021/day/{day_number}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    puzzle_test = soup.find('pre') 
    puzzle_test = str(puzzle_test).replace("<pre><code>","").replace("</code></pre>","")
    with open(f"day{day_number}/puzzle_test.txt", "w") as f:
        f.write(puzzle_test)

def get_test_answer(day_number):
    URL = f"https://adventofcode.com/2021/day/{day_number}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    code_list = str(soup.find_all('code')).split("<code>")
    for item in code_list:
        if '<em>' in item:
            return int(re.search(r'\d+', item).group())

def make_folder(day_number):
    os.mkdir(os.getcwd()+f"/day{day_number}")
    for step in ["a","b"]:
        with open(f'day{day_number}/day{day_number}_{step}.py', 'w') as f:
            f.write(f"""import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file, get_test_answer
from aocd.models import Puzzle

puzzle_test = read_file({day_number},test = True)
puzzle = Puzzle(year=2021, day={day_number}).input_data

def solution(puzzle):
    return 

assert solution(puzzle_test) == get_test_answer({day_number})
puzzle.answer_{step} = solution(puzzle) 
"""
    )

def read_file(day_number,test = False):
    file_name = os.getcwd() + f'/day{day_number}/puzzle.txt'
    if test: 
        file_name = os.getcwd() + f'/day{day_number}/puzzle_test.txt'
    puzzle = open(file_name,'r') 
    return  puzzle.readlines() 