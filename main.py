import click
import json
from pathlib import Path


@click.command()
@click.option('-i', '--input', required=False, default='/dev/null/doesnotexist', type=Path, help='''
  Input file for the cookies (defaults to STDIN if this left blank)
''')
@click.option('-o', '--output', required=False, default=None, type=Path, help='''
  Output file for the cookies (defaults to STDOUT if this left blank)
''')
def main(input, output):
  """Parse a copy and pasted version of an application's cookies to JSON for import
  """
  
  # Cast input to a path
  input = Path(input)
  
  # Check if input exists
  if input.exists():
    chrome_cookies_input = input.read_text()
  else:
    chrome_cookies_input = click.prompt('Please paste your cookies now')
  
  # Begin parsing the cookies
  chrome_cookies = chrome_cookies_input.splitlines()
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

  # Parse the cookies to JSON
  cookies_json = json.dumps(chrome_cookies_list)

  if output:
    parsed_chrome_cookies = Path(output)
    parsed_chrome_cookies.write_text(cookies_json)
    print(f'Cookies written to { str(parsed_chrome_cookies.absolute()) }')
  else:
    print(cookies_json)
    
  

if __name__ == '__main__':
  main()