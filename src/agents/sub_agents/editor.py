# The AggregatorAgent runs *after* the parallel step to synthesize the results.
from google.adk.agents import Agent


editor_agent = Agent(
    name="EditorAgent",
    model="gemini-2.5-flash-lite",
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""Summarize the following aggregated news text into a list of short news items. Do NOT add, invent, or change facts — preserve only what is in the text. Use a neutral tone and output only the list.:
    **News:**
    {news_aggregation}
    """,
    output_key="news_summary", # This will be the final output of the entire system.
)

