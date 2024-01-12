#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Shunsuke Otani
# SPDX-License-Identifier: BSD-3-Clause
import random

def main():
    amount = int(input())

    answer = random.randint(1,amount)
    print(f"{answer}")

if __name__ == "__main__":
    main()
