'''
解码订阅地址
一个订阅地址范例:
https://xbrss.com/rss/BenxLTA/CYfxZc?net_type=VMESS
输入浏览器得到的westworld.txt,即为订阅地址的base64加密结果
''' 

import base64
import re
import json
file = open('/home/wyk/Code/front-end/westworldss.txt')

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

def toJson(strs):
    for str in strs:
        j = json.loads(str)
        with open("/home/wyk/Code/front-end/test.json", "a") as f:
            json.dump(j, f, indent=4, sort_keys=True ,ensure_ascii=False)
            f.write(',\n')
    f.close()

# s = 'dm1lc3M6Ly9leUpoWkdRaU9pSm9hMlkxTURndWQzZGhjREV1WTI5dElpd2lZV2xrSWpvd0xDSm9iM04wSWpvaWFHdG1OVEE0TG5kM1lYQXhMbU52YlNJc0ltbGtJam9pTXpSaFltTXdPRFF0WWpsaVppMW1NalZtTFRGak5XRXRObVUyWmpBeE5qVTFaRGRqSWl3aWJtVjBJam9pZDNNaUxDSndZWFJvSWpvaUwyUjFhQ0lzSW5CdmNuUWlPakUyT0RBeExDSndjeUk2SXVtcm1PbUFuOEszNmFhWjVyaXZTRXZDdDA4eU1qVEN0K2VwdXVtWHNzSzNNZVdBamNLMzZJeUM1WkNONUxpdDZMMnM1THlZNVl5V3dyY3hNREF3VFNJc0luUnNjeUk2SW5Sc2N5SXNJblI1Y0dVaU9pSnViMjVsSWl3aWRpSTZNbjA9'
subs = file.read() + "=="
file.close()
byteSubs = base64.b64decode(subs)
urls = byteSubs.decode("utf-8")
# print (urls)
fileOut = open('/home/wyk/Code/front-end/westworldSubs.txt', "w+")
fileOut.write(urls)
fileOut.close()

file2 = open('/home/wyk/Code/front-end/westworldSubs.txt')
vmesses = []
curLine = file2.readline()
while curLine:
    # print(curLine)
    temp = curLine[8:]
    vmesses.append(temp)
    curLine = file2.readline()
file2.close()
# 此时已获得所有vmess链接，且已经过预处理，去掉前缀和换行符
# print(vmesses)
# 对所有vmess进行decode
vmessesDecode1 = []

for s in vmesses:
    temp = base64.b64decode(s)
    t = str(temp, encoding="utf-8")
    vmessesDecode1.append(t)
# print (vmessesDecode1)

fileOut2 = open('/home/wyk/Code/front-end/westworldSubHans.txt', "w+")
final = ""
for s in vmessesDecode1:
    fileOut2.write(s)
toJson(vmessesDecode1)
fileOut2.close()