MAX_SCORE=100
MIN_SCORE=0
INIT_SCORE=10
HOST='localhost'
PORT='6379'
PASSWORD=None
KEY='proxy'

import redis
from  random import choice

class RedisClient(object):
    def __init__(self,host=HOST,port=PORT,password=PASSWORD):
        '''
        :param host:
        :param port:
        :param password:
        '''
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INIT_SCORE):
        '''
        :param proxy:
        :param score:
        :return 返回添加后结果:
        '''
        if not self.db.zscore(KEY,proxy):
            return self.db.zadd(KEY,{proxy:score})

    def random(self):
        """
        :return 返回一个代理:
        """
        result=self.db.zrangebyscore(KEY,MAX_SCORE,MIN_SCORE)
        if len(result):
            return choice(result)
        else:
            result=self.db.zrevrange(KEY,0,100)
            if len(result):
                return choice(result)
            else:
                return None

    def decrease(self,proxy):
        '''

        :param proxy:
        :return:对代理进行分值计算
        '''
        score=self.db.zscore(KEY,proxy)
        if score and score >MIN_SCORE:
            print('代理：',proxy,'当前分数为：',score,'减去1')
            return self.db.zincrby(KEY,-1,proxy)
        else:
            print('代理：', proxy, '当前分数为：', score, '移除')
            return self.db.zrem(KEY, proxy)

    def exists(self,proxy):
        '''

        :param proxy:
        :return:返回一个bool值
        '''
        return  not self.db.zscore(KEY,proxy) == None

    def batch(self, start, stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(KEY, start, stop - 1)

    def max(self,proxy):
        '''

        :param proxy:
        :return:
        '''
        print('代理可用，将其设置为：',MAX_SCORE)
        return self.db.zadd(KEY,{proxy:MAX_SCORE})

    def count(self):
        '''

        :return:返回当前代理池内代理数量
        '''
        return self.db.zcard(KEY)

    def all(self):
        return  self.db.zrangebyscore(KEY,MIN_SCORE,MAX_SCORE)


if  __name__ == '__main__':
    r=RedisClient()
    print(r.random(),r.count())