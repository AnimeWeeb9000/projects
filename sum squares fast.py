# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MON

from time import time
import math

def list_nums(n: int):
    n = int(n)
    
    root = math.isqrt(n)
    if root * root == n:               # perfect-square fast path
        return [root, 0, 0, 0]

    def invalid_remainder(r: int):
        # Legendre: if the remainder is 7 then a cannot make 3 square sum
        while r % 4 == 0:
            r //= 4
        return r % 8 == 7

    limit = root
    squares = [i * i for i in range(limit + 1)]

    def two_square_decomp(s: int):
        i, j = 0, min(limit, math.isqrt(s))
        while i <= j:
            t = squares[i] + squares[j]
            if t == s:
                return i, j
            if t < s:
                i += 1
            else:
                j -= 1
        return None

    for a in range(limit, -1, -1):
        r = n - squares[a]
        if invalid_remainder(r):
            continue

        # optional pruning: enforce b <= a to cut symmetric duplicates
        bmax = min(a, math.isqrt(r))
        for b in range(bmax, -1, -1):
            s = r - b * b

            # quick necessary residue checks for two squares
            if s % 4 == 3:
                continue

            cd = two_square_decomp(s)
            if cd is not None:
                c, d = cd
                return [a, b, c, d]

    return None  # theoretically unreachable

# quick sanity test
if __name__ == "__main__":
    t1 = time()
    print(list_nums(123423412341234))      # e.g., [11, 1, 1, 0]
    t2 = time()
    print(f"This took {t2 - t1:.12f} seconds")
