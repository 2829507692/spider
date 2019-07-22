#计算单个数据的simhash值
import re
from simhash import Simhash
# def get_features(s):
#     width = 3
#     s = s.lower()
#     s = re.sub(r'[^\w]+', '', s)
#     print(s)
#     ret= [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]
#     print(ret)
#     return ret
#
# print ('%x' % Simhash(get_features('How are you? I am fine. Thanks.')).value)
# print ('%x' % Simhash(get_features('How are u? I am fine.     Thanks.')).value)
# print ('%x' % Simhash(get_features('How r you?I    am fine. Thanks.')).value)



##比较两个数据simhash值的距离
# print(Simhash('aa').distance(Simhash('bb')))
# print (Simhash('aa').distance(Simhash('aa')))




####
import re
from simhash import Simhash, SimhashIndex
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

data = {
    1: u'How are you? I Am fine. blar blar blar blar blar Thanks.',
    2: u'How are you i am fine. blar blar blar blar blar than',
    3: u'This is simhash test.',
}
objs = [(str(k), Simhash(get_features(v))) for k, v in data.items()]

index = SimhashIndex(objs, k=0)#设置判断距离，k数字越小，两者差异越小

print (index.bucket_size())##data字典数据长度

####判断传入的数据与已经存在的数据哪一个最相近
s1 = Simhash(get_features(u'How are you i am fine. blar blar blar blar blar thank'))
print (index.get_near_dups(s1))

index.add('4', s1)#将数据添加到data字典中，‘4’为key
print (index.get_near_dups(s1))