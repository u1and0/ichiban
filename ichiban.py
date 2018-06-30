#!/usr/bin/env python3


def kuji(*hit, **remain):
    """
    usage:
        >>> kuji('A', A=1, B=9)
        10.0
        >>> kuji('A', 'B', A=1, B=9, C=90)
        10.0
        >>> kuji('A', 'B', 'C', A=1, B=9, C=90, D=100)
        50.0
        >>> kuji('A', A=1, B=9, C=90, D=100)
        0.5

    args:
        hit: 当たりくじの賞
        remain: 現在余っているくじ

    return: 当たりくじが当たる確率
"""
    atari = [remain[_] for _ in hit]
    nokori = list(remain.values())
    return 100 * sum(atari) / sum(nokori)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
