#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Shunsuke Otani
# SPDX-License-Identifier: BSD-3-Clause
import random

def main():
    short = int(input())
    amount = int(input())

    if short > amount:
        return

    answer = random.randint(short,amount)
    print(f"{answer}")

if __name__ == "__main__":
    main()
