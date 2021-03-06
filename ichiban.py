#!/usr/bin/env python3
"""Ichiban kuji simulator"""
from collections import UserList
import random


def sumup_list(li: list) -> dict:
    """ count duplication of list elements and return dictionary"""
    uniq_list = sorted(list(set(li)))
    return {k: li.count(k) for k in uniq_list}


class Ichiban(UserList):
    """一番くじ確率計算
    description:
        args:
            remain: 現在余っている景品とその数
        self.data:
            インスタンスの実態を表すリスト型
        self.dict():
            dict typeとして返す。valuesは個数
        self.__repr__():
            インスタンスを打った時にdictのように表示する
            (注意！インスタンスの実態はself.data<-リスト型)
        self.kuji(*keys):
            景品を引く確率計算
        self.kakaku(default=0, **val):
            期待値計算
        self.hiku(key=None):
            くじ引きシミュレート
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

        # kuji(): 確率計算
        >>> poke.kuji()  # それぞれの景品を引く確率
        {'A': 0.2, 'B': 0.4, 'C': 0.4}
        >>> poke.kuji('A', 'B')  # A賞またはB賞を引く確率
        0.6

        # kakaku(): 期待値計算
        >>> poke.kakaku(A=2000, B=1000, C=100)  # A賞2000円、B賞1000円、C賞100円の価値
        840.0
        >>> poke.kakaku(A=2000, default=100)  # A賞2000円、それ以外100円
        480.0
        >>> poke.kakaku(A=2000)  # defaultは指定しなければ0円
        400.0

        # hiku(): くじシミュレート
        >>> poke.hiku('A')  # A賞を引いて残数を1減らす(引数が無しでランダム選択)
        'A'
        >>> poke  # 一個しかないA賞を引いたのでAがなくなる
        {'B': 2, 'C': 2}
        >>> poke.kuji()  # A賞を引いた後の確率
        {'B': 0.5, 'C': 0.5}
        >>> len(poke)  # A賞を引いた後の全数は1減っている
        4
    """

    def __init__(self, **remain):
        super().__init__(self)
        self.data = [x for k, v in remain.items() for x in list(k * v)]

    def dict(self):
        """return dict type data"""
        return sumup_list(self)

    def __repr__(self):
        return sumup_list(self).__repr__()

    def copy(self):
        return self.__class__(**self.dict())

    def kuji(self, *keys):
        """景品を引く確率計算
        description:
            * 現在残っている景品を引く確率を計算する
            * 引数がなければ、それぞれの景品を引く確率をdictionaryとして返す
            * 引数があれば、引数の景品を引く確率の合計をfloatとして返す
        usage:
            >> poke = Ichiban(A=1, B=2, C=2)  # 残り景品の数を入力
            >> poke.kuji()  # それぞれの景品を引く確率
            {'A': 0.2, 'B': 0.4, 'C': 0.4}
            >> poke.kuji('A', 'B')  # A賞またはB賞を引く確率
            0.6
        """
        # float type
        if keys:
            return sum([self.count(k) for k in set(keys)]) / len(self)
        # dict type
        return {k: self.count(k) / len(self) for k in self}

    def kakaku(self, default=0, **val):
        """期待値計算
        descripton:
            景品の価格を引数に取り、[価格x確率]の合計値を返す
        usage:
            >> poke = Ichiban(A=1, B=2, C=2)  # 残り景品の数を入力
            >> poke.kakaku(A=2000, B=1000, C=100)  # A賞2000円、B賞1000円、C賞100円の価値
            840.0
            >> poke.kakaku(A=2000, default=100)  # A賞2000円、それ以外100円
            480.0
            >> poke.kakaku(A=2000)  # defaultは指定しなければ0円
            400.0
        """
        prob = self.kuji()
        # if `val` has same `prob` key then `val` or `default` value
        kakaku_dic = {k: val.get(k, default) for k in prob.keys()}
        # multiply kakaku_dic[key] * kitai_dic[key] for each
        kitai_dic = {k: prob[k] * kakaku_dic[k] for k in kakaku_dic.keys()}
        return sum(kitai_dic.values())

    def hiku(self, key=None):
        """くじ引きシミュレート
        description:
            * keyが指定されれば、keyの景品を引く
            * keyが指定がされなければ、ランダムに景品を引く
        usage:
            >> poke = Ichiban(A=1, B=2, C=2)  # 残り景品の数を入力
            >> poke.hiku('A')  # A賞を引いて残数を1減らす(引数が無しでランダム選択)
            'A'
            >> poke  # 一個しかないA賞を引いたのでAがなくなる
            {'B': 2, 'C': 2}
            >> poke.kuji()  # A賞を引いた後の確率
            {'B': 0.5, 'C': 0.5}
            >> len(poke)  # A賞を引いた後の全数は1減っている
            4
        """
        index = self.index(key if key else random.choice(self))
        return self.pop(index)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
