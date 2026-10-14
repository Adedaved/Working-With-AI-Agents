# Memory

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Memory is information the agent can retain or retrieve beyond its immediate next action. Short-term state includes the current conversation and working variables. Longer-term stores can hold facts, previous runs, preferences or procedures. These stores are separate from the model's learned parameters and must be supplied or retrieved into usable context. Memory needs ownership, relevance and freshness: an old decision is not automatically today's rule.

## Try it: original exercise

1. Separate current run state from facts worth saving between runs.
2. Attach a source, timestamp and owner to saved preferences or decisions.
3. Retrieve only the information relevant to the new task.
4. Test whether a newer rule supersedes an older stored instruction.

## Check your understanding

What is the danger of retrieving an obsolete client policy?

**Answer checkpoint:** It can ground a specific but wrong answer; source freshness matters as much as memory availability.

## Common mistake

An agent may have persistent storage while the underlying LLM has no independent memory of your project.

## IBM sources and implementation guides

- [S023: What Is AI Agent Memory? | IBM](https://www.ibm.com/think/topics/ai-agent-memory)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
