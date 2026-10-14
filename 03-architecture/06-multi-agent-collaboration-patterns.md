# Multi-agent collaboration patterns

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Collaboration concerns how agents share work and coordinate decisions. They may exchange messages directly or update a shared state that others inspect. Choose explicit ownership of tasks and changes so workers do not overwrite each other or duplicate actions. Useful collaboration includes conflict resolution and clear handoff conditions. It is more than assigning three role names to the same prompt.

## Try it: original exercise

1. Partition a task into independent evidence-gathering assignments.
2. Give every assignment an owner, completion status and output location.
3. Define who may edit the final artifact and how conflicts are resolved.
4. Check whether contributions are relevant, non-duplicated and traceable.

## Check your understanding

What is risky about several agents editing the same file concurrently?

**Answer checkpoint:** Their changes can conflict or overwrite each other unless edits are coordinated.

## Common mistake

Parallel work should respect dependencies; a review cannot precede the artifact it reviews.

## IBM sources and implementation guides

- [S038: What is Multi-Agent Collaboration? | IBM](https://www.ibm.com/think/topics/multi-agent-collaboration)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
