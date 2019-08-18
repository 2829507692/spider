from .  import BaseFilter
import redis

class RedisFilter(BaseFilter):
    def _get_storage(self):
        '''
        返回一个redis对象
        :return:
        '''
        pool=redis.ConnectionPool(host=self.redis_host,port=self.redis_port,
                                  db=self.redis_db)
        client=redis.StrictRedis(connection_pool=pool)

        return client

    def _save(self,hashvalue):

        return self.storage.sadd(self.redis_key,hashvalue)#type:redis


    def _is_exist(self,hashvalue):
        return self.storage.sismember(self.redis_key,hashvalue)
