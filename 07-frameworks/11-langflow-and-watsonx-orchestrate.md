# Langflow and watsonx Orchestrate

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Langflow offers a visual way to connect components for LLM applications and agents. A visual graph can make a workflow easier to inspect, but its integrations and state still need testing. IBM's guide covers custom agents and integration with watsonx Orchestrate, including flows exposed through MCP or imported locally through the development kit. Understand which path you are following before setting it up.

## Try it: original exercise

1. Sketch a flow connecting a user input, source retrieval, model and output.
2. Inspect each component's inputs, outputs and configured credentials.
3. Use the relevant IBM integration path for a separate implementation lab.
4. Export or record the flow configuration so another reviewer can reproduce it.

## Check your understanding

Does a drag-and-drop workflow remove the need for validation?

**Answer checkpoint:** No. It changes the authoring interface, not the need to verify behavior and access.

## Common mistake

Visually connected nodes may still have mismatched schemas or missing runtime configuration.

## IBM sources and implementation guides

- [S079: What is LangFlow? | IBM](https://www.ibm.com/think/topics/langflow)
- [S080: Build Custom AI Agents with Langflow and watsonx Orchestrate | IBM](https://www.ibm.com/think/tutorials/build-custom-ai-agents-with-langflow)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
