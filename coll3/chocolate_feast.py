def chocolateFeast(n: int, c: int, m: int) -> int:
    chocolates = n // c
    wrappers = chocolates
    while wrappers >= m:
        new_chocolates = wrappers // m
        chocolates += new_chocolates
        wrappers = wrappers % m + new_chocolates
    return chocolates