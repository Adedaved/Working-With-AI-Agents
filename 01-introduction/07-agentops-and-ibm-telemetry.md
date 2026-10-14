# AgentOps and IBM Telemetry

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

AgentOps is the practice of observing and operating agents so their behavior can be understood and improved. Logs and traces show tool calls, errors, durations and resource usage. A trace follows one request through its steps; a span represents a particular operation within that trace. IBM's linked guide uses IBM Telemetry with watsonx Orchestrate Developer Edition. Treat telemetry as evidence of execution, and evaluate output correctness separately.

## Try it: original exercise

1. Create a run identifier and log each source inspected and tool result.
2. For the IBM implementation lab, follow the linked guide's current local setup prerequisites.
3. Run a small task and locate its trace, tool steps, errors and duration.
4. Compare a failed run with a corrected run to identify the first divergence.

## Check your understanding

Does a trace without errors prove the answer is correct?

**Answer checkpoint:** No. Every tool can succeed while the agent uses the wrong source or applies the wrong rule.

## Common mistake

Log useful metadata and evidence without copying credentials or unnecessary personal information into traces.

## IBM sources and implementation guides

- [S009: What is AgentOps? | IBM](https://www.ibm.com/think/topics/agentops)
- [S010: AgentOps: Monitor and Govern AI Agents with IBM Telemetry using watsonx Orchestrate](https://www.ibm.com/think/tutorials/agentops-telemetry-watsonx-orchestrate)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
