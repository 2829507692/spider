from data_filter.mysql_filter import MysqlFilter
data=['a','asdf','c','a','asdf','adfd','fdab']

# mysql_url='mysql+pymysql://root:password@localhost:3306/db_name?charset=utf8'
mysql_url='mysql+pymysql://root:123456@localhost:3306/filter?charset=utf8'
m_obj=MysqlFilter(mysql_url=mysql_url)

for  i in data:
    if  m_obj.is_exist(i):
        print('数据已存在',i)
    else:
        m_obj.save(i)
        print('添加数据',i)