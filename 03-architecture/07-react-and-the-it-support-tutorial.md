# ReAct and the IT support tutorial

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

ReAct interleaves reasoning, action and observation. The agent chooses an action, receives its result and uses that observation to select the next step. This pattern suits tasks where new evidence changes the plan. IBM's linked LangGraph example applies it to IT support tickets. Inspectable tool results and concise decision summaries are enough for a practical audit; private internal reasoning is not required.

## Try it: original exercise

1. Start with a ticket: the user cannot reach the internal application.
2. Retrieve the relevant runbook before choosing the next diagnostic action.
3. Use each observed result to revise the next step rather than following a blind script.
4. Stop at the diagnosis or approved action boundary and save the evidence-linked report.

## Check your understanding

What distinguishes ReAct from a fully fixed plan?

**Answer checkpoint:** Observations from each action inform subsequent decisions.

## Common mistake

Set a step or time budget so repeated unsuccessful tool calls do not continue indefinitely.

## IBM sources and implementation guides

- [S039: What is a ReAct Agent? | IBM](https://www.ibm.com/think/topics/react-agent)
- [S040: Deploy an IT Support LangGraph ReAct agent with Granite on watsonx.ai | IBM](https://www.ibm.com/think/tutorials/deploy-langgraph-react-agent-manage-it-support-tickets-watsonx-ai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
