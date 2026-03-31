# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=openai_api_key,
    base_url="https://openai.vocareum.com/v1" 
)

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key)

# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print(
    "\nExplanation: The DirectPromptAgent answered this question using the general "
    "knowledge contained within the GPT-3.5-turbo model. The agent does not use "
    "any additional persona, tools, or external knowledge sources—it simply sends "
    "the user prompt directly to the LLM and returns the response."
)
