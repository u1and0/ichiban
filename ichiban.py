#!/usr/bin/env python3


class Ichiban:
    """一番くじ確率計算
    usage:
        # A賞が1個、B賞が9個残っているくじの計算
        >>> ich = Ichiban(A=1, B=9)
        >>> ich.nokori  # 残り景品とその数
        {'A': 1, 'B': 9}
        >>> ich.kuji('A')  # A賞を引く確率
        10.0

        # A,B,C,D賞がそれぞれ1,9,90,100個残っているくじの計算
        >>> ich = Ichiban(A=1, B=9, C=90, D=100)
        >>> ich.atari('A', 'B', 'C')  # 当たり景品
        {'A': 1, 'B': 9, 'C': 90}
        >>> ich.all()  # 景品の全数
        200

    args:
        hit: 当たりくじの賞
        remain: 現在余っている景品とその数
    """

    def __init__(self, **remain):
        """remain: 残り景品とその数
        >>> Ichiban(S=1, A=2, B=2).nokori
        {'S': 1, 'A': 2, 'B': 2}
        """
        self.nokori = remain

    def atari(self, *hit):
        """hit: 当たりくじ
        >>> Ichiban(A=1, B=9, C=90).atari('A', 'B')
        {'A': 1, 'B': 9}
        """
        return {h: self.nokori[h] for h in hit}

    def kuji(self, *hit):
        """当たりくじを引く確率
        >>> Ichiban(A=1, B=9).kuji('A')
        10.0
        """
        atari_list = self.atari(*hit).values()
        nokori_list = self.nokori.values()
        return 100 * sum(atari_list) / sum(nokori_list)

    def all(self):
        """残りくじの数
        >>> Ichiban(S=1, A=2, B=2).all()
        5
        """
        return sum(self.nokori.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
