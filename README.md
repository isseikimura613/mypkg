# mypkg
[![test](https://github.com/isseikimura613/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/isseikimura613/mypkg/actions/workflows/test.yml)

## mypkgについて
mypkgは千葉工業大学未来ロボティクス学科の2023年度ロボットシステム学の授業課題である。

## talker.pyとlistener.pyについて
* talker.py
  
  0.5秒おきに整数0からカウントする。
  
* listener.py
  
  talkerから受け取った内容を表示する。

## 実行例

talker.pyとlistener.pyを実行するには端末を分ける必要がある。

* talker.py（端末１）
```
$ ros2 run mypkg talker
```
実行結果

```
何も表示されない
```

* listener.py（端末２）
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

## launch

talker.pyとlistener.pyを同時に動かすことができる。

* 実行例

```
$ ros2 launch mypkg talk_listen.launch.py
```

* 実行結果

```
[INFO] [launch]: All log files can be found below /home/issei38/.ros/log/2023-12-28-00-14-19-650196-ISSEI-853
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [855]
[INFO] [listener-2]: process started with pid [857]
[listener-2] [INFO] [1703690060.600461651] [listener]: Listen: 0
[listener-2] [INFO] [1703690061.082175945] [listener]: Listen: 1
[listener-2] [INFO] [1703690061.581881313] [listener]: Listen: 2
[listener-2] [INFO] [1703690062.082301753] [listener]: Listen: 3
[listener-2] [INFO] [1703690062.581819096] [listener]: Listen: 4
[listener-2] [INFO] [1703690063.082548454] [listener]: Listen: 5
```

## トピック

ROS2のノード間でデータをやり取りするための仕組みである。

talkerはトピックにデータを送信するノードであり、listenerはトピックからデータを受信するノードである。


## 必要なソフトウェア
* ROS2

## テスト環境
* Ubuntu 20.04

# ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©2023 Issei Kimura 