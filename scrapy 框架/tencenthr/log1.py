import logging  # 引入logging模块

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(filename)s->line:[%(lineno)d] : %(message)s')
                    # filename='./log.log',
                    # filemode='a',)  # logging.basicConfig函数对日志的输出格式及方式做相关配置
logger=logging.getLogger(__name__)
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')

if __name__ == '__main__':
    logger.warning('1234')
    logger.warning('你好')