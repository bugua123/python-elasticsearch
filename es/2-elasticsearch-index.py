from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# #创建索引
# result = es.indices.create(index='test_index', ignore=400)
# print(result)

#索引mapping

_index_mappings = {
    'mappings': {
        '_source': {
            'enabled': True
        },
        'properties': {
            'id': {
                'type': 'long',
                'index':'false'
            },
            'click': {
                'type': 'int',

            },
            'title': {
                'type': 'text'
            },
            'content': {
                'type': 'text'
            },
            "serial": {
                "type": "keyword",  # keyword不会进行分词,text会分词
                 "index": "false"  # 不建索引
            },
            "createtime": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
        }
    }
}
if es.indices.exists(index="test_index") is not True:
    result = es.indices.create(index='test_index', body = _index_mappings ,ignore=400)
    print(result)
else:
    print("index 已存在")




# #删除索引
# result = es.indices.delete(index='test_index', ignore=[400, 404])
# print(result)
