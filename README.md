# mypkg
[![test](https://github.com/isseikimura613/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/isseikimura613/mypkg/actions/workflows/test.yml)

## mypkgについて
mypkgは千葉工業大学未来ロボティクス学科2023年度ロボットシステム学の授業課題のリポジトリである。

また、このリポジトリはtalker.pyとlistener.pyの間で通信を行うROS 2のパッケージである。

## talker.pyとlistener.pyについて
* talker.py
  
  0.5秒おきに数字をカウントしてトピック（countup）を通じて送信する。
  
* listener.py
  
  トピック（countup）から受け取った内容を表示する。

## トピックについて

ROS 2のノード間でデータをやり取りするための流路である。

talkerはトピック（countup）に16ビット符号つき整数データを送信するノードであり、listenerはトピック（countup）からそのデータを受信するノードである。


## 実行例

talker.pyとlistener.pyを実行するには端末を分ける必要がある。

* talker.py（端末１）
```
$ ros2 run mypkg talker
```

```
何も表示されない
```

* listener.py（端末２）
```
$ ros2 run mypkg listener
```

```
[INFO] [1703689412.411794178] [listener]: Listen: 0
[INFO] [1703689412.889869328] [listener]: Listen: 1
[INFO] [1703689413.389504297] [listener]: Listen: 2
[INFO] [1703689413.890140154] [listener]: Listen: 3
[INFO] [1703689414.390001497] [listener]: Listen: 4
[INFO] [1703689414.890145275] [listener]: Listen: 5
[INFO] [1703689415.391211736] [listener]: Listen: 6
[INFO] [1703689415.890027850] [listener]: Listen: 7
...
```

## launch

talker.pyとlistener.pyを同時に動かすことができる。

* 実行例

```
$ ros2 launch mypkg talk_listen.launch.py
```

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
...
```

## 必要なソフトウェア
* Python
* ROS 2

## テスト環境
* Ubuntu 20.04

## テスト内容
2023年度ロボットシステム学の授業内で使用したコンテナを使用しています。
* [使用したコンテナ](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)

# ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されています。
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
    * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©2023 Issei Kimura 
