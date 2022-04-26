"""
topic: 单词朗读软件
运行： streamlit run say_a_word.py
"""
import streamlit as st
import pyttsx3
import csv
import time
import os
import random

class readwords(object):
	def __init__(self):
		# 初始化
		st.set_page_config(page_title="say_a_word", layout="wide")
		
	def readwords(self):
		# 输入单词列表名称
		index = st.radio('',(
				'高考核心983词汇',
				'大学四级3641词汇',
				'四六级580重点词汇'
				))
		# 栏目选择
		if index == '大学四级3641词汇':
			filename = 'collage4Words.csv'
		elif index == '四六级580重点词汇':
			filename = 'collage46Words.csv'
		elif index == '高考核心983词汇':
			filename = 'highschool985Words.csv'
		# CSV读入单词列表
		with open(filename, encoding='utf-8') as f:
			reader = csv.reader(f)
			c46 = []
			for row in reader:
				c46.append(row)
		# 输入起始位置
		c1, c2 = st.columns(2)
		with c1:
			startnum = st.text_input("从第几个单词开始")
		with c2:
			endnum = st.text_input("到第几个单词结束")
		# 防误数据过滤
		if startnum == '':
			startnum = 1 
			tag1 = 1
		else:
			startnum = int(startnum)
			tag1 = 0
		if endnum == '':
			endnum = len(c46)
			tag2 = 1
		else:
			endnum = int(endnum)
			tag2 = 0
		tag = tag1 + tag2
		if startnum > endnum:
			startnum = 1
		if startnum <= 0:
			startnum =1
		if endnum > len(c46):
			endnum = len(c46)
		num = endnum - startnum
		st.write(f'总共{num}个单词，预计需要{int((num*38)/600)}分钟')
		start = time.time()
		# 提交数据并阅读
		if st.button("提交"):
			if tag == 0:
				for i in range(startnum,endnum):
					self.toSpeake(c46, i)
			if tag > 0:
				list =[]
				for j in range(startnum,endnum):
					list.append(j)
					num = endnum - startnum
				for i in random.sample(list,k=num):
					self.toSpeake(c46, i)
			end = time.time()
			st.write(f'总共用时{int(end-start)}秒')

	def toSpeake(self, c46, i):
		# 初始化
		# engine = pyttsx3.init()
		# 显示并朗读
		w1 = c46[i][0]
		# 显示英文
		c1, c2 = st.columns(2)
		with c1:
			st.header(w1)
			# engine.say(w1)
			# engine.runAndWait()
			time.sleep(1)
		# 显示翻译
		with c2:
			w2 = c46[i][1]
			st.write(f'...   {i}   ...')
			time.sleep(0.7)
			st.write(w2)
		time.sleep(0.3)
		# 关闭播音
		# engine.stop()

if __name__ == '__main__':
	rw = readwords()
	rw.readwords()