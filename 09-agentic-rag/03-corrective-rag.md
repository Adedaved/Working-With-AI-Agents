# Corrective RAG

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Corrective RAG checks retrieval quality and takes a bounded corrective action when evidence is weak. Options include rewriting a query, retrieving again, using an approved alternate source or reporting that evidence is insufficient. IBM's insurance-policy example includes internal retrieval, evidence scoring and a checked web-search fallback. Public web information must not silently replace a private policy. Relevance scores are signals to verify, not guarantees of truth.

## Try it: original exercise

1. Ask a question whose answer is absent from a synthetic policy document.
2. Check whether the initial retrieval actually contains supporting evidence.
3. Allow one revised search or an approved alternative source, preserving provenance.
4. If the evidence remains insufficient, return a limited answer instead of filling the gap.

## Check your understanding

Can a general web article establish the terms of a specific private policy?

**Answer checkpoint:** No. Verify applicability; otherwise report that the policy-specific answer is unavailable.

## Common mistake

Do not loop endlessly until a source appears to confirm the answer you wanted.

## IBM sources and implementation guides

- [S096: Build a Corrective RAG Agent | IBM](https://www.ibm.com/think/tutorials/build-corrective-rag-agent-granite-tavily)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
