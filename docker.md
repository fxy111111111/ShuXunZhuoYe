***docker的使用方法（暑训作业）***

docker就是将系统隔离出一部分空间独立出来，用来配置。可以想象成一个没有系统的小型虚拟机。与本地系统是隔离的。但也可以通过特定的命令与系统联系起来。

sudo -i(到root用户提高权限)


*1.docker run*
语法：docker run {镜像名字} -d（让容器在后台执行）|-p(端口映射) {端口数据} |-v（挂载卷）挂载数据{宿主机目录：容器内目录（绑定挂载）/卷的名字：容器内的名字（命名卷挂载）} |-it（让我的控制台进入容器进行交互）|-rm（当容器停止的时候将容器清除掉）|--restart always（当容器停止时立即重启）/unless-stopped(当手动重启时可以不用重启)
作用：运行一个docker空间

*2.docker ps*
语法：docker ps -a（查看所有的，包括正在运行的和已经停止的）
作用：查看进程状态

*3.docker pull*
语法：docker pull {镜像名字} 
作用：下载镜像

*4.docker rm*
语法：docker rm -f（强制删除） {容器名字}
作用：删除容器

*5.docker rmi*
语法：docker rmi -f（强制删除） {镜像名字}
作用：删除镜像

*6.docker volume create*
语法：docker volume create {挂载卷名字}
作用：创建挂载卷

*7.docker volume inspect*
语法：docker volume insprct {挂载卷名字}
作用：查询挂载卷真实位置

*8.docker volume list*
语法：docker volmue list
作用：查看所有创建的卷

*9.docker stap*
语法：docker stap {容器名字}
作用：停止容器

*10.docker start*
语法：docker start {容器名字}
作用：重新启动容器，并保持原本的参数不变

*11.docker inspect*
语法：docker inspect {容器名字}
作用：查看容器信息

*12.docker exec -it*
语法：docker exec -it
作用：进入容器内部的控制台