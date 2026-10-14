# AutoGen and the multi-agent RAG tutorial

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

AutoGen supports interacting agents and coordinated workflows. IBM's explainer distinguishes Microsoft AutoGen from AG2, a separate project that continued an earlier lineage. Its linked local RAG tutorial uses AutoGen/AG2 terminology and specific dependencies. Read the actual package and version instructions rather than assuming examples from the two projects can be combined. The core exercise is separating evidence retrieval, analysis and synthesis.

## Try it: original exercise

1. Identify which project and package versions the selected IBM lab uses.
2. Assign a retrieval role to locate evidence in two synthetic documents.
3. Assign an answering role to use only the retrieved evidence.
4. Check cited sources and run termination before adapting the workflow.

## Check your understanding

Can an AutoGen example and an AG2 example be assumed to share identical APIs?

**Answer checkpoint:** No. Confirm the selected project, version and documentation.

## Common mistake

This lesson preserves IBM's labels while flagging the project distinction; it does not recommend mixing packages.

## IBM sources and implementation guides

- [S063: What is AutoGen? | IBM](https://www.ibm.com/think/topics/autogen)
- [S064: Local Multi-Agent RAG with AutoGen using Granite | IBM](https://www.ibm.com/think/tutorials/multi-agent-autogen-rag-granite)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
