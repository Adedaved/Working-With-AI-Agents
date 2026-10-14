# Communication

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Communication lets an agent exchange information with a person, another agent or an external system. A useful message includes the task, relevant evidence, output expectations and status. Structured fields make handoffs easier to validate than a long vague conversation. Share enough context for the recipient to act, and identify sources instead of passing unsupported claims. Communication does not imply that every participant shares the same memory.

## Try it: original exercise

1. Write a handoff with task_id, objective, source_ids and expected_output.
2. Include a status field: pending, completed, blocked or failed.
3. Ask the recipient to return evidence and unresolved questions.
4. Check the response against the handoff contract before continuing.

## Check your understanding

What is missing from a handoff that says only "please finish this"?

**Answer checkpoint:** The objective, relevant context, required result, ownership and constraints.

## Common mistake

A confident message from another agent is still a claim that may need evidence.

## IBM sources and implementation guides

- [S021: What is AI Agent Communication? | IBM](https://www.ibm.com/think/topics/ai-agent-communication)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
