#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ltdowndoad.py
#  
#  Copyright 2014 Juhnson <juhnson.Guo@Gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import urllib.request 
from bs4 import BeautifulSoup

def pagelist(url):
	list=[]
	html = urllib.request.urlopen(url).read().decode('gbk')
	soup = BeautifulSoup(html,"html.parser")
	for i in soup.find_all("a",attrs={"class": "t14b"}):
		list.append(i['href'])
	return list
	
def jump(url):
	'''
	跳转到小说正文
	'''
	html = urllib.request.urlopen(url).read().decode('gbk')
	soup = BeautifulSoup(html,"html.parser")
	jump_url=soup.find("a",attrs={"id":"htmldianjiyuedu"})['href']
	return(jump_url)
	
def get_txt(url):
	
	list=[]
	html = urllib.request.urlopen(url).read().decode('gbk')
	soup = BeautifulSoup(html,"html.parser")
	for i in soup.find("div",attrs={"id":"htmlList"}).find_all("a"):
		list.append(i['href'])
	print(list)
	
	return 0
	
def main():
#	url = 'http://www.lt89.com/modules/article/index.php?fullflag=1'
#	page=pagelist(url)
#	print(page)
#	url = 'http://www.lt89.com/modules/article/articleinfo.php?id=4708'
#	print(jump(url))
	url = 'http://www.lt89.com/files/article/html/4/4708/index.html'
	get_txt(url)
	return 0

if __name__ == '__main__':
	main()
