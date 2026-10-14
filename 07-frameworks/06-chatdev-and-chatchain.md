# ChatDev and ChatChain

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

ChatDev models collaborative software work through role-based agents. ChatChain structures their interactions into phases such as design, implementation and testing. The useful principle is to make handoffs and artifacts explicit, like a small development team. A role prompt does not establish expertise; the output still needs independent acceptance checks. IBM's linked guide demonstrates the communication pattern with watsonx.ai.

## Try it: original exercise

1. Describe a tiny software feature with clear input and output behavior.
2. Assign design, implementation and review phases with specific deliverables.
3. Require the implementation phase to follow the accepted specification.
4. Inspect whether the review identifies actual defects rather than praising the draft.

## Check your understanding

What should happen if the implementation conflicts with the design?

**Answer checkpoint:** Resolve the discrepancy and revise the relevant artifact before treating the workflow as complete.

## Common mistake

A simulated company structure is useful only when it produces better, reviewable artifacts.

## IBM sources and implementation guides

- [S069: What is ChatDev? | IBM](https://www.ibm.com/think/topics/chatdev)
- [S070: Use ChatDev ChatChain for agent communication on watsonx.ai | IBM](https://www.ibm.com/think/tutorials/chatdev-chatchain-agent-communication-watsonx-ai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
