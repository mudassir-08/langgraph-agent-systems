# LangGraph Learning Lab

A hands-on learning portfolio documenting my progress with LangGraph—from graph fundamentals to LLM-powered agents and tool-using workflows. The examples show how I use explicit state, nodes, edges, and routing to build structured AI applications.

## What you'll find

| Folder | Focus |
| --- | --- |
| [`Graph-Mastery/`](./Graph-Mastery/) | Core graph concepts: state, nodes, sequential workflows, conditional routing, and loops |
| [`Graph-agents/`](./Graph-agents/) | LLM-backed graph applications, conversation state, tool calling, ReAct-style loops, and a drafting workflow |

## Learning outcomes

These examples demonstrate my ability to:

- Model workflow data with graph state.
- Break tasks into nodes and connect them with edges.
- Route execution conditionally and build iterative workflows.
- Connect an LLM to a LangGraph application.
- Define tools and route between an agent and tool execution.
- Stream graph execution and inspect intermediate values.

## Getting started

Use Python 3.10 or newer. Install the dependencies for the folder you want to explore:

```bash
python -m pip install -r Graph-Mastery/requirements.txt
```

For the LLM-backed agent examples:

```bash
python -m pip install -r Graph-agents/requirements.txt
```

The graph fundamentals are primarily Jupyter notebooks; open them in Jupyter or VS Code. Agent scripts can be run from the repository root, for example:

```bash
python Graph-agents/G-agents/G1agent.py
```

Agent examples require a Groq API key. Copy `Graph-agents/.env.example` to `Graph-agents/.env` and set your key there. Never commit `.env` or paste a real key into notebooks or source files.

## Scope

This is a learning repository and a collection of practical demonstrations, not a complete bootcamp curriculum or a production-ready agent framework. The examples focus on foundational patterns; production systems also need concerns such as robust error handling, testing, observability, security, and deployment.

## Repository map

```text
Graph-Mastery/
  graph1–graph5.ipynb     # Introductory graph exercises
  exG1–exG5.ipynb         # Additional graph exercises
  graph1.py               # Python version of a basic graph example
Graph-agents/
  G-agents/
    G1agent.py            # Basic LLM-backed graph
    G2agent.py            # Conversation history in graph state
    G3reAct.py            # Agent and tool execution loop
    G4Drafter.py          # Tool-using drafting workflow
```

## License

This project is licensed under the [MIT License](./LICENSE).
