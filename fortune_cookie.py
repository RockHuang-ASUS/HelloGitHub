import pyfiglet
import random

with open('messages.txt', 'r', encoding='utf-8') as f:
    messages = [line.strip() for line in f]

def open_cookie():
    message = pyfiglet.figlet_format(random.choice(messages))
    lines = message.splitlines()
    length = [len(line) for line in lines]
    max_length = max(length)
    lines = [f"|  {line}{' ' * (max_length - length[i])}  |" for i, line in enumerate(lines)]
    message = '\n'.join(lines)
    return f" {'_' * (max_length + 4)} \n{message}\n|{'_' * (max_length + 4)}|"

if __name__ == '__main__':
    print(open_cookie())
