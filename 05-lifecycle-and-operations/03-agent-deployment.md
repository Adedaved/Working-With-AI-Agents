# Agent deployment

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Deployment makes the workflow available in its target environment with the identities, integrations and operational controls it needs. A notebook running once is not the same as an operated service. Choose a rollout that allows you to inspect failures before expanding usage. Separate code and configuration from secrets. Match permissions to the approved task and provide a way to stop or roll back a malfunctioning version.

## Try it: original exercise

1. Move the tested workflow into a controlled staging environment.
2. Configure required connections and restricted service identities.
3. Run a small pilot and inspect logs, outputs, latency and cost.
4. Promote the version only after acceptance criteria pass; keep rollback instructions.

## Check your understanding

What must be checked besides whether the process starts?

**Answer checkpoint:** Correct outputs, required access, failure behavior, operational visibility and recovery.

## Common mistake

A deployment platform cannot compensate for unclear acceptance criteria or incorrect source material.

## IBM sources and implementation guides

- [S053: How to Deploy AI Agents Across the Enterprise | IBM](https://www.ibm.com/think/topics/ai-agent-deployment)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
