#coding=utf-8
import sys
import math
reload(sys)
sys.setdefaultencoding('utf8')

#统计每个单词的词频
def tf(term, doc, normalize):
    if len(doc) == 0:
        return 0
    else:
        if normalize:
            return doc.count(term) / float(len(doc))
        else:
            return doc.count(term) / 1.0

for i in range(1,8):
    f = open('output%d.txt'%i,'r')
    str = f.read().split()
    f.close()
    dicta = { }
    total = 0
    #print str
    for each in str:
        #print each
        if dicta.has_key(each):
            pass
        else:
            dicta[each] = tf(each,str,False)
            total += dicta[each]


    fout = open('wordentropy%d.txt'%i,'w')
    for (k,v) in dicta.items():
        #print '%s:%s' %(k, v)
        p = v/total     #每个词在评论集合中出现的概率
        h = -p*(math.log(p))   #信息熵
        fout.write('%s     %s' %(k, h))     #这里暂时不考虑精度问题
        fout.write('\n')

    fout.close()