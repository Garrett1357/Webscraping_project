import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter

url = 'http://quotes.toscrape.com/'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
all_quotes = []


# Scrape quotes from the first 10 pages
for page in range(1, 11):
    page_quotes = [{'quote': quote.find('span', class_='text').text,
    'author': quote.find('small', class_='author').text, 
    'tags': [tag.text for tag in quote.find_all('a', class_='tag')]}
    for quote in soup.find_all('div', class_='quote')]

    all_quotes.extend(page_quotes)

# Count and length
authors = Counter(quote['author'] for quote in all_quotes)
tags = Counter(tag for quote in all_quotes for tag in quote['tags'])
total_quotes = len(all_quotes)
quote_lengths = [len(quote['quote']) for quote in all_quotes]

# statistics
most_quotes_author, most_quotes_count = authors.most_common(1)[0] #gets tuple of most quoted and extracts name/count
least_quotes_author, least_quotes_count = authors.most_common()[-1] #gets tuple of least quoted and extracts name/count
avg_quote_length = sum(quote_lengths) / total_quotes 
longest_quote = max(all_quotes, key=lambda x: len(x['quote']))['quote']
shortest_quote = min(all_quotes, key=lambda x: len(x['quote']))['quote']
most_popular_tag, most_popular_tag_count = tags.most_common(1)[0] 

# Print statements
print("Author Statistics:")
print(f"Most quotes by an author: {most_quotes_author}: {most_quotes_count} quotes")
print(f"Least quotes by an author: {least_quotes_author}: {least_quotes_count} quotes")
print("Average quote length:", avg_quote_length, "characters")
print("Longest quote:", longest_quote)
print("Shortest quote:", shortest_quote)
print(f"Most popular tag: {most_popular_tag}: {most_popular_tag_count} quotes")

# top authors plotly
top_authors = authors.most_common(10)
plt.figure(figsize=(10, 8))
plt.bar([author[0] for author in top_authors], [author[1] for author in top_authors])
plt.xlabel('Authors')
plt.ylabel('Number of Quotes')
plt.title('Top 10 Authors by Number of Quotes')
plt.xticks(rotation=45)
plt.show()

# top tags plotly
top_tags = tags.most_common(10)
plt.figure(figsize=(10, 8))
plt.bar([tag[0] for tag in top_tags], [tag[1] for tag in top_tags])
plt.xlabel('Tags')
plt.ylabel('Number of Quotes')
plt.title('Top 10 Tags by Popularity')
plt.xticks(rotation=45)
plt.show()

#Garrett Austin