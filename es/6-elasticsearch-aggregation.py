from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# #获取点击最大值
# doc={
#     "query": {
#         "match_all": {}
#     },
#     "aggs": {
#         "min_age": {
#             "min": {
#                 "field": "click"
#             }
#         }
#     }
# }
#
# res = es.search(index='test_index', size=20, body=doc)
# print(res)
# print(res['aggregations']['min_age']['value'])
#
#
#
# #获取点击最小值
#
# doc={
#     "query": {
#         "match_all": {}
#     },
#     "aggs": {
#         "max_age": {
#             "max": {
#                 "field": "click"
#             }
#         }
#     }
# }
#
# res = es.search(index='test_index', body = doc)
# print(res['aggregations']['max_age']['value'])
#
# #获取总点击数
# res = es.search(index='test_index', body = {
#     "query": {
#         "match_all": {}
#     },
#     "aggs": {
#         "sum_age": {
#             "sum": {
#                 "field": "click"
#             }
#         }
#     }
# })
# print(res['aggregations']['sum_age']['value'])
#
# #获取平均点击数
# res = es.search(index='test_index', body = {
#     "query": {
#         "match_all": {}
#     },
#     "aggs": {
#         "avg_age": {
#             "avg": {
#                 "field": "click"
#             }
#         }
#     }
# })
# print(res['aggregations']['avg_age']['value'])


#查询每个category数量
# doc={
#   "aggs": {
#     "group_by_category": {
#       "terms": { "field": "category" }
#     }
#   }
# }
#
# res=es.search(index="test_index",body=doc)
# print(res)


#查询title中包含“标题的”文档，并计算每个category的数量
doc={
  "size": 0,
  "query": {
    "match": {
      "title": "标题"
    }
  },
  "aggs": {
    "all_category": {
      "terms": {
        "field": "category"
      }
    }
  }
}

res=es.search(index="test_index",body=doc)
print(res)



# 先根据category 分组，在计算平均点击click
doc={
    "size": 0,
    "aggs" : {
        "group_by_category" : {
            "terms" : { "field" : "category" },
            "aggs" : {
                "avg_click" : {
                    "avg" : { "field" : "click" }
                }
            }
        }
    }
}

res=es.search(index="test_index",body=doc)
print(res)


# 先根据category 计算平均click ，然后降序排列
doc={
    "size": 0,
    "aggs" : {
        "all_category" : {
            "terms" : { "field" : "category", "order": { "avg_click": "desc" } },
            "aggs" : {
                "avg_click" : {
                    "avg" : { "field" : "click" }
                }
            }
        }
    }
}

res=es.search(index="test_index",body=doc)
print(res)


doc={
  "size": 0,
  "aggs": {
    "group_by_click": {
      "range": {
        "field": "click",
        "ranges": [
          {
            "from": 0,
            "to": 50
          },
          {
            "from": 50,
            "to": 100
          },
          {
            "from": 100,
            "to": 500
          }
        ]
      },
      "aggs": {
        "group_by_category": {
          "terms": {
            "field": "category"
          },
          "aggs": {
            "average_click": {
              "avg": {
                "field": "click"
              }
            }
          }
        }
      }
    }
  }
}

res=es.search(index="test_index",body=doc)
print(res)