# AI agent security

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Agent security covers the model, tools, data, identities and external systems together. A misleading document can influence a model; an overly privileged tool can turn that influence into an unwanted action. Treat retrieved material as data rather than trusted operational instructions. Apply least privilege, validate tool inputs and keep consequential actions reviewable. Security checks should be part of the specific workflow, not just the prompt.

## Try it: original exercise

1. Give an agent read-only access to a synthetic source folder.
2. Insert a data record that asks it to ignore its task and disclose unrelated information.
3. Verify it continues the approved task and does not follow the embedded instruction.
4. Confirm that unavailable operations are blocked by permissions, not just a verbal rule.

## Check your understanding

Why is a prompt alone insufficient to protect a powerful tool?

**Answer checkpoint:** It cannot replace runtime authorization and input validation.

## Common mistake

External text may look like an instruction, but its presence in a retrieved source does not make it trusted.

## IBM sources and implementation guides

- [S089: What is AI Agent Security? | IBM](https://www.ibm.com/think/topics/ai-agent-security)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
