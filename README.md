# jyuden
このROS 2パッケージは、`batterytalker` ノードを使用して、システムのバッテリー残量を定期的にパブリッシュします。バッテリーの状態を取得し、ROS 2のトピック `battery_status` にパブリッシュします。`batterytalker`ノードは、1秒ごとにバッテリーの状態を更新します。
# 概要
- `batterytalker`:このノードは、毎秒ごとに現在使用されてるデバイスの充電残量を出力します。
- `batterylistener`:このノードは、テスト用であり、`batterylistener`から受け取った情報を確認するために再度繰り返す。
# 実行例
まずは端末を２つ用意します
## 端末１

`batterytalker`ノードを実行し現在使用端末のバッテリー状態を取得します
```
$ ros2 run jyuden batterytalker
# なにも表示されませんが正常に作動しています。
```
## 端末２
`batterylistener`ノードを実行し、結果を表示します
- バッテリー残量が20%以上のとき
```
$ ros2 run jyuden batterylistener
[INFO] [1736391445.670933839] [batterylistener]: Received battery level: 100% -- Count: 1
[INFO] [1736391446.665502766] [batterylistener]: Received battery level: 100% -- Count: 2
[INFO] [1736391447.665620294] [batterylistener]: Received battery level: 100% -- Count: 3
```
- バッテリー残量が20%以下のとき
```
$ ros2 run jyuden batterylistener
[INFO] [1736392657.650492455] [batterylistener]: Received battery level: 20% -- Count: 1
[WARN] [1736392657.650813334] [batterylistener]: Battery level is low!
[INFO] [1736392658.644964797] [batterylistener]: Received battery level: 20% -- Count: 2
[WARN] [1736392658.645240354] [batterylistener]: Battery level is low!
[INFO] [1736392659.645093997] [batterylistener]: Received battery level: 20% -- Count: 3
[WARN] [1736392659.645472039] [batterylistener]: Battery level is low!
```
# 動作環境
## 必要な環境
- Ubuntu 22.04 LTS
- ROS 2 (Foxy以降)
- Python 3.8以上

## ライセンス
このリポジトリはBSD-3-Clauseライセンスのもとで公開されています。

## Copyright
© 2024 Ben Fang
