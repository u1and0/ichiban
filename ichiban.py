#!/usr/bin/env python3
from collections import UserDict


class Ichiban:
    """一番くじ確率計算
    usage:
    ## NEW
        # 残り景品の数を入力
        >>> poke = Ichiban(A=1, B=2, C=2, D=15)

        # 残り景品とその数
        >>> poke
        {'A': 1,'B': 2,'C': 2, 'D': 15}

        # くじを引く確率
        >>> poke.kuji()
        {'A': 1/20,'B': 2/20,'C': 2/20, 'D': 15/20}

        # A,B賞を引く確率
        >>> poke.kuji('A', 'B')
        {'A': 1/20,'B': 2/20}

        # 期待値計算用に景品の仮の価格を入力
        >>> poke.kakaku(A=2000, B=1000, C=100, D=0)
        # 1/20 * 2000 + 2/20 * 1000 + 2/20 * 100 + 0
        # この価格がくじを価格を上回ればくじを引く意義がある

    ## OLD
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

    def __init__(self, title=None, **remain):
        """remain: 残り景品とその数
        >>> Ichiban(S=1, A=2, B=2).nokori  # 残り景品
        {'S': 1, 'A': 2, 'B': 2}
        """
        self.title = title
        self.nokori = CalDict(**remain)
        self.atari = None
        self.hazure = None

    def hosii(self, *hit):
        """hit: 当たりくじ
        >>> ich = Ichiban(A=1, B=9, C=90)
        >>> ich.atari is None
        True
        >>> ich.hazure is None
        True
        >>> ich.hosii('A', 'B')  # 欲しい景品
        {'A': 1, 'B': 9}
        >>> ich.atari
        {'A': 1, 'B': 9}
        >>> ich.hazure
        {'C': 90}
        """
        self.atari = {h: self.nokori[h] for h in hit}
        self.hazure = self.nokori.copy()
        for k in hit:
            self.hazure.pop(k)
        return self.atari

    def kuji(self, *hit):
        """当たりくじを引く確率
        >>> Ichiban(A=1, B=9).kuji('A')
        10.0
        """
        atari_list = self.hosii(*hit).values()
        nokori_list = self.nokori.values()
        return 100 * sum(atari_list) / sum(nokori_list)

    def all(self):
        """残りくじの数
        >>> Ichiban(S=1, A=2, B=2).all()
        5
        """
        return sum(self.nokori.values())

    def describe(self, *args):
        """各景品を引く確率
        >>> ich = Ichiban(A=1, B=9, C=90)
        >>> ich.describe()
        {'A': 0.01, 'B': 0.09, 'C': 0.9}
        >>> ich.describe('A', 'C')
        {'A': 0.01, 'C': 0.9}
        """
        if args:
            dic = CalDict(**{i: self.nokori[i] for i in args})
        else:
            dic = self.nokori.copy()
        describe_dict = dic / self.all()
        return describe_dict


class CalDict(UserDict):
    """Caluculatable dictionary with operator
    usage:
        # calculate
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic + 5
        {'a': 6, 'b': 10, 'c': 20}
        >>> cdic - 5
        {'a': -4, 'b': 0, 'c': 10}
        >>> cdic * 5
        {'a': 5, 'b': 25, 'c': 75}
        >>> cdic / 5
        {'a': 0.2, 'b': 1.0, 'c': 3.0}
        >>> cdic // 5
        {'a': 0, 'b': 1, 'c': 3}
        >>> cdic % 5
        {'a': 1, 'b': 0, 'c': 0}
        >>> cdic ** 5
        {'a': 1, 'b': 3125, 'c': 759375}
        >>> -cdic
        {'a': -1, 'b': -5, 'c': -15}

        # self calculate
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic -= 5
        >>> cdic
        {'a': -4, 'b': 0, 'c': 10}

        # reverse caluculate
        >>> cdic = CalDict(a=2, b=5, c=10)
        >>> 2 / cdic
        {'a': 1.0, 'b': 0.4, 'c': 0.2}

        # element add
        >>> cdic = CalDict(a=1, b=-1, c=15)
        >>> bdic = CalDict(a=1, b=1, c=1)
        >>> cdic += bdic
        >>> cdic  # all key
        {'a': 2, 'b': 0, 'c': 16}
        >>> cdic + {'a': 5, 'c':-5}  # particular keys
        {'a': 7, 'b': 0, 'c': 11}

        # slice
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic['a']  # normal slice
        1
        >>> cdic['a','c']  # multiple slice
        {'a': 1, 'c': 15}
        >>> list(cdic['a','c'].values())  # get list values
        [1, 15]

        # sum
        >>> cdic = CalDict(a=1, b=5, c=15)
        >>> cdic.sum()
        21
        >>> cdic['b', 'c'].sum()
        20
    """

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def __add__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] + value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v + value for k, v in self.items()})

    def __radd__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] + self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value + v for k, v in self.items()})

    def __sub__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] - value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v - value for k, v in self.items()})

    def __rsub__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] - self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value - v for k, v in self.items()})

    def __mul__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] * value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v * value for k, v in self.items()})

    def __rmul__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] * self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value * v for k, v in self.items()})

    def __truediv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] / value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v / value for k, v in self.items()})

    def __rtruediv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] / self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value / v for k, v in self.items()})

    def __floordiv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] // value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v // value for k, v in self.items()})

    def __rfloordiv__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] // self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value // v for k, v in self.items()})

    def __mod__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i] % value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v % value for k, v in self.items()})

    def __rmod__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i] % self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value % v for k, v in self.items()})

    def __pow__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: self[i]**value[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: v**value for k, v in self.items()})

    def __rpow__(self, value):
        try:
            dic = self.copy()
            if isinstance(value, dict) or isinstance(value.data, dict):
                dic.update(**{i: value[i]**self[i] for i in value.keys()})
                return dic
        except AttributeError:
            return CalDict(**{k: value**v for k, v in self.items()})

    def __neg__(self):
        return CalDict(**{k: -v for k, v in self.items()})

    def __getitem__(self, key):
        if len(key) < 2:
            return self.data[key]
        else:
            return CalDict(**{i: self.data[i] for i in key})

    def sum(self):
        return sum(self.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
