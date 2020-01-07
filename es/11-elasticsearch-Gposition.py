from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])


#地理位置

#建立包含地理位置的索引
_index_mappings={
    "mappings":{
        "properties":{
            "address":{
                "type":"text"
            },
            "location":{
                "type":"geo_point"
            }
        }
    }
}

if es.indices.exists(index="test_index_position") is not True:
    result = es.indices.create(index='test_index_position', body = _index_mappings ,ignore=400)
    print(result)
else:
    print("index 已存在")


#插入文档格式1
doc={
  "address": "家庭地址1",
  "location": "41.12,-71.34"

}
res=es.index(index="test_index_position",body=doc)
print(res)
#插入文档格式2
doc={
  "address": "家庭地址2",
  "location": {
	"lat": 41.12,
	"lon": -71.34
  }
}
res=es.index (index="test_index_position",body=doc)
print(res)
#插入文档格式3
doc={
    "address": "家庭地址3",
    "location": [ -73.983, 40.719 ]
}
res=es.index (index="test_index_position",body=doc)
print(res)

doc={
    "query": {
    "geo_bounding_box":{
    "location": {
    "top_left":{
		 "lat": 42,
		 "lon": -72
		},
		"bottom_right":{
		    "lat": 40,
		    "lon": -74
                }
            }
        }
    }
}

res=es.search(index="test_index_position",body=doc)
print(res)


doc={
     "query": {
         "bool": {
             "must": [
                {
                    "match_all": {}
                }
             ],
             "filter": {
                 "geo_distance": {
                     "distance": "200km",
                     "location": {
                         "lat": 40,
                         "lon": -70
                     }
                 }
             }
         }
     }
}
res=es.search(index="test_index_position",size=20,body=doc)
print(res)

doc={
    "size": 0,
    "aggs": {
        "agg_by_distance_range": {
            "geo_distance": {
                "field": "location",
                "origin": {
                    "lat": 40,
                    "lon": -70
                },"unit": "mi",
                "ranges": [
                    {
                        "to": 100
                    },
                    {
                        "from": 100,
                        "to": 300
                    },
                    {
                        "from": 300
                    }
                ]
            }
        }
    }
}
res=es.search(index="test_index_position",size=20,body=doc)
print(res)