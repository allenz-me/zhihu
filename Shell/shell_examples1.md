### 1. 编写hello world脚本

```shell
#!/bin/bash
# 编写hello world脚本
echo "Hello World!"
```

### 2、通过位置变量创建 Linux 系统账户及密码

```shell
#!/bin/bash
# 通过位置变量创建 Linux 系统账户及密码
#$1 是执行脚本的第一个参数,$2 是执行脚本的第二个参数
useradd "$1"
echo "$2" | passwd ‐‐stdin "$1"
```

### 3、备份日志

```shell
#!/bin/bash
# 每周 5 使用 tar 命令备份/var/log 下的所有日志文件
# vim /root/logbak.sh
# 编写备份脚本,备份后的文件名包含日期标签,防止后面的备份将前面的备份数据覆盖
# 注意 date 命令需要使用反引号括起来,反引号在键盘<tab>键上面
tar	-czf	log-`date +%Y%m%d`.tar.gz	/var/log
# crontab ‐e	#编写计划任务,执行备份脚本
00	03	*	*	5	/root/logbak.sh
```

### 4、一键部署 LNMP(RPM 包版本)

```shell
#!/bin/bash
# 一键部署 LNMP(RPM 包版本)
# 使用 yum 安装部署 LNMP,需要提前配置好 yum 源,否则该脚本会失败
# 本脚本使用于 centos7.2 或 RHEL7.2
yum ‐y install httpd
yum ‐y install mariadb mariadb‐devel mariadb‐server
yum ‐y install php php‐mysql
systemctl start httpd mariadb
systemctl enable httpd mariadb
```

### 5、监控内存和磁盘容量，小于给定值时报警

```shell
#!/bin/bash
# 实时监控本机内存和硬盘剩余空间,剩余内存小于500M、根分区剩余空间小于1000M时,发送报警邮件给root管理员
# 提取根分区剩余空间
disk_size=$(df / | awk '/\//{print $4}')
# 提取内存剩余空间
mem_size=$(free | awk '/Mem/{print $4}')
while :
do
# 注意内存和磁盘提取的空间大小都是以 Kb 为单位
if [ $disk_size -le 512000 -a $mem_size -le 1024000 ]
then
mail ‐s "Warning" root <<EOF
Insufficient resources,资源不足
EOF
fi
done
```

1. -f：判断文件是否存在；
2. -d：判断目录是否存在；
3. -eq：等于，整数比较；
4. -ne：不等于，整数比较；
5. -lt：小于；
6. -gt：大于；
7. -le：小于或等于；
8. -ge：大于或等于；
9. -a：and，表示并的关系；
10. -o：or，或者，表示并的关系；
11. -z:空字符串；
12. ！：非；

**2.5、注意**

1、小括号可以使用>,<,=;并且括号内外可以没有空格；

2、中括号括号内侧必须要有空格；

3、中括号不可以使用<,>,=;而必须使用转义的逻辑判断条件

### 6、猜数字游戏

```shell
#!/bin/bash
# 脚本生成一个 100 以内的随机数,提示用户猜数字,根据用户的输入,提示用户猜对了,
# 猜小了或猜大了,直至用户猜对脚本结束。
# RANDOM 为系统自带的系统变量,值为 0‐32767的随机数
# 使用取余算法将随机数变为 1‐100 的随机数
num=$[RANDOM%100+1]
echo "$num"
# 使用 read 提示用户猜数字
# 使用 if 判断用户猜数字的大小关系:‐eq(等于),‐ne(不等于),‐gt(大于),‐ge(大于等于),
# ‐lt(小于),‐le(小于等于)
while :
do
read -p "计算机生成了一个 1‐100 的随机数,你猜: " cai
if [ $cai -eq $num ]
then
echo "恭喜,猜对了"
exit
elif [ $cai -gt $num ]
then
echo "Oops,猜大了"
else
echo "Oops,猜小了"
fi
done
```

