import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():  # 修复：函数名缺少下划线
    # 1. 获取机械臂URDF默认路径
    urdf_package_path = get_package_share_directory('fist.jixiebi')
    default_urdf_path = os.path.join(urdf_package_path, 'urdf', 'jliebi.urdf')

    # 2. 声明可动态修改的URDF路径参数
    model_arg = launch.actions.DeclareLaunchArgument(  # 修复：改为大驼峰命名
        name='model',
        default_value=default_urdf_path,
        description='机械臂URDF模型文件路径'
    )  # 修复：补全右括号

    # 3. 通过系统命令读取URDF文件内容
    robot_description_content = launch.substitutions.Command(
        ['cat', launch.substitutions.LaunchConfiguration('model')]
    )

    # 4. 将URDF内容封装为ROS参数
    robot_description = launch_ros.parameter_descriptions.ParameterValue(
        robot_description_content,
        value_type=str
    )

    # 5. 配置机器人状态发布节点
    robot_state_publisher_node = launch_ros.actions.Node(  # 修复：改为Node而非Model
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description
        }]  # 修复：方括号闭合
    )

    # 6. 整合所有组件
    return launch.LaunchDescription([
        model_arg,
        robot_state_publisher_node,
    ])  # 修复：使用方括号并正确闭合