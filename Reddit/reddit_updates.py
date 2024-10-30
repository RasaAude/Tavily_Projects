import os
from dotenv import load_dotenv
from tavily import TavilyClient
load_dotenv()

'''groq_api_key = os.getenv('GROQ_API_KEY')
groq =Groq(groq_api_key)'''
tavily_api_key = os.getenv('TAVILY_API_KEY') 
tavily = TavilyClient(tavily_api_key)

search_response = tavily.search(
    query="mentions of Tavily, Agentic Search, or AI Agents on Reddit in the past week",
    search_depth="advanced",
    include_domains=["reddit.com"],
    max_results=5
)

extract_responses = {}
for result in search_response['results']:
    url = result['url']
    print(url)
    extract_response = tavily.extract(url)
    extract_responses[url] = extract_response
