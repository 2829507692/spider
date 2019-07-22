##基于信息摘要算法实现去重和存储
import hashlib
import six

class BaseFilter(object):
    def __init__(self,func_name='md5',
                 redis_host='localhost',
                 redis_port=6379,
                 redis_db=0,
                 redis_key='filter',
                 mysql_url=None,
                 mysql_table_name='filter'):
        self.redis_host=redis_host
        self.redis_port=redis_port
        self.redis_db=redis_db
        self.redis_key=redis_key
        self.mysql_url=mysql_url
        self.mysql_table_name=mysql_table_name
        self.hash_func=getattr(hashlib,func_name)
        self.storage=self._get_storage()

    def safe_data(self,data):
        '''
        对数据进行处理
        :param data:
        :return: 返回处理后的字符串
        '''
        if six.PY3:
            if isinstance(data,bytes):
                return data
            elif isinstance(data,str):
                return data.encode()
            else:
                raise Exception('请传入一个字符串')
        else:
            if isinstance(data,str):
                return data
            elif isinstance(data,unicode):
                return data.encode()
            else:
                raise Exception('请传入一个字符串')

    def get_hash(self,data):
        '''
        :param data:
        :return:返回指纹
        '''
        hash_obj=self.hash_func()
        hash_obj.update(self.safe_data(data))
        hash_value=hash_obj.hexdigest()
        return hash_value

    def save(self,data):
        '''
        调用get_hash(data)方法，得到一个hash值,
        :param data:
        :return:返回存储结果
        '''
        hashvalue=self.get_hash(data)
        return  self._save(hashvalue)


    def is_exist(self,data):
        '''

        :param data:
        :return:返回判断结果
        '''
        hashvalue=self.get_hash(data)
        return self._is_exist(hashvalue)

    def _save(self,hashvalue):
        '''让子类进行重写
        :param hashvalue:
        :return:
        '''
        pass

    def _is_exist(self,hashvalue):
        '''
        让子类进行重写
        :param hashvalue:
        :return:
        '''
        pass

    def _get_storage(self):
        pass