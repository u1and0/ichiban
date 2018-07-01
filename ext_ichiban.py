#!/usr/bin/env python3
import pandas as pd
from ichiban import Ichiban


class ExtIchiban(Ichiban):
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
        >>> ich.hosii('A', 'B')  # 当たり景品
        {'A': 1, 'B': 9}
        >>> ich.all()  # 景品の全数
        200

    args:
        hit: 当たりくじの賞
        remain: 現在余っている景品とその数
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def describe(self):
        num = pd.Series(self.nokori, index=self.nokori.keys())
        df = pd.DataFrame({'景品数': num, '確率': num / self.all()})
        return df

    def plot(self, target='確率', kind='pie', *args, **kwargs):
        return self.describe()[target].plot(kind=kind, *args, **kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
