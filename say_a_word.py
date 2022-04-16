"""
topic: 单词朗读软件
运行： streamlit run say_a_word.py
"""
import streamlit as st
import pyttsx3
import pandas as pd
import time
import os

class readwords(object):
	def __init__(self):
		# 初始化
		st.set_page_config(page_title="say_a_word", layout="wide")
		
	def readwords(self):
		# 输入单词列表名称
		index = st.radio(
			'chose words list',(
				'高考核心985词汇',
				'大学四级3500词汇',
				'四六级600重点词汇'
				))
		# 栏目选择
		if index == '大学四级3500词汇':
			filename = 'collage4Words.csv'
		elif index == '四六级600重点词汇':
			filename = 'collage46Words.csv'
		elif index == '高考核心985词汇':
			filename = 'highschool985Words.csv'
		# CSV读入单词列表
		c46 = pd.read_csv('wordlists/'+filename)
		st.write(f'总共用{c46.shape[0]}个单词')
		# 输入起始位置
		startnum = st.number_input("输入从第几个单词开始")
		endnum = st.number_input("输入到第几个单词结束")
		if startnum > endnum:
			startnum = 1
		if startnum <= 0:
			startnum =1
		if endnum > c46.shape[0]:
			endnum = c46.shape[0]
		if st.button("提交"):
			num = endnum - startnum
			st.write(f'总共{num+1}个单词，预计需要{int((num*38)/600)}分钟')
			start = time.time()
			self.toSpeake(c46, int(startnum-1), int(endnum))
			end = time.time()
			st.write(f'总共用时{int((end-start)/60)}分钟')

	def toSpeake(self, c46, startnum, endnum):
		# 初始化
		engine = pyttsx3.init()
		# 显示并朗读
		for i in range(startnum,endnum):
			w1 = c46.loc[i, 'item']
			engine.say(w1)
			engine.runAndWait()
			# 显示英文
			c1, c2, c3 = st.columns(3)
			with c1:
				st.header(w1)
				engine.say(w1)
				engine.runAndWait()
			# 显示翻译
			with c2:
				w2 = c46.loc[i, 'translate']
				st.write(f'...   {i+1}   ...')
				st.write(w2)
			time.sleep(0.3)
		# 关闭播音
		engine.stop()

if __name__ == '__main__':
	rw = readwords()
	rw.readwords()
