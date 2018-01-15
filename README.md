# turtlebot_gamepad_teach_and_replay
Implementing PFoE(Particle Filter on Episode) in TurtleBot. 
## Demo
[PFoE with TurtleBot - YouTube](https://www.youtube.com/watch?v=HcmX92bSTL8&feature=youtu.be)
## Requirements
* TurtleBot2
* Ubuntu
  * Ubuntu 14.04(Operation has been confirmed)
  * Ubuntu 16.04
* ROS
  * ROS Indigo(Operation has been confirmed)
  * ROS Kinetic
* Controller
  * Logicoo Wireless Gamepad F710
## Installation
Install package to run TurtleBot.
```
$ sudo apt-get install ros-indigo-turtlebot*
```
Create catkin_ws.
```
$ mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
$ catkin_init_workspace
$ cd ~/catkin_ws && catkin_make && source ~/catkin_ws/devel/setup.bash
```
Clone of this repository.
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/TomotakaSuzuki/turtlebot_gamepad_teach_and_replay.git
$ cd ~/catkin_ws && catkin_make
```
## Usage
Start up the node.
```
$ roslaunch turtlebot_bringup minimal.launch
$ roslaunch turtlebot_bringup 3dsensor.launch
$ roslaunch turtlebot_gamepad_training_replay training_replay.launch
```
### Training
When the 'RB' of the gamepad is pushed, it becomes acceptance state of training operation, and output of sensor and motor is recorded in topic of the event. Robots can be operated with the four-way controller while holding down the 'x' button of the gamepad. When you can stop the teach with a push of the 'LB' of the gamepad. The episode is recored to a file in ~/.ros/. The name of the file can be obtained from the ROS parameter `/current\_bag\_file`.
### Replay
After the training, the replay can be started by long pushing the 'LB' button of the gamepad. It finishes with one more push of the 'LB' button. After that, you can restart the replay again.  
### Caution
Bag files are stored in ~/.ros but they are not erased. Please clean in the directory occasionally.
## Contributers
* Ryuichi Ueda  
codes that first implemented the PFoE algorithm(original repository: [raspimouse_gamepad_teach_and_replay](https://github.com/ryuichiueda/raspimouse_gamepad_teach_and_replay))
* Ryo Okazaki  
codes for gamepad control(original repository: [raspimouse_game_controller](https://github.com/zaki0929/raspimouse_game_controller))
* Masahiro Kato  
codes for teaching(original repository: [raspimouse_maze_manual](https://github.com/kato-masahiro/raspimouse_maze_manual))
