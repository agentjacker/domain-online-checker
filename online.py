import requests

with open('bmw.txt') as f:
    websites = [line.rstrip() for line in f]

online_websites = []

for website in websites:
    try:
        response = requests.get('https://' + website)
        if response.status_code == 200:
            online_websites.append(website)
            print(website + ' is online')
        else:
            print(website + ' is not online')
    except:
        print(website + ' is not online')

with open('bmws.txt', 'w') as f:
    for website in online_websites:
        f.write(website + '\n')
