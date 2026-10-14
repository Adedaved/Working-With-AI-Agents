# Agentic coding

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A coding agent can inspect a repository, edit files, run tools and revise its changes. It is more capable than completing a line of code, but still needs a clear engineering task. Supply the relevant repository, describe the bug or desired behavior, and specify how to check success. Ask for changes that fit the project rather than a wholesale rewrite. The deliverable should include the diff, relevant check results and unresolved limitations.

## Try it: original exercise

1. Give a coding agent a repository and a specific reproducible issue.
2. Ask it to inspect existing conventions and propose the smallest relevant change.
3. Have it edit the files and run the checks appropriate to the change.
4. Review the diff and request a revision if behavior or scope is wrong.

## Check your understanding

Why is an isolated branch useful?

**Answer checkpoint:** It makes the change reviewable and keeps the release decision separate from the agent's implementation work.

## Common mistake

Code that looks plausible is not proof that it runs or solves the original problem.

## IBM sources and implementation guides

- [S007: What is Agentic Coding? | IBM](https://www.ibm.com/think/topics/agentic-coding)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
