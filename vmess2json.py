import json

str = '{"v":2,"ps":"订阅·请连接此节点再更新订阅·动态IP·空闲·不限流量·10M","add":"rssd1.w-zo.com","port":443,"id":"6374b87e-8c72-489a-b675-3ba8992e98ad","aid":0,"host":"rssd1.w-zo.com","net":"ws","type":"none","path":"/z90","tls":"tls"}'
j = json.loads(str)
with open("/home/wyk/Code/front-end/test.json", "w+") as f:
    json.dump(j, f, ensure_ascii=False)

def toJson(str):
    j = json.loads(str)
    with open("/home/wyk/Code/front-end/test.json", "w+") as f:
        json.dump(j, f, ensure_ascii=False)