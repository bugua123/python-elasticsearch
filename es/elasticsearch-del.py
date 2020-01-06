from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# #删除索引
# result = es.indices.delete(index='test_index', ignore=[400, 404])
# print(result)

#删除一条数据
#id 查询出实际id 替换
res = es.delete(index="test_index", id ="1pmoeW8BTLJAn2cX6Rul")
print(res)