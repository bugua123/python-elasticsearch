from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])


#mget 批量查询 方式1
doc={
   "docs" : [
      {
         "_index" : "test_index",
         "_id" :    "20u6fm8BEC1vup8q88hc"
      },
      {
         "_index" : "test_index",
         "_id" :    "3Eu6fm8BEC1vup8q88hc"
      }
   ]
}
res=es.mget(index="test_index",body=doc)

print(res)

#mget 批量查询 方式2
doc={
    "ids": ["20u6fm8BEC1vup8q88hc", "3Eu6fm8BEC1vup8q88hc"]
}
res=es.mget(index="test_index",body=doc)
print(res)