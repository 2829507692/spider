from data_filter.redis_filter import RedisFilter
data=['a','nad','c','a','nad']
r=RedisFilter()
for i in  data:
    if r.is_exist(i):
        print('数据重复',i)
    else:
        r.save(i)
        print('保存数据',i)