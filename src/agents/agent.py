from google.adk.agents import ParallelAgent, SequentialAgent
from .sub_agents.aggregator import aggregator_agent
from .sub_agents.worker_google_news import google_agent
from .sub_agents.worker_dds import duckduckgo_agent
from .sub_agents.worker_reddit import reddit_agent    
from .sub_agents.editor import editor_agent
from google.adk.agents import Agent
from google.adk.tools import AgentTool

# The ParallelAgent runs all its sub-agents simultaneously.
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[google_agent, duckduckgo_agent, reddit_agent],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
# The root_agent can now be executed to perform the entire multi-topic research and aggregation process.
content_team_agent = SequentialAgent(
    name="ContentTeamAgent",
    sub_agents=[parallel_research_team, aggregator_agent, editor_agent],
)

root_agent = Agent(
    name="RootAgent",
    model="gemini-2.5-flash-lite",
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""You are a News Editor-in-Chief. Your role has only two duties:
        1, If a user asks for news about a specific topic, you must use the `ContentTeamAgent` tool to search for news on that topic and return the findings.

        2, If a user does not request news, respond as a professional news editor: be concise, friendly, and authoritative. Offer clear framing, short recommendations or next steps when appropriate, and avoid unnecessary detail. Use plain language and maintain an impartial, professional tone.

    """,
    tools=[
        AgentTool(content_team_agent)
    ],    output_key="final_response", # This will be the final output of the entire system.
)