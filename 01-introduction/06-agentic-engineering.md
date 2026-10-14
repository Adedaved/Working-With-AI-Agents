# Agentic engineering

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Agentic engineering applies engineering judgment to work carried out with agents. The human remains responsible for requirements, architectural trade-offs, review and acceptance. An agent can accelerate implementation without replacing that responsibility. Keep decisions about interfaces, compatibility, performance and releases explicit. Ask for evidence such as a minimal diff or a reproducible check. This approach works best when the agent can use the real project context and the reviewer can understand what changed.

## Try it: original exercise

1. Define acceptance criteria before asking the agent to implement a feature.
2. Identify existing architectural constraints and compatibility requirements.
3. Review the resulting design, diff and validation evidence.
4. Approve the change only after resolving material questions.

## Check your understanding

Who decides whether the final implementation is acceptable?

**Answer checkpoint:** The responsible human or team, using agreed criteria and evidence.

## Common mistake

Repeatedly accepting generated code without inspection does not become engineering merely because an agent wrote it.

## IBM sources and implementation guides

- [S008: What is Agentic Engineering? | IBM](https://www.ibm.com/think/topics/agentic-engineering)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
