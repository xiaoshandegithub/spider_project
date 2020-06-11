import json

import requests

url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
cookies_str = 'll="108288"; bid=RF5J95EeLmo; __utma=30149280.879390850.1591794235.1591794235.1591794235.1; __utmc=30149280; __utmz=30149280.1591794235.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1591794235; __utma=223695111.1990881057.1591794245.1591794245.1591794245.1; __utmb=223695111.0.10.1591794245; __utmc=223695111; __utmz=223695111.1591794245.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1591794245%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __yadk_uid=KeUMidBm7xRq0o8siEvwzKA1WEpgcpES; _vwo_uuid_v2=D81292BC03E568CA09221425D7A335276|17f864138a238056c2d7e8c83d714b7d; _pk_id.100001.4cf6=91e31659dfb28db9.1591794245.1.1591794799.1591794245.'
cookies_dict = {line.split('=')[0]:line.split('=')[1] for line in cookies_str.split('; ')}
response = requests.get(url, headers=headers, cookies=cookies_dict)

print(response.content.decode())
json_str = json.loads(response.content.decode())
for line_json_dict in json_str:
    print(line_json_dict['title'])
    print(line_json_dict['url'])







