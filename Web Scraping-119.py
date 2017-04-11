## 2. Web Page Structure ##

# Write your code here.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content

## 3. Retrieving Elements from a Page ##

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

head = parser.head
title = head.title
title_text = title.text

## 4. Using Find All ##

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")

# Get the text.
print(p[0].text)


head = parser.find_all('head')
title = head[0].find_all('title')
title_text = title[0].text

print(title)
