# AgenticAI
Agentic AI Workflow for Product Development

This project demonstrates the design and implementation of an Agentic AI system that simulates a real-world product development workflow using multiple AI agents. The system orchestrates specialized agents that collaborate to analyze a product specification, generate user stories, define product features, and create detailed development tasks.

The project is divided into two phases:

Phase 1 - Agent Library

In this phase, a reusable agent toolkit was developed by implementing several types of AI agents, including:

Direct Prompt Agent
Augmented Prompt Agent
Knowledge-Augmented Prompt Agent
Retrieval-Augmented Generation (RAG) Agent
Evaluation Agent
Routing Agent
Action Planning Agent

Each agent demonstrates a different pattern for interacting with large language models and was tested using individual scripts.

Phase 2 - Agentic Workflow

In this phase, the agents from Phase 1 were orchestrated into a multi-agent workflow that simulates a product development planning process. The workflow performs the following steps:

Interprets a product specification.
Uses an Action Planning Agent to break down the workflow steps.
Routes tasks to the appropriate specialized agents using a Routing Agent.
Uses Knowledge-Augmented Agents to generate structured outputs.
Validates responses using Evaluation Agents.

The final output is a structured project plan containing:

User Stories
Product Features
Development Tasks
Key Concepts Demonstrated
Multi-agent AI system design
Agent orchestration and routing
Knowledge-augmented prompting
Retrieval-augmented generation (RAG)
AI response evaluation and refinement
Workflow automation using AI agents
Technologies Used
Python
OpenAI API
Prompt Engineering
Agent-based workflow design

This project showcases how AI agents can collaborate autonomously to plan and structure complex workflows, demonstrating practical applications of Agentic AI in product management and software development processes.
