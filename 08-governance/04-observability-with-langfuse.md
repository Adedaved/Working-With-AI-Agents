# Observability with Langfuse

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Observability helps explain behavior using traces, logs and metrics. IBM's Langfuse guide uses a vendor-risk example with watsonx Orchestrate. Its key lesson is to connect a final classification with the data and operations that produced it. Record tool outcomes, timing, configuration and errors. Keep output evaluation separate: an observable wrong answer is still wrong, but easier to diagnose.

## Try it: original exercise

1. Create a synthetic vendor record with explicit risk-rule inputs.
2. Record the agent's source lookup, tool calls and classification.
3. Locate the first incorrect or missing input in a failed trace.
4. Correct that step and compare the new output with the rule-based expected result.

## Check your understanding

How does observability help when a final answer looks plausible?

**Answer checkpoint:** It reveals whether the system actually consulted the required source and followed the expected workflow.

## Common mistake

Avoid logging secrets or unnecessary sensitive contents simply because the tracing platform supports it.

## IBM sources and implementation guides

- [S088: Enhance AI Agent Observability with Langfuse using watsonx Orchestrate | IBM](https://www.ibm.com/think/tutorials/ai-agent-observability-langfuse-watsonx-orchestrate)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
