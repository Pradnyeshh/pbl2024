# from flask import Flask, request, jsonify
from flask import request,Flask,render_template,redirect,Response,jsonify, send_from_directory

import requests
import wikipedia
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/generate-content', methods=['POST'])
def generate_content():
    # Parse the incoming request JSON data to retrieve the topic and report type
    data = request.json
    topic = data['topic']
    report_type = data['report_type']

    print("Hit hua  ")

    if report_type == 'general':
        # Fetch news articles
        print("in general")
        api_key_news = '276c412b1a684791a75efd7872ce7da8'
        articles = get_news(api_key_news, topic, max_articles=2)

        # Fetch detailed information from Wikipedia
        summary, full_content, charts = get_wikipedia_details(topic)
        print(summary)
    elif report_type == 'technical':
        # Fetch technical report using IEEE API
        api_key_ieee = 'your_ieee_api_key'  # Replace 'your_ieee_api_key' with your actual API key
        ieee_report = get_technical_report(topic, api_key_ieee)

        # Initialize other variables as None for consistency
        articles = []
        summary = None
        full_content = None
        charts = None

        return jsonify({
            'articles': articles,
            'summary': summary,
            'full_content': full_content,
            'charts': charts,
            'ieee_report': ieee_report
        })

    # Return the fetched data as a JSON response to the frontend for the general report
    return jsonify({
        'articles': articles,
        'summary': summary,
        'full_content': full_content,
        'charts': charts
    })
# Function to fetch news articles from NewsAPI
def get_news(api_key, query, max_articles=2):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&pageSize={max_articles}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return articles
    else:
        print("Failed to fetch news:", response.text)
        return []

# Function to fetch detailed information from Wikipedia
def get_wikipedia_details(topic):
    try:
        wikipedia.set_lang("en")
        page = wikipedia.page(topic)
        # Extract main summary
        summary = page.summary
        # Extract full content (including sections)
        full_content = page.content
        # Parse HTML of the Wikipedia page
        soup = BeautifulSoup(page.html(), 'html.parser')
        # Extract any available charts (example: images with class "thumb")
        charts = soup.find_all('img', class_='thumb')
        return summary, full_content, charts
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{topic}'.", None, None
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
        return f"Disambiguation page found for '{topic}'. Options: {', '.join(options)}.", None, None

# Prompt user to enter the topic name
# topic = input("Enter a topic to search: ")

# # Example usage
# api_key_news = '276c412b1a684791a75efd7872ce7da8'

# # Fetch news articles (for fun facts)
# articles = get_news(api_key_news, topic, max_articles=2)
# print("Fun Facts from News Articles:")
# for article in articles:
#     print("Title:", article['title'])
#     print("URL:", article['url'])
#     print()

# # Fetch detailed information from Wikipedia
# summary, full_content, charts = get_wikipedia_details(topic)
# print("Overview (from Wikipedia):")
# print(summary)
# print()

# if full_content:
#     print("Detailed Information (from Wikipedia):")
#     print(full_content)
#     print()

# if charts:
#     print("Charts (from Wikipedia):")
#     for i, chart in enumerate(charts, start=1):
#         print(f"Chart {i}: {chart['src']}")

def get_technical_report(topic, api_key):
    base_url = "https://example.com/ieee/api"  # Replace with actual IEEE API endpoint
    params = {
        'topic': topic,
        'api_key': "c9epkj8pvvxb2chgj3f7my6t"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        
        ieee_report = response.json()  # Assuming the response is in JSON format
        return ieee_report
    except requests.RequestException as e:
        print("Error fetching data from IEEE API:", e)
        return None



if __name__ == '__main__':
    app.run(debug=True)