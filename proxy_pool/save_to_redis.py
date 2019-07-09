from storage_model import RedisClient
from get_model import Crawler

max_count=1000

class Getter(object):
    def __init__(self):
        self.redis=RedisClient()
        self.crawler=Crawler()

    def is_over(self):
        if self.redis.count() >=max_count:
            return True
        else:
            return False
    def run(self):
        '''
        :return: 调用add方法添加代理到redis
        '''
        if not self.is_over():
            for num in range(self.crawler._CrawCount_):
                callback=self.crawler._CrawlFunc_[num]
                proxies=self.crawler.get_profies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
if __name__ == '__main__':
    get=Getter()
    get.run()