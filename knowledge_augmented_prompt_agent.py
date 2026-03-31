# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=openai_api_key,
    base_url="https://openai.vocareum.com/v1" 
)
prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    persona,
    knowledge
)

# Generate the response
response = knowledge_agent.respond(prompt)

# TODO: 3 - Print a statement showing the agent uses provided knowledge
print("Agent Response:")
print(response)

print("\nExplanation:")
print(
    "The agent responded using the provided knowledge ('The capital of France is London, not Paris') "
    "instead of the model’s real-world knowledge that the capital is Paris. "
    "This demonstrates that the KnowledgeAugmentedPromptAgent relies strictly on the supplied knowledge base."
)