# Agentic orchestration in a team

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

In a team workflow, orchestration determines who works next, which outputs are required and how the overall task completes. Build responsibilities around separable work rather than decorative personas. Use a shared task ledger and explicit acceptance checks. Architecture Chapter 3 explains the design; here the focus is applying it to a team producing one reviewed deliverable.

## Try it: original exercise

1. Create a task ledger with source review, evidence extraction and synthesis.
2. Assign each role an output contract and access to its required inputs.
3. Require the synthesis role to verify evidence before combining contributions.
4. Measure completeness, duplicated work and review effort against a single-agent run.

## Check your understanding

What is the completion condition for the whole team?

**Answer checkpoint:** The accepted deliverable meets the task criteria, not merely that every agent has sent a message.

## Common mistake

Useful coordination needs evidence and dependency checks as well as a shared goal.

## IBM sources and implementation guides

- [S057: What is AI Agent Orchestration? | IBM](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [S058: LLM Agent Orchestration: A Step by Step Guide | IBM](https://www.ibm.com/think/tutorials/llm-agent-orchestration-with-langchain-and-granite)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
