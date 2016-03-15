#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#先把词的信息熵信息保存到一个字典中
f1 = open('wordentropy7.txt','r')
dicta = { }
lines = f1.readlines()
for eachline in lines:
    key, value = eachline.split()
    dicta[key] = value

#for (k, v) in dicta.items():
    #print '%s %s'%(k, v)

#将句子的熵数据保存在文件中
f2 = open('output7.txt','r')
lines = f2.readlines()
print len(lines)     #可以据此验证最后存储的句子的熵信息是否完整
f2.close()
fout = open('sen_entropy7.txt','w')
i = 0
for eachline in lines:
    sentropy = 0
    i += 1
    wordlist = eachline.split()
    for word in wordlist:
        if dicta.get(word) == None:
            pass
        else:
            sentropy += float(dicta[word])   #之前直接用dicta[word]会产生keyerror,找不到相应的键就会报错，所以用dict.get()来判断是否存在
    fout.write('%s  %s'%(i, sentropy))
    fout.write('\n')

fout.close()


