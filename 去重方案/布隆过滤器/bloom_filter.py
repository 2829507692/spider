import hashlib
import six
import redis

'''
基于redis的布隆过滤器
布隆过滤器（Bloom Filter）是1970年由布隆提出的。它实际上是一个很长的二进制向量和一系列随机映射函数。
布隆过滤器可以用于检索一个元素是否在一个集合中。
它的优点是空间效率和查询时间都比一般的算法要好的多，缺点是有一定的误识别率和删除困难。'''

class MultpleHash(object):

    def __init__(self,salts,hash_name='md5'):
        if len(salts)<3:
            raise Exception('请保证salts的长度至少为三')
        self.salts=salts
        self.hash_func=getattr(hashlib,hash_name)

    def safe_data(self, data):
        '''
        对数据进行处理
        :param data:
        :return: 返回处理后的字符串
        '''
        if six.PY3:
            if isinstance(data, bytes):
                return data
            elif isinstance(data, str):
                return data.encode()
            else:
                raise Exception('请传入一个字符串')
        else:
            if isinstance(data, str):
                return data
            elif isinstance(data, unicode):
                return data.encode()
            else:
                raise Exception('请传入一个字符串')


    def get_hash_value(self,data):
        hash_value_list=[]
        for salt in self.salts:
            hash_obj=self.hash_func()
            hash_obj.update(self.safe_data(data))
            hash_obj.update(self.safe_data(salt))
            hash_value=hash_obj.hexdigest()
            hash_value_list.append(int(hash_value,16))
        return hash_value_list

class BloomFilter(object):
    def __init__(self,salts,redis_host='127.0.0.1',redis_port=6379,redis_db=5,
                 redis_key='bloom',
                 ):
        self.redis_host=redis_host
        self.redis_port=redis_port
        self.redis_db=redis_db
        self.redis_key=redis_key
        self.MultpleHash=MultpleHash(salts)

    def get_redis_client(self):
        '''
        返回一个redis连接对象
        :return:
        '''
        pool=redis.ConnectionPool(host=self.redis_host,port=self.redis_port,
                                  db=self.redis_db)
        client=redis.StrictRedis(connection_pool=pool)

        return client

    def save(self,data):
        '''
        set offset and value in redis string
        :param data:
        :return:
        '''
        for value in self.MultpleHash.get_hash_value(data):
            offset=self.get_offset(value)
            self.get_redis_client().setbit(self.redis_key,offset,1)
        return True

    def is_exists(self,data):
        '''
        judge the value whether exists in redis string
        :return:
        '''
        value_list=[]
        for value in self.MultpleHash.get_hash_value(data):
            offset=self.get_offset(value)
            value=self.get_redis_client().getbit(self.redis_key,offset)
            value_list.append(value)
        if 0 in value_list:
            return False
        return True


    def get_offset(self,value):
        '''
        :param value:
        :return:
        '''
        return value%(2**7*2**20*2**3)


if __name__ == '__main__':
    bf=BloomFilter(['1','2','3'])
    data =['asd','31','14','65','12','14']
    for da in data:
        if bf.is_exists(da):
            print('发现重复数据',da)
        else:
            bf.save(da)
            print('保存数据',da)