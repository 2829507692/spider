import pymongo
from bson.objectid import ObjectId
mongo=pymongo.MongoClient()
db=mongo.taobao
collection=db.info
# s=collection.insert_one({
#     'name':'erha'
# })
# print(s.inserted_id)
# ss=collection.find({'_id':ObjectId('5cf8e59cd974302111fdd0c7')})
# print(ss.next())
# result=collection.find({'location':{'$regex':'^上'}}).sort('deal',pymongo.ASCENDING).skip(3)
# result=collection.find({'price':{'$in':[20,30]}})
result=collection.find()
# result=collection.find({'name':{'$type':'string'}})
# result=collection.find()
# for index,i in enumerate(result):
#     coditin={'name':{'$type':'string'}}
#     i['age']=index
#     # collection.update(coditin,i)
#     collection.update(coditin,{'$set':i})