### 12、编写脚本测试 192.168.4.0/24 整个网段中哪些主机处于开机状态,哪些主机处于关机状态 (for 版本)

```shell
#!/bin/bash
# 编写脚本测试 192.168.4.0/24 整个网段中哪些主机处于开机状态,哪些主机处于关机
# 状态(for 版本)
for i in {1..254}
do
# 每隔0.3秒ping一次，一共ping2次，并以1毫秒为单位设置ping的超时时间
ping ‐c 2 ‐i 0.3 ‐W 1 192.168.4.$i &> /dev/null
if [ $? -eq 0 ];then
echo "192.168.4.$i is up"
else
echo "192.168.4.$i is down"
fi
done
```

### 13、编写脚本测试 192.168.4.0/24 整个网段中哪些主机处于开机状态,哪些主机处于关机状态 (while 版本)

```shell
#!/bin/bash
# 编写脚本测试 192.168.4.0/24 整个网段中哪些主机处于开机状态,哪些主机处于关机
# 状态(while 版本)
i=1
while [ $i -le 254 ]
do
ping ‐c 2 ‐i 0.3 ‐W 1 192.168.4.$i &> /dev/null
if [ $? -eq 0 ]
then
echo "192.168.4.$i is up"
else
echo "192.168.4.$i is down"
fi
let i++
done
```

### 14、编写脚本测试 192.168.4.0/24 整个网段中哪些主机处于开机状态,哪些主机处于关机状态 (多进程版)

```shell
#!/bin/bash
# 编写脚本测试 192.168.4.0/24 整个网段中哪些主机处于开机状态,哪些主机处于关机
# 状态(多进程版)
#定义一个函数,ping 某一台主机,并检测主机的存活状态
myping(){
ping ‐c 2 ‐i 0.3 ‐W 1 $1 &>/dev/null
if [ $? -eq 0 ];then
echo "$1 is up"
else
echo "$1 is down"
fi
}
for i in {1..254}
do
myping 192.168.4.$i &
done
# 使用&符号,将执行的函数放入后台执行
# 这样做的好处是不需要等待ping第一台主机的回应,就可以继续并发ping第二台主机,依次类推。
```

### 17、9*9 乘法表

```shell
#!/bin/bash
# 9*9 乘法表(编写 shell 脚本,打印 9*9 乘法表)
for i in `seq 9`
do
for j in `seq $i`
do
echo -n "$j*$i=$[i*j] "  # -n 取消换行操作
done
echo  # 换行
done
```

### 26、对 100 以内的所有正整数相加求和(1+2+3+4...+100)

```shell
#!/bin/bash
# 对 100 以内的所有正整数相加求和(1+2+3+4...+100)
#seq 100 可以快速自动生成 100 个整数
sum=0
for i in `seq 100`
do
sum=$[sum+i]
done
echo "总和是:$sum"
```

整数运算：`$[]`和`(())`

### 32、统计/var/log 有多少个文件,并显示这些文件名

```shell
#!/bin/bash
# 统计/var/log 有多少个文件,并显示这些文件名
# 使用 ls 递归显示所有,再判断是否为文件,如果是文件则计数器加 1
cd /var/log
sum=0
for i in `ls -r *`
do
if [ -f $i ];then
let sum++
echo "文件名:$i"
fi
done
echo "总文件数量为:$sum"
```

### 60、批量下载有序文件(pdf、图片、视频等等)

```shell
#!/bin/bash
# 批量下载有序文件(pdf、图片、视频等等)
# 本脚本准备有序的网络资料进行批量下载操作(如 01.jpg,02.jpg,03.jpg)
# 设置资源来源的域名连接
url="百度一下，你就知道"
echo "开始下载..."
sleep 2
type=jpg
for i in `seq 100`
echo "正在下载$i.$type"
curl $url/$i.$type -o /tmp/${i}$type
sleep 1
done
#curl 使用-o 选项指定下载文件另存到哪里.
```


