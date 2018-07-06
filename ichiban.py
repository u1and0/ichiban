#!/usr/bin/env python3
from collections import UserDict
import random


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
        >>> cdic > 0
        True
        >>> -cdic <= -1
        True

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

    def __gt__(self, value):
        return all(i > value for i in self.values())

    def __lt__(self, value):
        return all(i < value for i in self.values())

    def __ge__(self, value):
        return all(i >= value for i in self.values())

    def __le__(self, value):
        return all(i <= value for i in self.values())

    def __getitem__(self, key):
        if len(key) < 2:
            return self.data[key]
        else:
            return CalDict(**{i: self.data[i] for i in key})

    def sum(self):
        return sum(self.values())


class Ichiban(CalDict):
    """一番くじ確率計算
    usage:
        >>> poke = Ichiban(A=1, B=2, C=2)  # 残り景品の数を入力
        >>> poke  # 残り景品とその数
        {'A': 1, 'B': 2, 'C': 2}
        >>> poke.kuji()  # くじを引く確率
        {'A': 0.2, 'B': 0.4, 'C': 0.4}
        >>> poke.kuji('A', 'B')  # A賞, B賞を引くそれぞれの確率
        {'A': 0.2, 'B': 0.4}
        >>> round(poke.kuji('A', 'B').sum(), 1)  # A賞またはB賞を引く確率
        0.6
        >>> poke.kakaku(A=2000, B=1000, C=100)  # 期待値計算
        840.0
        >>> poke.hiku('A')  # A賞を引いて残数を1減らす(引数が無ければ景品ランダム)
        'A'
        >>> poke.kuji()  # A賞を引いた後の確率
        {'A': 0.0, 'B': 0.5, 'C': 0.5}

    args:
        remain: 現在余っている景品とその数
    """

    def __init__(self, **remain):
        super().__init__(**remain)

    def kuji(self, *keys):
        if not keys:
            return self / self.sum()
        else:
            return self[keys] / self.sum()

    def hiku(self, key=None):
        if not key:
            key = random.choice(list(self.keys()))
        self[key] -= 1
        return key

    def kakaku(self, **values):
        kakaku_dic = self.kuji() * values
        return kakaku_dic.sum()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
