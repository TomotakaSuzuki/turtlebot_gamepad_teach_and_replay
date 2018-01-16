# turtlebot_gamepad_teach_and_replay
PFoE(Particle Filter on Episode)をTurtleBotに実装したもの
## Demo
[PFoE with TurtleBot - YouTube](https://www.youtube.com/watch?v=HcmX92bSTL8&feature=youtu.be)
## Requirements
* TurtleBot2
* Ubuntu
  * Ubuntu 14.04(動作確認済み)
  * Ubuntu 16.04
* ROS
  * ROS Indigo(動作確認済み)
  * ROS Kinetic
* Controller
  * Logicool Wireless Gamepad F710
## Installation
TurtleBotを動かすためのパッケージをインストール  
以下はIndigoの場合
```
$ sudo apt-get install ros-indigo-turtlebot*
```
catkinワークスペースの作成
```
$ mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
$ catkin_init_workspace
$ cd ~/catkin_ws && catkin_make && source ~/catkin_ws/devel/setup.bash
```
リポジトリのclone
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/TomotakaSuzuki/turtlebot_gamepad_teach_and_replay.git
$ cd ~/catkin_ws && catkin_make
```
## Usage
ノードをlaunch
```
$ roslaunch turtlebot_bringup minimal.launch
$ roslaunch turtlebot_bringup 3dsensor.launch
$ roslaunch turtlebot_gamepad_training_replay training_replay.launch
```
### トレーニング
ゲームパッドのRBを押すとトレーニング操作の受付状態となり、センサとモータの出力をeventというトピックに記録するようになります。ゲームパッドのXボタンを押しながら十字キーを操作するとロボットが動きます。記録を終了するときはゲームパッドのLBを軽く押して終了します。記録中のトピックは~/.ros/内にバグファイルとして記録されます。ファイル名はROSのパラメータとして/current_bag_fileから得ることができます。
### リプレイ
トレーニング終了後、ゲームコントローラのLBを長押しするとリプレイがスタートします。その後はトレーニングかリプレイが選択できます。  
~/.ros下にバグファイルが溜まっていくので定期的に掃除をお願いします。
## Contributers
* Ryuichi Ueda  
RaspberryPi MouseにPFoEを実装したプログラム(元のコードのリポジトリ: [raspimouse_gamepad_teach_and_replay](https://github.com/ryuichiueda/raspimouse_gamepad_teach_and_replay))
* Ryo Okazaki  
ゲームパッドによるロボット操作プログラム(元のコードのリポジトリ: [raspimouse_game_controller](https://github.com/zaki0929/raspimouse_game_controller))
* Masahiro Kato  
イベントの出力コードの作成(元のコードのリポジトリ: [raspimouse_maze_manual](https://github.com/kato-masahiro/raspimouse_maze_manual))
## License
このリポジトリは、BSD-3-Clauseライセンス下です。[ライセンス](https://github.com/TomotakaSuzuki/turtlebot_gamepad_teach_and_replay/blob/master/LICENSE)を参照してください。
