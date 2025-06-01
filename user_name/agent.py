from google.adk.agents import Agent
from google.adk.tools import google_search
# from test import get_username
import os
import getpass

def get_username() -> dict:
    """
    Returns:
        dict: A dictionary with the key 'output' and the value as the current user's name.
    
    """
    try:
        username = os.getlogin()
    except OSError:
        username = getpass.getuser()
    return {'output': username}





root_agent = Agent(
    name="user_name",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    you are an agent that can use the following tools:
  
    - google_search: performs a Google search and returns the results.
    You can use the tools to answer the user's question.

    """,


    tools=[google_search],
    # tools=[get_username],

)   
