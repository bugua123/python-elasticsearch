from elasticsearch import Elasticsearch
from elasticsearch.helpers import  bulk

es = Elasticsearch(['127.0.0.1:9200'])

#批量插入数据

indexs=[]
index_text ={
              "serial":"版本2",
              "title":"这是标题bulk",
              "content":"这是一段测试文档",
              "createTime" :"2020-01-05",

                }
index_text2 ={
              "serial":"版本3",
              "title":"这是标题bulk2",
              "content":"这是一段测试文档",
              "createTime" :"2020-01-05",

                }
indexs.append(index_text)
indexs.append(index_text2)
res,_=bulk(es,indexs,index='test_index',raise_on_error=True)
print(res)