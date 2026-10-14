# Hierarchical AI agents

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Hierarchical agents divide work into levels. A higher-level coordinator holds the broader objective and delegates bounded tasks to lower-level specialists. Each delegation needs scope, relevant context and acceptance criteria. The hierarchy can reduce task complexity for a worker, but can also create bottlenecks and errors in translation. Use it when responsibilities genuinely differ, and keep the coordinator able to inspect and reject unsuitable results.

## Try it: original exercise

1. Define a coordinator for an incident report and specialists for logs and documentation.
2. Give each specialist a bounded input and an evidence-linked output.
3. Have the coordinator reconcile disagreements before drafting the report.
4. Evaluate whether the hierarchy improves quality enough to justify its overhead.

## Check your understanding

What should the coordinator do when two workers contradict each other?

**Answer checkpoint:** Compare their sources and assumptions, seek missing evidence and resolve or report the disagreement.

## Common mistake

Delegation does not remove the need for a final owner of the result.

## IBM sources and implementation guides

- [S035: What are Hierarchical AI Agents? | IBM](https://www.ibm.com/think/topics/hierarchical-ai-agents)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
