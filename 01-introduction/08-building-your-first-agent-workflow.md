# Building your first agent workflow

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A practical first workflow connects a goal to real inputs, restricted tools and a concrete output. Begin with read-only source access and draft creation. The model can propose tool calls, but application code or the host executes them. Build in validation and a clear stopping rule. For a tutorial repository, success might mean all approved topics are represented, internal links work and the final artifact is readable.

## Try it: original exercise

1. State the goal: create an evidence-linked summary of six support tickets.
2. Provide the ticket file, category definitions and an example of the output.
3. Allow file reads and draft writes, then ask the agent to document actions.
4. Check every ticket against the summary and provide specific corrective feedback.

## Check your understanding

What should happen when required input is missing?

**Answer checkpoint:** The agent should identify the missing input and seek it or report the limitation, rather than inventing it.

## Common mistake

The instruction to use a tool does not create tool access that the environment lacks.

## IBM sources and implementation guides

- [S011: How to Build an AI Agent | IBM](https://www.ibm.com/think/topics/how-to-build-an-ai-agent)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
