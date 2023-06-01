#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt 

def greet():
	print('Welcome to the Brain Games!')

def main():
	greet()
	welcome_user()

if __name__ == '__main__':
	main()

