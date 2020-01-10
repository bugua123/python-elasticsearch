from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

#简单查询模板的使用


#查询模板
doc={
    "source" : {
      "query": { "match" : { "{{my_field}}" : "{{my_value}}" } },
      "size" : "{{my_size}}"
    },
    "params" : {
        "my_field" : "title",
        "my_value" : "标题",
        "my_size" : 5
    }
}
# res=es.search_template(index="test_index",body=doc)
# print(res)


#建立查询模板
doc={
    "script": {
        "lang": "mustache",
        "source": {
            "query": {
                "match": {
                    "title": "{{query_string}}"
                }
            }
        }
    }
}
# res=es.put_script("search_template",body=doc)
# print(res)

#查询 查询模板
# res=es.get_script("search_template")
# print(res)

#删除查询模板
# es.delete_script("search_template")

#使用模板查询
doc={
    "id":"search_template",
    "params":{
        "query_string":"这是标题"
    }
}
# res=es.search_template(index="test_index",body=doc)
# print(res)


#给模板提供给定参数
doc={
  "source": "{ \"query\": { \"terms\": {{#toJson}}statuses{{/toJson}} }}",
  "params": {
    "statuses" : {
        "status": [ "pending", "published" ]
    }
  }
}

res=es.render_search_template(body=doc)
print(res)