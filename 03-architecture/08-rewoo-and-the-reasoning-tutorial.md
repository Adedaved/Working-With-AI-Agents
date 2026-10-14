# ReWOO and the reasoning tutorial

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

ReWOO separates planning from evidence collection. A planner lays out the needed work, workers obtain tool results, and a solver synthesizes the evidence into an answer. This can reduce repeated model interactions when the information requirements are predictable. It still uses observations: the name describes planning without waiting for each tool response, not answering without evidence. Failure handling remains necessary when a planned tool call cannot complete.

## Try it: original exercise

1. Plan the evidence needed to compare two deployment options.
2. Collect the specified compatibility, cost and operational constraints.
3. Synthesize only after the evidence-gathering stage reports its results.
4. Revise or stop if missing evidence makes the original plan insufficient.

## Check your understanding

Does ReWOO eliminate external tools or their results?

**Answer checkpoint:** No. It separates advance planning from tool execution and final synthesis.

## Common mistake

An upfront plan can become stale when conditions change; efficiency does not excuse an invalid plan.

## IBM sources and implementation guides

- [S041: What is ReWOO? | IBM](https://www.ibm.com/think/topics/rewoo)
- [S042: Building a ReWOO Reasoning Agent Using IBM Granite](https://www.ibm.com/think/tutorials/build-rewoo-reasoning-agent-granite)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
