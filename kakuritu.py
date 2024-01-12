#!/usr/bin/python3

import random

def main():
    amount = int(input())

    answer = random.randint(1,amount)
    print(f"{answer}")

if __name__ == "__main__":
    main()
