import math
from operator import *

import pandas as pd

rating = pd.read_csv(r'C:\\Users\\Administrator\\Desktop\\movie-data\\ml-latest-small\\ratings.csv')
#ratings.csv's columns are user,movieId,rating,timestamp
user = rating['userId']
movieId = rating['movieId']
rating1 = rating['rating'] #人对电影的评分
timestamp = rating['timestamp'] #打分的时间
user_item = dict()#构造一个字典，格式{userid:[movieid,movieid],……}因为一个人会看多部电影
for i in range(len(user)):
    if user[i] not in user_item:
        user_item[user[i]] = set()
        user_item[user[i]].add(movieId[i])
item_user = dict()#建立物品——用户的倒排表，为了降低表的稀疏性
for i in range(len(user)):
    if movieId[i] not in item_user:
        item_user[movieId[i]] = set()#set结构可以看成一个不重复的数组
    item_user[movieId[i]].add(user[i])
N = dict()#计数，看看每个电影被看了多少次
C = dict()#得出两个物品同时被一个用户看的次数
for i,items in item_user.items():
    for item in items:
        if item not in N:
            N[item] = 0
        N[item]+=1
        for item2 in items:
            if item ==item2:
                continue
            if (item, item2) not in C:
                C[item,item2] = 0
            C[item,item2]+=1
w = dict()#通过C（1,2）/N[1]*N[2] 算出系数表，等于把物品的关联程度算出来啦;如果想加上时间的因素，就用log加入
for i ,item in C.items():
    w[i[0],i[1]] = C[i[0], i[1]]/math.sqrt(N[i[0]] * N[i[1]] *1.0)
rank = dict()#推荐列表
target_user = 1   #input("write the user you want to recommand:")
train = user_item[target_user]
ralated_item = dict()
for i in w:
    if i[0] in train and i[1] not in train:#找出同时出现的两部电影，两部电影有1部被target-user看过
        if i[1] not in ralated_item:
            ralated_item[i[1]] = 0
        ralated_item[i[1]] = w[i[0],i[1]]
print(sorted(ralated_item.items(), key = itemgetter(1), reverse=True)[:10])#打印出前十的。