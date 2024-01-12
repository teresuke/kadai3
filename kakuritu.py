#!/usr/bin/python3

import random

def kakuritu(amount):
    return random.randint(1,amount)

def main():
    amount = int(input())
    
    if amount <= 0:
        return
    
    answer = kakuritu(amount)
    print(f"{answer}")

if __name__ == "__main__":
    main()##下の二行はREADME.mdの説明にいるのか？
