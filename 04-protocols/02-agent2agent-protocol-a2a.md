# Agent2Agent protocol: A2A

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A2A standardizes communication between agents that may live in different systems. It helps separate a client or requesting agent from the service that performs the task. Capabilities, tasks, messages and returned artifacts form the collaboration interface. IBM's example demonstrates a terminal client communicating with an agent server. The protocol carries requests and responses; it does not by itself make an agent competent, authorized or trustworthy.

## Try it: original exercise

1. Identify the client, agent server and advertised capabilities in IBM's guide.
2. Map a user request into a task with a clear expected output.
3. Follow how status updates and the final response return to the client.
4. Test unknown requests and failure responses before connecting real workflows.

## Check your understanding

How does A2A differ from MCP at the main conceptual level?

**Answer checkpoint:** A2A supports agent collaboration; MCP primarily connects an AI application to tools and resources.

## Common mistake

Remote capability discovery must be paired with authentication and permission checks.

## IBM sources and implementation guides

- [S046: What Is Agent2Agent (A2A) Protocol? | IBM](https://www.ibm.com/think/topics/agent2agent-protocol)
- [S047: Use the A2A Protocol for AI Agent Communication | IBM](https://www.ibm.com/think/tutorials/use-a2a-protocol-for-ai-agent-communication)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
