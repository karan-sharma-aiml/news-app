import requests  # For sending HTTP requests

# Take user input for the type of news
query = input("🔎 What type of news are you interested in today? ")

# API key from NewsAPI (replace with your own key if required)
api = "7cf7b804202343088abded269bbc42e4"

# Build API URL dynamically with user query
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-22&sortBy=publishedAt&apiKey={api}"

# Make the GET request to fetch news
response = requests.get(url)

# Convert response into JSON format
data = response.json()

# Extract the articles list
articles = data["articles"]

# Print formatted news results
print("\n📰 Latest News on:", query.capitalize())
print("--------------------------------------------------\n")

for index, article in enumerate(articles):
    print(f"{index + 1}. {article['title']}")   # Show headline
    print(f"   👉 Link: {article['url']}")       # Show link
    print("--------------------------------------------------\n")

