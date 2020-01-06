from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

#获取点击最大值
doc={
    "query": {
        "match_all": {}
    },
    "aggs": {
        "min_age": {
            "min": {
                "field": "click"
            }
        }
    }
}

res = es.search(index='test_index', size=20, body=doc)
print(res)
print(res['aggregations']['min_age']['value'])



#获取点击最小值

doc={
    "query": {
        "match_all": {}
    },
    "aggs": {
        "max_age": {
            "max": {
                "field": "click"
            }
        }
    }
}

res = es.search(index='test_index', body = doc)
print(res['aggregations']['max_age']['value'])

#获取总点击数
res = es.search(index='test_index', body = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "sum_age": {
            "sum": {
                "field": "click"
            }
        }
    }
})
print(res['aggregations']['sum_age']['value'])

#获取平均点击数
res = es.search(index='test_index', body = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "avg_age": {
            "avg": {
                "field": "click"
            }
        }
    }
})
print(res['aggregations']['avg_age']['value'])

