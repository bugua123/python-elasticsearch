from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# PUT / test_index / _doc / 20
# u6fm8BEC1vup8q88hc
# {
#
#     "serial": "版本300",
#     "title": "这是标题bulk2",
#     "content": "这是一段测试文档",
#     "createtime": "2020-01-05",
#     "click": 50,
#     "category": "体育"
#
# }

#更新文档
doc ={"doc":
          {
            "serial": "版本300",
            "title": "这是标题bulk2",
            "content": "这是一段测试文档",
            "createtime": "2020-01-05",
            "click": 50,
            "category": "体育"
           }
}

res=es.update(index="test_index",id="3Eu6fm8BEC1vup8q88hc",doc_type="_doc" ,body=doc)

print(res)
