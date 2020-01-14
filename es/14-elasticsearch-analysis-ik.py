from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

#分词 确保 安装 ik-analyzer 分词插件

#Elasticsearch python 插件中好像没有操作分词的方法，现在展示出 kibana 中 操作

#"analyzer": "ik_smart", 可以根据自己需要选择不同的分词器
# GET /_analyze
# {
#   "text":"我是一名编程人员",
#   "analyzer":"ik_max_word"
# }