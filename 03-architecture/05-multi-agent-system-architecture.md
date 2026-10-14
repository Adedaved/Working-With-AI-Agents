# Multi-agent system architecture

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A multi-agent system contains several agents whose interactions contribute to a shared outcome. The architecture specifies their roles, communication, shared state and coordination. IBM's crewAI call-analysis guide demonstrates specialist roles around a customer-service transcript. Architecture is about deciding how the system should be arranged; Chapter 6 develops the collaboration workflow. Shared models can share the same blind spots, so agreement is not independent proof.

## Try it: original exercise

1. Choose roles for a transcript task: evidence extraction, issue classification and review.
2. Give each role only the tools and source material it needs.
3. Define a shared evidence schema containing transcript locations.
4. Compare the combined report with the original transcript and a single-agent baseline.

## Check your understanding

Why can three agreeing agents still be wrong?

**Answer checkpoint:** They may rely on the same misleading input, unsupported assumption or model limitation.

## Common mistake

Prefer evidence reconciliation over majority voting when the question is factual.

## IBM sources and implementation guides

- [S036: What is a Multi-Agent System? | IBM](https://www.ibm.com/think/topics/multiagent-system)
- [S037: Multi-agent Collaboration for Customer Call Analysis using Watsonx.ai and CrewAI | IBM](https://www.ibm.com/think/tutorials/multi-agent-collaboration-call-analysis-watsonx-ai-crewai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
