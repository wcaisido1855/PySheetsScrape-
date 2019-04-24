import requests
from bs4 import BeautifulSoup
from csv import writer

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Title', 'Link', 'Date']
#     csv_writer.writerow(headers)


response = requests.get('examplewebsite.com')

page_html = BeautifulSoup(response.text,'html.parser')

container.div.div.a
print(container)
