from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# #根据id 查询数据
# res=es.get(index='test_index',id='2JmpeW8BTLJAn2cXohup')
# print(res)
#
# #查询所有数据
# res=es.search(index='test_index')
# print(res)
#
# print(res['hits']['hits'])
# # 通过['hits']参数，可以解析出查询数据的详细内容
# # 根据实际情况进行解析



#查询所有数据

doc={
    "query": {
        "match_all": {}
    }
}

res = es.search(index='test_index', size=20, body =doc )
print(res)


#根据条件查找
# doc = {
#             "query": {
#                 "match": {
#                     "_id": "2pmzeW8BTLJAn2cXQBvc"
#                 }
#             }
#         }
#
#
# res = es.search(index="test_index",body=doc)
# print(res)
# print(res['hits']['hits'])