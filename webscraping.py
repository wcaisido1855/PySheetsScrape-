import requests
from bs4 import BeautifulSoup
from csv import writer

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Title', 'Link', 'Date']
#     csv_writer.writerow(headers)


response = requests.get('http://www.romriellinvest.com/listings/up-and-coming-neighborhood/')

page_html = BeautifulSoup(response.text,'html.parser')

# Extract Variables
PostingTitle = page_html.find(class_='blog-single-title').get_text().replace('\n', '')
PostingDate = page_html.find(class_='date').get_text().replace('\n', '')

# Need to figure out how to parse and display all of the <p> and <div> tags inside this div
PropertyOverviewDescription = page_html.find(class_='mp-property-header').find_next_sibling().get_text().replace('\n', '')

# Need to figure out how to parse and display table
PropertyDetailsTable = page_html.find(class_='property-details').get_text()

NB_Data = [PostingTitle, PostingDate, PropertyOverviewDescription, PropertyDetailsTable]

print("\n")
print("[Title]: " + PostingTitle, "\n")
print("[Date]: " + PostingDate, "\n")
print("[Property Overview]:")
print(PropertyOverviewDescription, "\n")
print("[Property Details]:")
print(PropertyDetailsTable)


#posts = soup.find_all(class_='holder blog-single')
#for post in posts:
#    title = post.find(class_='blog-single-title').get_text().replace('\n', '')
#    print (title)
#         link = post.find('a')['href']
#         date = post.select('.post-date')[0].get_text()
#         csv_writer.writerow([title, link, date])

