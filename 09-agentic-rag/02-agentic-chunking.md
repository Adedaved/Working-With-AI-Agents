# Agentic chunking

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Chunking divides documents into pieces that can be retrieved and passed to a model. Agentic chunking uses content-aware decisions to preserve meaningful relationships rather than relying only on fixed lengths. A useful chunk should remain understandable with its heading, source and relevant metadata. IBM's linked guide demonstrates an implementation with LangChain and watsonx.ai. Measure retrieval quality: a more elaborate splitting method is not automatically better.

## Try it: original exercise

1. Write a synthetic runbook containing normal steps and a separate exceptions section.
2. Split it once at fixed lengths and once at meaningful section boundaries.
3. Ask a question about an exception and inspect which chunks are retrieved.
4. Compare whether the retrieved pieces preserve the condition and its associated action.

## Check your understanding

What can go wrong when a sentence and its exception are split apart?

**Answer checkpoint:** The answer may apply a general rule without the qualifying condition.

## Common mistake

Preserve source and section metadata so a reviewer can reconstruct the original context.

## IBM sources and implementation guides

- [S094: What Is Agentic Chunking? | IBM](https://www.ibm.com/think/topics/agentic-chunking)
- [S095: Agentic Chunking: Optimize LLM Inputs with LangChain and watsonx.ai | IBM](https://www.ibm.com/think/tutorials/use-agentic-chunking-to-optimize-llm-inputs-with-langchain-watsonx-ai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
