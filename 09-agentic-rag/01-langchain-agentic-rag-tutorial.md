# LangChain agentic RAG tutorial

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Retrieval-augmented generation brings external evidence into a model's context. Agentic RAG adds decisions about what to retrieve, whether it is sufficient and what to do next. IBM's LangChain and Granite guide illustrates the pattern. Retrieval does not guarantee accuracy: the wrong document or an unsupported inference can still produce a wrong answer. Keep source identifiers, document versions and the distinction between evidence and inference.

## Try it: original exercise

1. Create two synthetic runbook documents about different services.
2. Ask a question that requires the correct service-specific source.
3. Have the agent retrieve evidence and cite the relevant document section.
4. Check that each material claim is supported and that missing details remain explicit.

## Check your understanding

Does retrieval modify the model's trained weights?

**Answer checkpoint:** No. It supplies context for the current task rather than performing model training.

## Common mistake

A citation is useful only if the cited passage actually supports the nearby claim.

## IBM sources and implementation guides

- [S093: LangChain agentic RAG tutorial using Granite | IBM](https://www.ibm.com/think/tutorials/agentic-rag)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
