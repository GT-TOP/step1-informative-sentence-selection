#coding=utf-8
import sys
import jieba
reload(sys)
sys.setdefaultencoding('utf8')

#删除爬取的原始评论中的空行
def delete_enter(inputFile, outputFile):
    fin = open(inputFile,'r')
    fout = open(outputFile,'w')
    lines = fin.readlines()
    for eachline in lines:
        line = eachline.strip()
        if line != '':
            fout.write(line + '\n')
    fin.close()
    fout.close()

#中文分词
def filter_stopword(inputFile, outputFile):
    with open('stopword.txt','r') as f:
        stopwords = f.read()
        print stopwords
    fin = open(inputFile, 'r')		  #以读的方式打开文件
    fout = open(outputFile, 'w')		  #以写的方式打开文件

    for eachLine in fin:
        if eachLine != '\n':      #去除评论文本中的空行
            line = eachLine.strip().decode('utf8', 'ignore')  #去除每行首尾可能出现的空格，并转为Unicode进行处理,ignore忽略非法字符
            wordList = list(jieba.cut(line))	 #用结巴分词，对每行内容进行分词
            outStr = ''
            for word in wordList:
                if word not in stopwords:
                    outStr += word
                    outStr += ' '
            fout.write(outStr.strip().encode('utf8') + '\n') #将分词好的结果写入到输出文件
    fin.close()
    fout.close()

for i in range(1,8):
    delete_enter('location%d.txt'%i,'location%d_1.txt'%i)
    filter_stopword('location%d_1.txt'%i,'output%d.txt'%i)