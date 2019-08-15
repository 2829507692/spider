TESTER_CYCLE=20
GETER_CYCLE=20
TESTER_ENABLED=True
GETER_ENABLED=False
API_ENABLED=True
API_HOST='127.0.0.1'
API_PORT='5000'


from multiprocessing import Process
from api_model import app
from save_to_redis import Getter
from test_models import Tester
from time import sleep

class Scheduler():
    def schedule_tetser(self,cycle=TESTER_CYCLE):
        '''
        定时测试代理
        :param cycle:
        :return:
        '''
        tester =Tester()
        while True:
            print('测试器开始工作！！')
            tester.run()
            sleep(cycle)

    def schedule_geter(self,cycle=GETER_CYCLE):
        '''
        定时抓取代理
        :param cycle:
        :return:
        '''
        geter=Getter()
        while True:
            print('开始抓取代理！！')
            geter.run()
            sleep(cycle)

    def schedule_api(self):
        app.run(API_HOST,API_PORT)


    def run(self):
        print('代理池开始工作')
        if TESTER_ENABLED:
            tester_process=Process(target=self.schedule_tetser)
            tester_process.start()
        if GETER_ENABLED:
            getter_process=Process(target=self.schedule_geter)
            getter_process.start()
        if API_ENABLED:
            api_process=Process(target=self.schedule_api)
            api_process.start()

if __name__ == '__main__':
    sc=Scheduler()
    sc.run()