#!/usr/bin/env python3
"""
ichiban.IchibanクラスのIchiban().hiku()メソッドについて
ヒストグラム化してランダムに引けているか分析
"""

import pandas as pd
import ichiban
poke = ichiban.Ichiban(a=1, b=2, c=1, d=9, e=18, f=14, g=15)


def uniq_list(li):
    return sorted(list(set(li)))


def count_kuji(li, label):
    return {k: li.count(k) for k in label}


def try_kuji(kuji, num):
    return [kuji.hiku() for _ in range(num)]


def kuji_hist(kuji, num, try_count):
    label = uniq_list(kuji)
    tryed = [
        count_kuji(li=try_kuji(kuji.copy(), num), label=label)
        for _ in range(try_count)
    ]
    df = pd.DataFrame(tryed)
    return df.sum() / df.sum().sum()


if __name__ == '__main__':
    try1000 = kuji_hist(poke.copy(), num=15, try_count=1000)
    prob = pd.Series(dict(poke.kuji()))
    print(pd.DataFrame({'try': try1000, 'probability': prob}))
    print('似た数値になればランダムに引けている')
