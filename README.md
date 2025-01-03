# ROS 2BatteryTalkerでパソコンの充電残量確認
このパッケージは、現在のデバイスのバッテリー状態を定期的に観測し、ROS 2 のトピックを介して他のノードに送信する機能を提供します。`BatteryTalker` ノードがバッテリー状態を定期的にパブリッシュし、`BatteryListener `ノードはテスト用です。

## 概要
- BatteryTalker:このノードは、毎秒ごとに現在使用されてるデバイスの充電残量を出力します。
- BatteryListener:このノードは、BatteryTalkerから受け取った情報を確認するために再度繰り返す。
## セットアップ方法
### リポジトリをクローン
このリポジトリをクローンします
```
git clone https://github.com/ssssben/jyuuden.git
```
### 使い方
はじめにディレクトリに移動してビルドをしてください
```
cd jyuuden
colcon build
```
そして環境をソースしてください
```
source install/setup.bash
```
ノードを実行します
```
ros2 run mypkg batterytalker
```

## 実行例
以下が`batterytalker`の実行例になります:
```
[INFO] [1735893812.604802516] [batterytalker]: Battery level: 97%
[INFO] [1735893813.598910572] [batterytalker]: Battery level: 97%
[INFO] [1735893814.599055181] [batterytalker]: Battery level: 97%
[INFO] [1735893815.599096051] [batterytalker]: Battery level: 97%
[INFO] [1735893816.598954601] [batterytalker]: Battery level: 97%
```

## 動作環境
### 必要な環境
- Ubuntu 22.04 LTS
- ROS 2 (Foxy以降)
- Python 3.8以上

### ライセンス
このリポジトリはBSD-3-Clauseライセンスのもとで公開されています。

### Copyright
© 2024 Ben Fang
