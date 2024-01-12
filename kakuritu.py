#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Shunsuke Otani
# SPDX-License-Identifier: BSD-3-Clause
import random

def main():
    min1 = int(input())
    max1 = int(input())

    if min1 > max1:
        return

    answer = random.randint(min1,max1)
    print(f"{answer}")

if __name__ == "__main__":
    main()
