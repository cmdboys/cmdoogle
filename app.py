# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from colorama import  init, Fore, Back, Style  
init(autoreset=True)  
import urllib.request
from urllib.parse import quote

baseurl = "http://www.baidu.com/s?wd="

class Colored(object):  
  
    #  前景色:红色  背景色:默认  
    def red(self, s):  
        return Fore.RED + s + Fore.RESET  
  
    #  前景色:绿色  背景色:默认  
    def green(self, s):  
        return Fore.GREEN + s + Fore.RESET  
  
    #  前景色:黄色  背景色:默认  
    def yellow(self, s):  
        return Fore.YELLOW + s + Fore.RESET  
  
    #  前景色:蓝色  背景色:默认  
    def blue(self, s):  
        return Fore.BLUE + s + Fore.RESET  
  
    #  前景色:洋红色  背景色:默认  
    def magenta(self, s):  
        return Fore.MAGENTA + s + Fore.RESET  
  
    #  前景色:青色  背景色:默认  
    def cyan(self, s):  
        return Fore.CYAN + s + Fore.RESET  
  
    #  前景色:白色  背景色:默认  
    def white(self, s):  
        return Fore.WHITE + s + Fore.RESET  
  
    #  前景色:黑色  背景色:默认  
    def black(self, s):  
        return Fore.BLACK  
  
    #  前景色:白色  背景色:绿色  
    def white_green(self, s):  
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET  

color = Colored() 

def getHtml(keyword = ""):
	fp = urllib.request.urlopen(baseurl+quote(keyword))
	mybytes = fp.read()

	mystr = mybytes.decode("utf8")
	fp.close()
	soup = BeautifulSoup(mystr, 'html.parser')


	barr = soup.select('.c-container')

	cArray = []
	gg = 0;

	
	for child in barr:
		if child.select('h3'):
			gg+=1
			ghh = str(gg)+". "+child.select('h3')[0].get_text();
			print(color.green(ghh.replace('\n',''))) 
			print(color.yellow('----------------------------------------'))


	return barr;

def openPage(url):
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()

	mystr = mybytes
	fp.close()
	soup = BeautifulSoup(mystr, 'html.parser')
	print("\n")
	print("+-----------------------------+")
	print("\n")
	print(color.yellow(soup.title.get_text()))
	print("\n")
	print("+-----------------------------+")
	print("\n")
	print(color.green(soup.body.get_text()))
	print("\n")
	print("+-----------------------------+")
	print("\n")
	print(color.yellow("+---- 请阅读以下命令以继续：------+"))
	print(color.red("B(返回搜索)，[ctrl]+[c] 退出"))
	typee = input("：")

	if typee == "B":
			runner()


def runner():
	print("+------------------------------------------------------------+")
	print("|							     |")
	print(color.yellow("|		         Cmdoogle	          	     |"))
	print("|							     |")
	print("+------------------------------------------------------------+")
	print(color.yellow("请输入搜索内容："))
	ins = input("：")
	print(color.red("搜索中..."))
	print(color.yellow("+---- 搜索结果：------+"))
	maxArray = getHtml(ins)

	print("\n")
	print(color.yellow("+---- 请阅读以下命令以继续：------+"))
	print(color.red("B(返回搜索)，数字(进入某条搜索结果)，[ctrl]+[c] 退出"))
	typee = input("：")

	if typee == "B":
		runner()
	else:
		if str(int(typee)) == typee:
			# TO DO
			index = int(typee) - 1;
			h3 = maxArray[index].select('h3')[0]

			if maxArray[index] and maxArray[index].select('h3')[0]:
				url = h3.select('a')[0].attrs['href']

				if url:
					openPage(url)


		else:
			runner()


runner()	
