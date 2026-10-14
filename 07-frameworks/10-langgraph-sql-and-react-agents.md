# LangGraph: SQL and ReAct agents

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

LangGraph represents workflows as a graph of steps with shared state and transitions. This helps model branches, retries and human checkpoints. IBM links a SQL-agent tutorial and an IT-support ReAct tutorial. For the SQL case, language becomes a proposed query against a database; validate the query and restrict database access. For ReAct, each tool observation informs the next action. Both need explicit stop and failure behavior.

## Try it: original exercise

1. Draw a graph with retrieve, decide, validate and respond nodes.
2. For a SQL lab, use a synthetic database and a read-only database identity.
3. For the support lab, restrict tools and record each diagnostic observation.
4. Check the graph terminates correctly on success, missing evidence and tool failure.

## Check your understanding

Is asking the model not to modify a database enough protection?

**Answer checkpoint:** No. Enforce read-only permissions and appropriate query validation outside the model.

## Common mistake

SQL-agent capabilities should be evaluated on the actual database schema and the selected framework version.

## IBM sources and implementation guides

- [S076: What is LangGraph? | IBM](https://www.ibm.com/think/topics/langgraph)
- [S077: Build a LangGraph SQL Agent with Mistral Medium 3 | IBM](https://www.ibm.com/think/tutorials/build-sql-agent-langgraph-mistral-medium-3-watsonx-ai)
- [S078: Deploy an IT Support LangGraph ReAct agent with Granite on watsonx.ai | IBM](https://www.ibm.com/think/tutorials/deploy-langgraph-react-agent-manage-it-support-tickets-watsonx-ai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
