from mitmproxy import ctx
import json
import pymongo
#client = pymongo.MongoClient
#db=client['app']
#collection=db['igetebook']

def response(flow):
    url='https://entree.igetget.com/label/navigation/content'
    if flow.request.url==url:
        flow.apparent_encoding='utf-8'
        text=flow.response.text
        data = json.loads(text)
        books=data.get('c').get('list')
        for book in books:
            data ={
                    'item_type':book.get('item_type'),
                    'product_id':book.get('product_id'),
                    'name':book.get('name'),
                    'intro':book.get('intro'),
                    'img':book.get('index_img'),
                    'author_list':book.get('author_list')
                    }
            print(str(data))

