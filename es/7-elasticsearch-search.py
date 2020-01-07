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

# doc={
#     "query": {
#         "match_all": {}
#     }
# }
#
# res = es.search(index='test_index', size=20, body =doc )
# print(res)


#根据id查找
doc = {
            "query": {
                "match": {
                    "_id": "2pmzeW8BTLJAn2cXQBvc"
                }
            }
        }


res = es.search(index="test_index",body=doc)
print(res)
print(res['hits']['hits'])



#等于查询 term与terms, 查询 name='这是标题' 这个值不会分词必须完全包含
doc={
    "query":{
        "term":{
            "title":"这是标题"
        }
    }
}
res=es.search(index='test_index',size=20,body=doc)
print(res)


#等于查询 term与terms, 查询 title='这是标题' 或 name='这是标题2'
doc={
    "query": {
        "terms": {
            "title": ["这是标题","这是标题2"]
        }
    }
}
res = es.search(index= 'test_index', size= 20, body= doc)
print(res)

# match: 匹配title包含"标题"关键字的数据, 会进行分词包含 或者 的
doc={
    "query": {
        "match": {
            "title": "标题"
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)
print(res)


#multi_match: 在title或content里匹配包含 这 的关键字的数据
doc={
    "query": {
        "multi_match": {
            "query": "这",
            "fields": ["title", "content"]
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)
print(res)


#查询id 1 2 的数据
doc={
    "query":{
        "ids":{
            "values":["1","2"]
        }
    }
}
res=es.search(index="test_index",size=20,body=doc)
print(res)

# 复合查询bool , bool有3类查询关系，must(都满足),should(其中一个满足),must_not(都不满足)

doc={
    "query":{
        "bool":{
            "must":[
                {
                    "term":{
                        "title":"这是标题",
                    }
                },
                {
                    "term":{
                        "content":"这是一段测试文档",
                    },
                },
            ]
        }
    }
}
res=es.search(index="test_index",size=20,body=doc)
print(res)

doc={
    "query": {
        "bool": {
            "should": [
                {
                    "term": {
                        "title": "标题",
                    },

                },
                {
                    "term": {
                        "content": "文档",
                    },

                },
            ]
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)

#切片式查询

doc={
    "query": {
        "bool": {
            "should": [
                {
                    "term": {
                        "title": "标题",
                    },

                },
                {
                    "term": {
                        "content": "文档",
                    },

                },
            ]
        }
    },
    "from": 2, #从第二条数据开始
    "size": 4, # 获取4条数据
}

res = es.search(index='test_index', size=20, body=doc)
print(res)

#范围查询
doc={
    "query": {
        "range": {
            "age": {
                "gte": 18, #>=18
                "lte": 30  #<=30
            }
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)
print(res)

#前缀查询
doc={
    "query": {
        "prefix": {
            "title": "这"
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)
print(res)

#通配符查询
doc={
    "query": {
        "wildcard": {
            "title": "*标题"
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)
print(res)

#排序
doc={
    "query": {
        "wildcard": {
            "title": "标题*"
        }
    },
    "sort": {
        "createtime": {
            "order": "desc" #降序
        }
    }
}

res = es.search(index='test_index', size=20, body=doc)
print(res)

# count, 执行查询并获取该查询的匹配数
c = es.count(index='test_index')
print(c)

# 短语匹配 match_phrase (搜索is a little的短语,不进行切分)
doc={
    "query": {
        "match_phrase": {
            "title": "这是标题"
        }
    }
}
res = es.search(index='test_index', size=20, body=doc)
print(res)


# from、size
#from：从“第几条”开始查询, size：查询多少条
doc={
    "query": {
        "match_all": {}
    },
    "size": 1,
    "from": 2
}
res = es.search(index='test_index', body =doc )
print(res)

#range 范围查找
doc={
  "query": {
    "range": {
      "click": {
        "gt": 30,
        "lt": 60
      }
    }
  }
}

res=es.search(index="test_index",body=doc)
print(res)

# Highlight Search(高亮检索)
# doc={
#     "query": {
#         "match": {"title": "标题"}
#     },
#     "from": 0,
#     "size": 1,
#     "highlight": {
#         "fields": {"title": {}}
#     },
#     "_source": ["title", "content"]
# }
# res=es.search(index="test_index",body=doc)
# print(res)

#范围查询（range query）
doc={
  "query": {
    "range": {
      "click": {
          "lte": 60

      }
    }
  }
}
res=es.search(index="test_index",body=doc)
print(res)

#多字段查询
doc={
    "query": {
        "bool": {
            "should": [
                { "match": { "title": "bulk" }},
                { "match": { "category":  "新闻" }}
            ]
        }
    }
}
res=es.search(index="test_index",body=doc)
print(res)

#dis_max只取某一个query最大的分数，完全不考虑其他query的分数
doc={
    "query": {
      "dis_max": {
            "queries": [
                { "match": { "title": "bulk" }},
                { "match": { "category":  "新闻" }}
            ]
        }
    }
}
res=es.search(index="test_index",body=doc)
print(res)

#使用tie_breaker将其他query的分数也考虑进去
doc={
    "query": {
        "dis_max": {
            "queries": [
              {"match": {"title": "bulk"}},
              {"match": {"category": "新闻"}}
            ],
            "tie_breaker": 0.5
        }
    }
}
res=es.search(index="test_index",body=doc)
print(res)