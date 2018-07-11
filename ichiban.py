#!/usr/bin/env python3
"""
# Ichiban
Ichiban kuji simulator
"""
from collections import UserList
import random


class Ichiban(UserList):
    """一番くじ確率計算
    usage:
        >>> poke = Ichiban(A=1, B=2, C=2)  # 残り景品の数を入力
        >>> poke.data  # 残り景品
        ['A', 'B', 'B', 'C', 'C']
        >>> poke  # 残り景品とその数(__repr__で返される)
        {'A': 1, 'B': 2, 'C': 2}
        >>> poke.dict()  # 残り景品とその数(dict型で返される)
        {'A': 1, 'B': 2, 'C': 2}
        >>> len(poke)  # 残り景品の全数
        5
        >>> poke.kuji()  # それぞれの景品を引く確率
        {'A': 0.2, 'B': 0.4, 'C': 0.4}
        >>> poke.kuji('A', 'B')  # A賞またはB賞を引く確率
        0.6
        >>> poke.kakaku(A=2000, B=1000, C=100)  # 期待値計算, 景品に価格を付ける
        840.0
        >>> poke.kakaku(A=2000)  # 期待値計算, 引数が足りなければdefaultに指定された価格(default=0)
        400.0
        >>> poke.hiku('B')  # B賞を引いて残数を1減らす(引数が無ければランダムに景品を選択)
        'B'
        >>> poke.kuji()  # A賞を引いた後の確率
        {'A': 0.25, 'B': 0.25, 'C': 0.5}
        >>> len(poke)  # A賞を引いた後の全数
        4

    args: remain:
        現在余っている景品とその数
    self.data:
        リスト型 (__repr__では辞書型に見えるが、メソッドはリスト型を継承)
    self.dict():
        dict typeとして返す。valuesは個数。
    self.__repr__():
        インスタンスを打った時にdictのように表示する。
    self.kuji(self, *keys):
        景品を引く確率計算
    self.kakaku(self, default=0, **val):
        期待値計算
    self.hiku(self, key=None):
        くじ引きシミュレート
    """

    def __init__(self, **remain):
        super().__init__(self)
        self.data = [x for k, v in remain.items() for x in list(k * v)]

    def dict(self):
        """return dict type data"""
        return {k: self.count(k) for k in sorted(list(set(self)))}

    def __repr__(self):
        return self.dict().__repr__()

    def kuji(self, *keys):
        """景品を引く確率計算"""
        if keys:
            # float type
            return sum([self.count(k) for k in set(keys)]) / len(self)
        return {k: self.count(k) / len(self) for k in self}  # dict type

    def kakaku(self, default=0, **val):
        """期待値計算"""
        prob = self.kuji()
        kakaku_dic = {k: val.get(k, default) for k in prob.keys()}
        kitai_dic = {k: prob[k] * kakaku_dic[k] for k in kakaku_dic.keys()}
        return sum(kitai_dic.values())

    def hiku(self, key=None):
        """くじ引きシミュレート"""
        index = self.index(key if key else random.choice(self))
        return self.pop(index)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
