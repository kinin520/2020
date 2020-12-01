#打开并读取函数
file=open(r'D:\Walden.txt', 'r')
lines=file.readlines()
lines
words=[]

for line in lines:
    tmp_list=line.split(" ")#print((line.split(""))
    for word in tmp_list:
        words.append(word)#words.append(tmp_list)
#对word中每个元素计算他出现的个数
#把统计结果保存到字典中，字典的key是单词，value是单词出现的次数
word_count={}
word_set=set(words)
for word in word_set:
    count_nun=words.count(word)
    word_count[word]=count_num
#对word_count字典进行排序，按照出现的次数（value）进行降序排序
sorted(word_count.items(),key=lambda item:item[1],reverse=True)
