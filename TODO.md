# TODO

* クラス化
    * アトリビュートとして
    * `__get`メソッドで残りくじの選択簡単に
    * 期待値メソッド
        * 金額
    * シミュレートメソッド
        * ランダムに引く
    * describeメソッド
        * Aを引く確率、 Bを引く確率...
    * plotメソッド
        * describeメソッドを棒グラフで表示
    * next メソッド
        * Ichiban.next() でどれかの要素の数字を1減らす
        * Ichiban.next('A') で要素Aの数字を1減らす
* CalDict
    * 要素同士の計算
    ```python
    if len(value) > 1:
        return {self[i] + value[i] for i in self.keys()}
    ```
* インターフェース
    * スマホから計算
