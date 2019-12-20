# xxe_poc

## 使用须知

* 安装 requests 模块```pip3 install requests```
* 需要 Python3 环境

## 1、内网主机扫描 inhostscan.py
```
用法：python3 inhostscan.py 漏洞地址 带扫描的IP段
示例：python3 inhostscan.py http://192.168.38.132/xxe_test.php 192.168.38
```

## 2、内网主机端口扫描 portscan.py
```
用法：python3 inhostscan.py 漏洞地址 待扫描的目标IP 扫描端口范围（支持输入单端口）
示例：python3 inhostscan.py http://192.168.38.132/xxe_test.php 192.168.38.129 1-65535
```

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
