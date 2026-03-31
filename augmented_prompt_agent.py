# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=openai_api_key,
    base_url="https://openai.vocareum.com/v1" 
)

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# The agent likely used general knowledge from the GPT-3.5 model to determine that
# the capital of France is Paris. This information comes from the model’s training
# data and built-in world knowledge.
#
# The system prompt specifying the persona ("college professor") affects the tone
# and structure of the response. Because the persona requires responses to start
# with "Dear students,", the agent formats the answer in a more academic and
# instructional style instead of a simple direct response.
