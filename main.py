import json
from pathlib import Path

def main():

  chrome_cookies_file = Path('test')
  chrome_cookies = chrome_cookies_file.read_text()

  chrome_cookies = chrome_cookies.splitlines()

  chrome_cookies_list = []

  for line in chrome_cookies:
    line = line.split('\t')

    name = line[0]
    value = line[1]
    domain = line[2]
    path = line[3]
    expires = line[4]
    size = line[5]
    http_only = line[6]
    secure = line[7]
    same_site = line[8]
    same_party = line[9]
    partition_key = line[10]
    priority = line[11]

    cookies = {
        "name": name,
        "value": value,
        "domain": domain,
        "hostOnly": False, #Unknown
        "path": path,
        "secure": len(secure) > 0,
        "httpOnly": len(http_only) > 0,
        "sameSite": "no_restriction" if len(same_site) == 0 else '',
        "session": True,
        "firstPartyDomain": "",
        "partitionKey": partition_key,
        "storeId": None
      }

    chrome_cookies_list.append(cookies)


  parsed_chrome_cookies = Path('test_cookies')
  cookies_json = json.dumps(chrome_cookies_list)
  parsed_chrome_cookies.write_text(cookies_json)

if __name__ == '__main__':
  main()