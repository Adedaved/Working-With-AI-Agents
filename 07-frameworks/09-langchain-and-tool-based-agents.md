# LangChain and tool-based agents

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

LangChain supplies components for connecting models, prompts, tools and retrieval in applications. It can help assemble a workflow without writing every adapter yourself. IBM's tool-based guide demonstrates an agent using Granite and external functions. A framework can describe a tool to the model, but execution and validation must remain real software operations. Keep dependency versions aligned with the implementation guide you follow.

## Try it: original exercise

1. Define a small read-only function and its input schema.
2. Connect it to a tool-capable model following the selected IBM guide.
3. Ask a question that requires the function's data and inspect the call.
4. Test a malformed argument and confirm the runtime rejects it.

## Check your understanding

What is the framework helping connect?

**Answer checkpoint:** Model interactions, tools, context and workflow components; it does not replace the underlying model.

## Common mistake

Do not copy older import paths into a newer dependency environment without checking compatibility.

## IBM sources and implementation guides

- [S074: What Is LangChain? | IBM](https://www.ibm.com/think/topics/langchain)
- [S075: Using LangChain Tools to Build an AI Agent with Granite | IBM](https://www.ibm.com/think/tutorials/using-langchain-tools-to-build-an-ai-agent)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
