**nav2_costmap_2d:构建2d地图**
订阅：sensor_msgs/LaserScan(激光雷达点云),nav_msgs/Odometry(里程计)
发布：nav2_msgs/Costmap(代价地图)


**nav2_planner:路径规划**
sub:nav_msgs/Costmap(代价地图)
    geomentry_msgs/PoseStamped(目标点)
pub:nav_msgs/path


**nav2_controller:局部路径控制，控制机器人**
sub:nav_msgs/path(全局路线)
    sensor_msgs/LaserScan(激光雷达点云)
pub:geomentry_msgs/Twist(控制指令)


**nav2_bt_navigator:行为树导航框架，串联了“路径规划->避障->控制”**
sub:geomentry_msgs/PoseStamped(目标点)


**nav2_lifecycle_manager:管理navigation2各版块的生命周期**


***1.环境感知与地图***
nav2_costmap_2d:构建2d地图。
nav2_map_server:加载，发布，保存地图。
nav2_occgrid_loader:地图加载的辅助工具。

***2.路径规划***
nav2_planner:全局路径规划。
nav2_navfn_planner:基于navfn算法的路径规划，nav2_planner的补充，适用于简单的场景。
nav2_smac_planner:基于State Lattice的规划器，更贴合机器人运动学特征。
nav2_behavior_tree:提供导航相关的行为节点树。

***3.运动控制相关***
nav2_controller:局部路径跟踪和控制根据全局地图和实时地图发布对机器人的控制命令。
nav2_dwb_controller:基于动态窗口法的局部控制器在速度空间寻求最优解。
nav2_regulated_pure_pursuit_controller:基于“Pure Oursuit”算法适用于低速平滑场景。

***4.导航逻辑与行为管理***
nav2_bt_navigator:导航的“行为决策核心”通过行为树（BT）串联“路径规划，控制，避障等”。
nav2_navigator:提供高层导航接口，接收用户目标请求点，协调“nav2_navigator”去实现。

***5.定位与里程计相关***
nav2_amcl:通过传感器确定机器人位置。
nav2_pose_estimator:提供位姿接口，为导航提供统一的机器人位姿数据。

***6.系统管理工具***
nav2_lifecycle_manager:管理navigator2中所有模块的生命周期和其的初始化顺序。
nav2_util:提供工具函数（如：日志，参数解析，时间转换等）。
nav2_node:导航节点的基础框架，封装节点之类。

***7.调试与可视化相关***
nav2_rviz_plugins:提供Rviz专用插件。
nav2_bt_visualizer:可视化nav2_bt_navigator的行为树过程。


