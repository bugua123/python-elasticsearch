from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

index_text ={
              "serial":"版本1",
              "title":"这是标题",
              "content":"这是一段测试文档",
              "createtime" :"2020-01-05",
            "click":100

                }
es.index(index="test_index",body = index_text)
