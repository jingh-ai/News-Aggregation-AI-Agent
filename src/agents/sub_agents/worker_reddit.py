# Research Agent: Its job is to use the google_search tool and present findings.
from google.adk.agents import Agent
import praw
from google.adk.tools import FunctionTool


def reddit_news_search(topic: str, limit: int = 5) -> List[Dict]:
    """Searches Reddit for the latest news and discussions on a specific topic 
    
    Args:
        topic: The topic or keyword to search for (e.g., "Artificial Intelligence", "Stock Market").
        limit: The number of posts to return (default is 5).

    Return:
        A list of dictionaries containing the title, subreddit, score, URL, and a short text preview of each post.
    
    Exception:
        If an error occurs during the search, it returns a list with an error message.
    """
    # Initialize Reddit Client (Replace with your actual credentials)
    reddit = praw.Reddit(
        client_id="YOUR_REDDIT_CLIENT_ID",
        client_secret="YOUR_REDDIT_CLIENT_SECRET"
        )

    # Reddit search
    results = []
    try:
        search_results = reddit.subreddit("all").search(topic, sort="relevance", time_filter="week", limit=limit)
        
        for post in search_results:
            results.append({
                "title": post.title,
                "subreddit": post.subreddit.display_name,
                "score": post.score,
                "url": post.url,
                "text": post.selftext[:200] + "..." if post.selftext else "No text preview"
            })
    except Exception as e:
        return [{"error": str(e)}]
    return results


reddit_tool = FunctionTool.from_function(
    func=reddit_news_search,
    name="reddit_search",
    description="Useful for finding current events, news, and public opinion on specific topics from Reddit."
)

reddit_agent = Agent(
    model="RedditAgent",
    model="gemini-2.5-flash-lite",
    instruction="""
    You are a professional News Research Agent. 
    Your goal is to find high-quality information on Reddit based on user requests.
    
    When a user asks for news:
    1. Identify the core topic.
    2. Use the reddit_search tool to get data.
    3. Summarize the findings into a clear bulleted list, highlighting the most popular discussions (score) and providing links.
    """
    tools=[reddit_tool],
    output_key="reddit_news",
)
