from data_filter.memory_filter import MemoryFilter
data=['a','1','c','a','1']

m_obj=MemoryFilter()
for i in data:
    if  m_obj.is_exist(i):
        print('数据重复',i)
    else:
        m_obj.save(i)
        print('保存数据',i)


