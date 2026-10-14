# Model Context Protocol: MCP

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

MCP standardizes how an AI application connects to exposed tools and resources. The host runs the AI application, a client establishes the connection, and a server exposes capabilities. IBM links both a server-building guide and an IBM Bob integration guide; the latter currently redirects to Bob documentation. Tool schemas describe accepted arguments. Real authorization, validation and execution happen outside the model. MCP is a connection standard, not a model or an automatic permission grant.

## Try it: original exercise

1. Sketch host, client, server and a read-only tool such as lookup_runbook.
2. Define the tool input and structured output; inspect tool_contract.json for a toy contract.
3. Follow IBM's server guide or Bob guide to connect a small local server in a separate lab.
4. Test discovery, a valid call and a rejected unsupported call.

## Worked aid

| Connection | Main purpose | Example |
|---|---|---|
| MCP | AI application to tools and resources | Read a runbook |
| A2A | Agent to agent | Delegate an evidence-gathering task |
| ACP | Earlier interoperability approach | Understand older examples and migration |

## Check your understanding

Does connecting an MCP server mean every listed action should be allowed?

**Answer checkpoint:** No. Review exposed capabilities and enforce appropriate permissions for the task.

## Common mistake

The bundled contract is illustrative JSON, not a complete MCP wire-protocol message.

## IBM sources and implementation guides

- [S048: What is Model Context Protocol (MCP)? | IBM](https://www.ibm.com/think/topics/model-context-protocol)
- [S049: Build MCP servers with IBM Bob | Docs | IBM Bob](https://bob.ibm.com/docs/ide/tutorials/mcp-server-integration)
- [S050: How to build an MCP Server | IBM](https://www.ibm.com/think/tutorials/how-to-build-an-mcp-server)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
