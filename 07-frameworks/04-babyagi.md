# BabyAGI

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

BabyAGI demonstrates an execute-create-prioritize loop. A system completes a task, proposes follow-up work and reorders the remaining queue toward the objective. It is useful for understanding task management but raises an obvious issue: generated follow-up tasks can keep the system busy without finishing the goal. Make relevance, dependencies and termination explicit.

## Try it: original exercise

1. Create a queue of three tasks for a small knowledge-base cleanup.
2. After one task, propose only follow-ups needed for the original objective.
3. Prioritize tasks by dependency and relevance, removing duplicates.
4. Stop when the acceptance criteria are met rather than when no new ideas can be generated.

## Check your understanding

What prevents endless task generation?

**Answer checkpoint:** A bounded objective, queue checks, a budget and an explicit completion rule.

## Common mistake

New tasks are proposals to validate, not automatic proof that more work is required.

## IBM sources and implementation guides

- [S066: What is BabyAGI? | IBM](https://www.ibm.com/think/topics/babyagi)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
