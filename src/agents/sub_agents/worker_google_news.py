# Research Agent: Its job is to use the google_search tool and present findings.
from google.adk.agents import Agent
from google.adk.tools import google_search


google_agent = Agent(
    name="GoogleAgent",
    model="gemini-2.5-flash-lite",
    instruction="You are a journalist. Your only task is to use the google_search tool to find five news on the given topic. Each news article should include the publication date, the content of the news, and a link to the source.",
    tools=[google_search],
    output_key="google_news", # The result of this agent will be stored in the session state with this key.
)

