# step1-informative-sentence-selection
从原始评论文本中挑选信息量大的句子
1.ch_cut文件利用结巴分词对评论文本做中文分词及过滤预处理；
2.word_entropy文件计算每个词的信息熵entropy；
3.sentence_entropy文件利用每个词的信息熵来计算句子的熵；
  在此过程中，由于某些占据多行的评论被程序识别为一行，导致最后产生数目的差异
