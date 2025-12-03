# Research Agent: Its job is to use the DuckDuckGo tool and present findings.
from google.adk.agents import Agent
from ddgs import DDGS
from datetime import datetime


def duckduckgo_search(topic: str) -> str:
    """Search for news articles on DuckDuckGo related to the given topic.

    This function uses the DuckDuckGo search API to find recent news articles
    related to the specified topic. It retrieves the top five results and formats
    them into a readable string.

    Args:
        topic: The topic to search for news articles.

    Returns:
        A formatted string containing the titles, links, and content of the news articles.
    """
    current_date = datetime.now().strftime("%Y-%m")

    # DuckDuckGo search
    ddg_api = DDGS()
    results = ddg_api.news(f"{topic} {current_date}", max_results=5)
    if results:
        news_results = "\n\n".join([f"Date: {result['date']}\nContent: {result['body']}\nSource: {result['url']}" for result in results])
        return news_results
    else:
        return f"No news found for {topic}。"
    

duckduckgo_agent = Agent(
    name="DuckDuckGoAgent",
    model="gemini-2.5-flash-lite",
    instruction="You are a journalist. Your only task is to use the duckduckgo_search() tool to find five news on the given topic. Each news article should include the publication date, the content of the news, and a link to the source.",
    tools=[duckduckgo_search],
    output_key="duckduckgo_news", # The result of this agent will be stored in the session state with this key.
)