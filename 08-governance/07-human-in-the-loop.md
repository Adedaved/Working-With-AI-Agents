# Human-in-the-loop

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Human-in-the-loop design places review or intervention at defined points in a workflow. A system can pause at a fixed stage or interrupt when a condition demands judgment. IBM's LangGraph tutorial illustrates both approaches with persisted state. Make approval concrete: show the proposed change, supporting evidence and expected effect. Resume only after an actual decision, preserving the state and scope that were reviewed.

## Try it: original exercise

1. Choose a review point before a draft is sent or a repository change is merged.
2. Present the proposed artifact, evidence and unresolved issues.
3. Record approval, requested edits or rejection.
4. Apply the decision and recheck any material changes before continuing.

## Check your understanding

Does no response after an approval request count as approval?

**Answer checkpoint:** No. A required approval must be explicit; dependent actions remain paused.

## Common mistake

Approval of an outline does not automatically approve every later release or scope change.

## IBM sources and implementation guides

- [S091: Human in the loop tutorial | IBM](https://www.ibm.com/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
