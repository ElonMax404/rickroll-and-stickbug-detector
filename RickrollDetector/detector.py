import requests


url = input('Input url to check: ')
headers = {'User-Agent': '<yourUserAgent>'}
keywords = ['Rick','Astley','Rick Astley - Never Gonna Give You Up (Video)','Official Rick Astley','Never gonna give you up','Never gonna let you down','Never gonna run around and desert you','Never gonna make you cry','Never gonna say goodbye','Never gonna tell a lie and hurt you']
response = requests.get(url, headers=headers)

def checker(resp):

    found_keywords = 0
    for el in keywords:
        if el.lower() in str(resp.content).lower():
            print(f"Looks like a rickroll! I've found those keywords in this link: ")
            break
    for el in keywords:
        if el.lower() in str(resp.content).lower():
            print(f'{el},')
            found_keywords = found_keywords+1

    if found_keywords == 0:
        print(f"You can be sure that this isn't a rickroll!")


checker(response)
