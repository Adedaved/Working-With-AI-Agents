# Agentic workflows

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A workflow links observations, decisions and actions. Some steps should be deterministic: validate a file, count records or check permissions. An agentic decision is useful where inputs vary and the next action depends on what was found. LangGraph represents work with nodes, transitions and shared state; IBM's linked implementation uses LangGraph and Granite. Keep the graph understandable and give loops an explicit limit.

## Try it: original exercise

1. Sketch the states: read input, classify, validate and write a draft.
2. Add a branch for missing data that requests clarification rather than guessing.
3. Record shared state such as processed ticket IDs and outstanding errors.
4. Stop when all valid inputs are accounted for or the retry limit is reached.

## Check your understanding

Why track processed IDs?

**Answer checkpoint:** To detect omissions and duplicate processing when a workflow branches or resumes.

## Common mistake

A fixed four-step script is a workflow, but its fixed sequence alone does not demonstrate adaptive agent behavior.

## IBM sources and implementation guides

- [S019: What are Agentic Workflows? | IBM](https://www.ibm.com/think/topics/agentic-workflows)
- [S020: Building Agentic Workflows with LangGraph and Granite | IBM](https://www.ibm.com/think/tutorials/build-agentic-workflows-langgraph-granite)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
