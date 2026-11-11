# Graph Agents

A set of practical examples exploring how to build LLM-backed applications as LangGraph workflows. They progress from a basic model call to conversation state, tool use, and an iterative drafting workflow.

## Examples

| File | Focus |
| --- | --- |
| `G-agents/G1agent.py` | A basic LangGraph node that calls an LLM |
| `G-agents/G2agent.py` | Passing conversation messages through graph state |
| `G-agents/G3reAct.py` | Tool definitions and an agent/tool execution loop |
| `G-agents/G4Drafter.py` | A tool-using drafting workflow with streamed graph steps |

The text files in `G-agents/` are example conversation/output artifacts used alongside the exercises.

## Setup

From the repository root:

```bash
python -m pip install -r Graph-agents/requirements.txt
```

Create a local environment file from the template:

```powershell
Copy-Item Graph-agents/.env.example Graph-agents/.env
```

Set `GROQ_API_KEY` in `Graph-agents/.env`, then run an example from the repository root:

```bash
python Graph-agents/G-agents/G1agent.py
```

The examples use Groq through `langchain-groq`. Model availability and provider requirements may change; consult the provider's current documentation if a model identifier stops working.

## Learning goal

These examples demonstrate graph-based orchestration of LLM calls and tools, including explicit state and control flow. They are educational prototypes, not production-ready agents. Before using similar patterns in a deployed system, add appropriate validation, error handling, tests, safeguards for tool actions, and operational monitoring.

## API-key safety

Keep the real API key only in your local `.env` file. `.env` files are ignored by the repository's `.gitignore`; commit `.env.example` with a placeholder, never a real credential. If a key has already been published, revoke it and create a replacement.
