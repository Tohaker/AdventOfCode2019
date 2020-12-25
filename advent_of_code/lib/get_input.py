from os import path
import requests

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, 'session_token.txt'))

with open(filepath, 'r') as file:
    sessionId = [line for line in file][0]

cookies = {'session': sessionId}


def download_input(dayNo):
    input = requests.get(
        f'https://www.adventofcode.com/2019/day/{dayNo}/input', cookies=cookies)
    return list(filter(len, [line.strip() for line in input.text.split('\n')]))
