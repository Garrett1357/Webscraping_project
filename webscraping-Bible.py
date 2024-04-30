import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# Give a random chapter between 1 -> 21
chapter_number = random.randrange(1, 22)
if chapter_number < 10:
    chapter_number = '0' + str(chapter_number)
else:
    chapter_number = str(chapter_number)

# Format the URL to include the randomly selected chapter number
webpage = 'https://ebible.org/asv/JHN' + chapter_number + '.htm'
#print("Chapter:", chapter_number)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('div', class_='p')

myverses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split('.')
    for v in verse_list:
        myverses.append(v)

#print(myverses)
random_verse = random.choice(myverses)
print(f"Chapter:{chapter_number} Verse:{random_verse}")
