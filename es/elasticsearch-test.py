from elasticsearch import Elasticsearch

# 精简连接
es = Elasticsearch(['127.0.0.1:9200'])
# es = Elasticsearch([{'host':'192.168.1.110','port':9200}])

# 动态连接
# es = Elasticsearch(
#     ['one:port', 'tow:port'],
#     # 在做任何操作之前，先进行嗅探
#     sniff_on_start=True,
#     # 节点没有响应时，进行刷新，重新连接
#     sniff_on_connection_fail=True,
#     # 每 60 秒刷新一次
#     sniffer_timeout=60
# )




# es = Elasticsearch(
#     ['192.168.1.110', '192.168.1.111', '192.168.1.112'],  # 连接集群，以列表的形式存放节点的ip地址
#     sniff_on_start=True,  # 连接前测试
#     sniff_on_connection_fail=True,  # 节点无响应时刷新节点
#     sniff_timeout=60    # 设置超时时间
# )


#对不同的节点赋值不同参数
# es = Elasticsearch([
#     {'host': 'localhost'},
#     {'host': 'secondhost', 'port': 9200, 'url_prefix': 'es', 'use_ssl': True},
# ])


#ssl 方式连接
# es = Elasticsearch(
#     ['localhost:443', 'other_host:443'],
#     #打开SSL
#     use_ssl=True,
#     #确保我们验证了SSL证书（默认关闭）
#     verify_certs=True,
#     #提供CA证书的路径
#     ca_certs='/path/to/CA_certs',
#     #PEM格式的SSL客户端证书
#     client_cert='/path/to/clientcert.pem',
#     #PEM格式的SSL客户端密钥
#     client_key='/path/to/clientkey.pem'
# )


# 打印集群健康状况
print(es.cluster.health())
#打印集群状态
print(es.cluster.stats())

#打印连接的集群节点信息
print(es.cluster.client.info())