class Test(object):
    def __init__(self,V):
	    self.V=V


t1=Test(100)
t2=Test(100)
t3=Test(1000)
t4=t1

data=[t1,t2,t3,t4]
#剔除重复数据
s=set(data)
print(s)

# 剔除重复数据 判断依据为 test对象V相同，则为相同数据
# sign=[]
# datas=[]
# for da in data:
# 	if da.v not in sign:
# 		sign.append(da.v)
# 		datas.append(da)
		
# 剔除重复数据 判断依据为 test对象类相同，则为相同数据
# sign=[]
# datas=[]
# for da in data:
# 	if da.__class__ not in sign:
# 		sign.append(da.__class__)
# 		datas.append(da)
	
