# coding:utf-8

import json
import pymongo
from mitmproxy import ctx


client = pymongo.MongoClient('localhost')
db = clent['igetget']
collection = db['books']


def response(flow):
    """
    获取响应中的电子书信息
    :param flow:
    :return:
    """
    global collection
    url = 'https://dedao.igetget.com/v3/discover/booklist'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'title':book.get('operation_title'),
                'cover':book.get('cover'),
                'summary':book.get('other_share_summary'),
                'price':book.get('price')
            }
            ctx.log.info(str(data))
            collection.insert(data)


