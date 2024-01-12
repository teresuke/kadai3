#!/usr/bin/python3

import random

def roll_dice(sides):
        return random.randint(1, sides)

def main():
    sides = int(input())##数字を選択する

    if sides <= 0:
        return      ##すく終了にする

    result = roll_dice(sides)
    print(f"{result}")

if __name__ == "__main__":
    main()
