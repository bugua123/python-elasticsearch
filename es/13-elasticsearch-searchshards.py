from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

#查询对搜索请求执行的索引和分片

res=es.search_shards("test_index")
print(res)