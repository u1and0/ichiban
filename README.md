# CalDict

* Caluculatable dictionary with operator
* python dictionary enhancement
* inherit of `collection.UserDict`

## calculate
Enable to use `+, -, *, / , //, %, **, <, <=, >, >=` for dictionary.

```python
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
>>> cdic > 1
False
>>> -cdic <= -1
True
```

## self calculate
Enable to operate dictionary self.

```python
>>> cdic = CalDict(a=1, b=5, c=15)
>>> cdic -= 5
>>> cdic
{'a': -4, 'b': 0, 'c': 10}
```

## reverse caluculate
Operator can be used in either from right or left.

```python
>>> cdic = CalDict(a=2, b=5, c=10)
>>> 2 / cdic
{'a': 1.0, 'b': 0.4, 'c': 0.2}
```

## element add
Caliculatable for each keys.

```python
>>> cdic = CalDict(a=1, b=-1, c=15)
>>> bdic = CalDict(a=1, b=1, c=1)
>>> cdic += bdic
>>> cdic  # all key
{'a': 2, 'b': 0, 'c': 16}
>>> cdic + {'a': 5, 'c':-5}  # particular keys
{'a': 7, 'b': 0, 'c': 11}
```

## slice
Enable to use maltiple slice in addition to normal dictionary slice.

```python
>>> cdic = CalDict(a=1, b=5, c=15)
>>> cdic['a']  # normal slice
1
>>> cdic['a','c']  # multiple slice
{'a': 1, 'c': 15}
>>> list(cdic['a','c'].values())  # get list values
[1, 15]
```

## function apply
Using one or more operations over keys.
Like pandas.DataFrame().apply() method.

```python
>>> cdic = CalDict(a=1, b=5, c=15)
>>> cdic.apply(sum)
21
>>> cdic.apply(lambda x: x**2)
{'a': 1, 'b': 25, 'c': 225}
>>> cdic.apply(lambda x,y,z: x*y*z, 10, 0.5)
{'a': 5.0, 'b': 25.0, 'c': 75.0}
>>> cdic.apply([max,min])
{'max': 15, 'min': 1}
```

## stats
Support for basic stats methods `max, min, sum, mean`.

```python
>>> cdic = CalDict(a=1, b=5, c=15)
>>> cdic.max()
15
>>> cdic.min()
1
>>> cdic.sum()
21
>>> cdic.mean()
7.0
"""
```


# Ichiban
一番くじシミュレータ。
計算可能な辞書"CalDict"クラスを作成 / 継承して実装を易しくしています。


## くじを作成
ポケモンくじのインスタンスを作成します。
A賞が1個、 B賞が2個、 C賞が2個の仮想のくじを想定します。

```python
>>> poke = Ichiban(A=1, B=2, C=2)  # 引数は残り景品の数
```

これで`poke`から賞を引く確率を計算(`kuji()`メソッド)したり、くじを引くシミュレートができたり(`hiku()`メソッド)、このくじ自体の期待値を計算したりすることができます。

今あるくじの残り景品数を見るには`poke`で参照できます。

```python
>>> poke  # 残り景品とその数
{'A': 1, 'B': 2, 'C': 2}
```


## 確率計算
今あるくじを引いたときに、当てることができる景品の確率を計算します。

```python
>>> poke.kuji()  # くじを引く確率
{'A': 0.2, 'B': 0.4, 'C': 0.4}
```

A賞が0.2, すなわち20%の確率、B,C賞が0.4, すなわち40%の確率で当たることを示しています。

特定の賞の確率だけを抜き出すこともできます。
以下のようにして、`kuji()`メソッドの引数にA, Bを入れることで、A賞、B賞が当たるそれぞれ確率を表示します。

```python
>>> poke.kuji('A', 'B')  # A賞, B賞を引くそれぞれの確率
{'A': 0.2, 'B': 0.4}
```

A賞またはB賞が当たる確率はA,B賞のみの確率を計算した後、合計を出すsumメソッドで計算します。

```python
>>> poke.kuji('A', 'B').sum()  # A賞またはB賞を引く確率
0.6
```


## 期待値計算
期待値は「景品が当たる確率 x 景品の価格」で計算できます。
`kakaku()`メソッドを使えば簡単に計算をすることができます。
`kakaku()`メソッドの引数には景品の価格を自分で決めて、入力します。
以下の例ではA賞が2000円、B賞が1000円、C賞が100円として計算しました。

```python
>>> poke.kakaku(A=2000, B=1000, C=100)  # 期待値計算
840.0
```

結果、このくじの価格は840円です。
一番くじの価格は620円なので、計算上、このくじを引くと120円も得です。

> 実際のくじは店側が儲かるように作られるため、くじの初期配置の期待値はくじの金額を上回ることはありません。
> しかし、くじが妙に偏って引かれて上位賞だけが残ったり、特定の商品の価格を吊り上げたりすればくじの価格を上回ることは可能です。
> あくまで、賞に価格を付けるのは計算者自身なので、極端な話、C賞が2000円相当としてC賞がたくさん余っていればくじの期待値は上がります。


## シミュレート
A賞を引いて残数を1減らす(引数が無ければ景品ランダム)

```python
>>> poke.hiku('A')
'A'
```

A賞を引いた後の景品の数

```python
>>> poke.kuji()
{'A': 0, 'B': 2, 'C': 2}
```

A賞を引いた後の確率

```python
>>> poke.kuji()
{'A': 0.0, 'B': 0.5, 'C': 0.5}
```

引数がなければ、0になっていないくじを一枚ランダムに引きます。

```python
>>> poke.hiku()
'B'
```


## まとめ
以上の流れをまとめると

* `poke = Ichiban(A=1, B=2, ...)`でインスタンス(ここでは`poke`)を作成
* `poke.kuji()` で確率計算
* `poke.kakaku()`で期待値計算
* `poke.hiku()`でくじシミュレーション

```python
>>> poke = Ichiban(A=1, B=2, C=2)  # 引数は残り景品の数
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
```


[Gitghub - ichiban](https://github.com/u1and0/ichiban)
