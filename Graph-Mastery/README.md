# Graph Mastery

Beginner-friendly exercises for learning the building blocks of LangGraph. The notebooks progress from a minimal stateful graph to routing and iterative workflows.

## Topics covered

- Defining graph state with `TypedDict`.
- Writing nodes that read and update state.
- Connecting nodes into sequential workflows.
- Adding conditional edges to choose the next step.
- Using loops to repeat work until a stopping condition is met.
- Compiling a graph and invoking it with input state.

## Suggested order

1. `graph1.ipynb` and `exG1.ipynb` — a first graph and state update.
2. `graph2.ipynb` and `exG2.ipynb` — processing state and performing an operation.
3. `graph3.ipynb` and `exG3.ipynb` — multi-step node sequences.
4. `graph4.ipynb` and `exG4.ipynb` — conditional routing.
5. `graph5.ipynb` and `exG5.ipynb` — loops and exit conditions.

`graph1.py` is a Python-script counterpart to the first basic graph example.

## Setup

From the repository root:

```bash
python -m pip install -r Graph-Mastery/requirements.txt
```

Open the notebooks in Jupyter or VS Code and run the cells in order. The examples do not require an API key.

## Learning goal

By working through these exercises, learners practice representing a workflow as explicit state transitions instead of a single opaque chain. These are foundational exercises; they do not cover every LangGraph feature or production deployment.
