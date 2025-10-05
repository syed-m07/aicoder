# AI Coder

AI Coder is an autonomous AI-powered software engineering agent. It uses a multi-agent system to turn a natural language prompt into a fully functional software project, generating the entire codebase from scratch.

## How It Works

The system is built on a multi-agent architecture orchestrated by [LangGraph](https://github.com/langchain-ai/langgraph). The process flows through a series of specialized agents:

1.  **Planner Agent**: Receives the user's high-level prompt (e.g., "build a todo app") and creates a comprehensive project plan. This includes the project name, description, technology stack, required features, and a list of all the files that need to be created.

2.  **Architect Agent**: Takes the plan from the Planner and designs a detailed software architecture. It breaks down each file's purpose into a series of concrete, ordered implementation tasks. Each task description is highly detailed, specifying the exact functions, classes, variables, and integration points required.

3.  **Coder Agent**: Executes the architectural plan step-by-step. For each task, it:
    *   Reads the current state of the relevant file (if it exists).
    *   Uses a powerful language model ([Groq](https://groq.com/)) and a set of tools to write or modify the code.
    *   Saves the changes to the file system.
    *   This agent loops through all tasks until the entire project is implemented.

All generated code is safely contained within a `generated_project` directory.

## Features

-   **Autonomous Code Generation**: Go from a single prompt to a complete codebase.
-   **Multi-Agent System**: Specialized agents for planning, architecture, and coding ensure a structured and robust development process.
-   **Tool-Equipped Coder**: The Coder agent can read, write, and list files, giving it the ability to build a project incrementally.
-   **Safe Execution**: All file system operations are sandboxed to a specific project directory to prevent unintended changes to your system.
-   **Powered by LangGraph and Groq**: Utilizes modern AI frameworks for fast and reliable agent orchestration and inference.

## Technology Stack

-   **Backend**: Python
-   **AI Orchestration**: LangChain & LangGraph
-   **LLM Provider**: Groq (via `langchain-groq`)
-   **Data Validation**: Pydantic

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/AICoder.git
    cd AICoder
    ```

2.  **Install dependencies:**
    This project uses `uv` for package management.
    ```bash
    uv pip install -r requirements.txt 
    # Or create and sync a virtual environment
    uv venv
    uv pip sync
    ```
    *(Note: If you don't have `uv`, you can install it with `pip install uv` or use `pip` directly with the `pyproject.toml` file.)*

3.  **Set up environment variables:**
    Create a `.env` file in the root of the project and add your Groq API key:
    ```
    GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

## Usage

1.  **Run the application from the command line:**
    ```bash
    python main.py
    ```

2.  **Enter your project prompt:**
    When prompted, type in a description of the application you want to build.
    ```
    Enter your project prompt: Build a colourful modern todo app in html css and js
    ```

3.  **Find your code:**
    The agent will start working, and you can observe its progress in the console. All the generated files will be located in the `generated_project` directory.

## Project Structure

```
.
├── agent/                # Contains the core agent logic
│   ├── graph.py          # Defines the agent graph and workflow
│   ├── prompts.py        # Stores prompts for each agent
│   ├── states.py         # Defines the Pydantic state models
│   └── tools.py          # Tools for the Coder agent (e.g., file I/O)
├── generated_project/    # Output directory for the generated code
├── main.py               # Main entry point to run the application
├── .env                  # For API keys and environment variables
├── pyproject.toml        # Project metadata and dependencies
└── README.md             # This file
```
