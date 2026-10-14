# Agent testing

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Agent testing checks behavior across inputs and conditions, not just whether software executes. Verify tool contracts, task completion, grounded answers and permission boundaries. Include ambiguity, unavailable services and adversarial content as appropriate to the use case. Repeated trials may reveal variability that one run hides. Keep a reviewed expected result so tests do not merely approve whatever the agent produced.

## Try it: original exercise

1. Use example_tickets.csv as a six-record synthetic input.
2. Check expected categories and flag the ambiguous account-access record.
3. Simulate an unreadable input or unavailable lookup; require an explicit limitation.
4. Repeat after changing the instructions and compare against expected_ticket_results.json.

## Worked aid

Synthetic data and a reviewed answer set are included in this folder. They support a manual agent evaluation exercise; no cloud agent is deployed by the repository.

## Check your understanding

How should an agent handle a ticket containing a request to ignore the classification rules?

**Answer checkpoint:** Treat that text as task data, follow the trusted instructions and record any relevant concern.

## Common mistake

A model grading another model is useful feedback, but does not replace independent checks on important facts.

## IBM sources and implementation guides

- [S054: AI Agent Testing | IBM](https://www.ibm.com/think/topics/ai-agent-testing)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
