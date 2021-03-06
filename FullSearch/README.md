# 全探索（FullSearch）

## 参考
https://qiita.com/gogotealove/items/11f9e83218926211083a

## 概要

* n個の選択肢に、それぞれ Yes or No の二択がある  
* その部分集合（選択できるパターン、取りうる組み合わせ）を全て網羅的にチェックしたい

という場合に使えるアルゴリズム。

選択肢の1つ1つを2進数のbitに見立ててシフト演算でチェックを行うことから、`bit探索` とも呼ばれる。

## パターン数と計算量

### パターン数
 `2^n` となる。  
「Yes or No の2択」が「n個」あるため。

### 計算量
 `n * 2n` となる。  
* n=3 の場合、 `3 * (2 * 2 * 2)` で 24回。
* n=10 の場合、 `10 * (2^10)` で 10240回。
* n=20 の場合、 `20 * (2^20)` で 20971520回。

選択肢（今回の例だと果物の数）の増加に伴い、計算量は一気に増える。

## 例題1
```
みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。  
財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。
```

## 考え方・実装方法
全ての買い物パターン（=8パターン、2^3）の合計金額を計算し、その中から300円以下で済んだパターンだけを列挙する。
* 何も買わない（0,0,0）
* どれか1つ買う（1,0,0）
* どれか2つ買う（1,1,0）
* 全て買う（1,1,1）

### step 1 初期状態

step1実装状態：[ex1_step1.py](ex1_step1.py)

### step2 シフト演算

| 1 | 0 | 1 |
| --- | --- | --- |
| みかん | りんご | ぶどう |

 `(i >> n) & 1` ： i を n 回右にシフトした値と、論理積を取る（最下位桁が取得できる）

#### `(i >> n) & 1` によるループについて理解する
* `x >> n`
  * x のnビット右シフトする。
  * 右シフト1回につき、桁が1つ下がる。(ex:101 -> 10 -> 1)
* `& 1`
  * 1と論理積を取る。  
  * つまり、1 とビットマスクを取るということである。  
  * 1桁目が 0 なら 0が返り、 1 なら 1が返る。これにより、1桁目が1かどうかを判別できる。
    * ex:
      * 101 & 1 -> 1
      * 10 & 1 -> 0
      * 1 & 1 -> 1

step2実装状態：[ex1_step2.py](ex1_step2.py)

### step3 パターンごとの合計金額を計算し、処理を完成させる

step2実装状態：[ex1_step3.py](ex1_step3.py)

## 例題2
```
もも（50円）みかん（100円）ざくろ（150円）りんご（200円）ぶどう（300円）すいか（400円）がそれぞれ1つずつ果物屋さんにありました。  
財布の中には500円ありますが、考え得るすべての買い物パターンを列挙しなさい。
```

回答：[ex2.py](ex2.py)
