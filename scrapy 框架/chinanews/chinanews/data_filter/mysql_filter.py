from . import BaseFilter
from sqlalchemy import  create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

class MysqlFilter(BaseFilter):
    def __init__(self,*args,**kwargs):
        BaseFilter.__init__(self, *args, **kwargs)
        self.table=type(
            self.mysql_table_name,
            (Base,),
            dict(
                __tablename__=self.mysql_table_name,
        id = Column(Integer, primary_key=True),
        hashvalue = Column(String(64), index=True, unique=True),
            )

        )

    def _get_storage(self):
        '''

        :return:
        '''
        enige=create_engine(self.mysql_url)
        Base.metadata.create_all(enige)#创建表
        Session=sessionmaker(enige)
        return Session

    def _save(self,hashvalue):
        '''

        :param hashvalue:
        :return:
        '''
        session=self.storage()
        filter=self.table(hashvalue=hashvalue)
        session.add(filter)
        session.commit()
        session.close()

    def _is_exist(self,hashvalue):
        session=self.storage()
        ret =session.query(self.table).filter_by(hashvalue=hashvalue).first()
        session.close()
        if ret:
            return True
        return False