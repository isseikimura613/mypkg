# mypkg
## mypkgについて
mypkgは千葉工業大学未来ロボティクス学科の2023年度ロボットシステム学の授業課題である。

## talker.pyとlistener.pyについて
* talker
  
  0.5秒おきに整数0からカウントする。
* listener
  
  talkerから受け取った内容を表示する。

## 実行例

talkerとlistenerを実行するには端末を分ける必要がある。

* talker（端末１）
```
$ ros2 run mypkg talker
```
実行結果

```
何も表示されない
```

* listener（端末２）
```
$ ros2 run mypkg listener
```

実行結果

```
[INFO] [1703689412.411794178] [listener]: Listen: 0
[INFO] [1703689412.889869328] [listener]: Listen: 1
[INFO] [1703689413.389504297] [listener]: Listen: 2
[INFO] [1703689413.890140154] [listener]: Listen: 3
[INFO] [1703689414.390001497] [listener]: Listen: 4
[INFO] [1703689414.890145275] [listener]: Listen: 5
[INFO] [1703689415.391211736] [listener]: Listen: 6
[INFO] [1703689415.890027850] [listener]: Listen: 7
```


## 必要なソフトウェア
* ROS2

## テスト環境
* Ubuntu 20.04

# ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©2023 Issei Kimura 
