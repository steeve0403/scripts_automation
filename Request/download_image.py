import requests

# https://coderavecjonathan.com/res/papillon.jpg

response = requests.get('https://codeavecjonathan.com/res/papillon.jpg')

if response.status_code == 200:
    file = open('papillon.jpg', 'wb')
    file.write(response.content)
    file.close()
else:
    print(f"Error : code{response.status_code}.")