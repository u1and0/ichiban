#!/usr/bin/env python3


class Ichiban:
    """一番くじ確率計算"""

    def __init__(self, *hit, **remain):
        self.atari = [remain[_] for _ in hit]
        self.nokori = remain

    def kuji(self):
        """当たりくじを引く確率
        usage:
            >>> Ichiban('A', A=1, B=9).kuji()
            10.0
            >>> Ichiban('A', 'B', A=1, B=9, C=90).kuji()
            10.0
            >>> Ichiban('A', 'B', 'C', A=1, B=9, C=90, D=100).kuji()
            50.0
            >>> Ichiban('A', A=1, B=9, C=90, D=100).kuji()
            0.5

        args:
            hit: 当たりくじの賞
            remain: 現在余っているくじ

        return: 当たりくじが当たる確率
        """
        return 100 * sum(self.atari) / sum(self.nokori.values())

    def all(self):
        """残りくじの数"""
        return sum(self.nokori.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
