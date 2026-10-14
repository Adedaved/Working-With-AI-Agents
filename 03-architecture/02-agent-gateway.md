# Agent gateway

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A gateway mediates agent access to tools, services and other resources. It can route calls, enforce authorization, constrain requests and record activity. Think of it as a controlled entry point into the resources that agents use. Its job differs from selecting the business task: the agent may propose an action, while the gateway checks whether that action is allowed. A gateway is useful infrastructure, not a guarantee that the agent's answer is correct.

## Try it: original exercise

1. Inventory the services an agent may call.
2. Define permitted operations for each service and identity.
3. Test an allowed read and a denied write through the access layer.
4. Inspect the request log to verify that rejected actions did not execute.

## Check your understanding

Should an agent decide its own permissions merely by asking for a tool?

**Answer checkpoint:** No. Permissions must be enforced outside the model by the host or access layer.

## Common mistake

A successful connection does not imply unrestricted access to every operation.

## IBM sources and implementation guides

- [S033: What is an Agent Gateway? | IBM](https://www.ibm.com/think/topics/agent-gateway)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
