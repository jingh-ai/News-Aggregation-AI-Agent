# The AggregatorAgent runs *after* the parallel step to synthesize the results.
from google.adk.agents import Agent


aggregator_agent = Agent(
    name="AggregatorAgent",
    model="gemini-2.5-flash-lite",
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""Combine these two journalist findings into a single summary, removing any duplicates:
    **Google News:**
    {google_news}

    **DuckDuckGo News:**
    {duckduckgo_news}
    
    You should merge the news from these two sources and remove duplicate content.""",
    output_key="news_aggregation", # This will be the final output of the entire system.
)

