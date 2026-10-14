# Types of AI agents

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A simple reflex agent reacts to a current condition using rules. A model-based reflex agent also maintains an internal representation of its environment. A goal-based agent selects actions toward a target. A utility-based agent compares outcomes using a scoring function. A learning agent improves its behavior through experience and feedback. These distinctions explain design choices; they are not a leaderboard of products. More complexity is justified only when the task needs it.

## Try it: original exercise

1. Use a rule to raise an alert when a measurement crosses a threshold: simple reflex.
2. Remember whether the alert was already sent: model-based state.
3. Plan steps to restore service: goal-based; weigh downtime against cost: utility-based.
4. Update a policy using evaluated experience: learning; describe what actually changes.

## Worked aid

| Type | Main idea | Original example |
|---|---|---|
| Simple reflex | Current condition and rule | Send a threshold alert |
| Model-based reflex | Rule plus internal state | Suppress a previously sent alert |
| Goal-based | Actions toward a target | Plan service recovery |
| Utility-based | Compare trade-offs | Balance downtime, risk and cost |
| Learning | Improve through experience | Refine a policy from evaluated outcomes |

## Check your understanding

Which type explicitly weighs several acceptable outcomes using a score?

**Answer checkpoint:** A utility-based agent. A goal alone defines the target; utility distinguishes preferable ways to reach it.

## Common mistake

Saving a preference in memory is not automatically the same as retraining the underlying model.

## IBM sources and implementation guides

- [S013: Types of AI Agents | IBM](https://www.ibm.com/think/topics/ai-agent-types)
- [S014: What is a Goal-Based Agent? | IBM](https://www.ibm.com/think/topics/goal-based-agent)
- [S015: What is a Model-Based Reflex Agent? | IBM](https://www.ibm.com/think/topics/model-based-reflex-agent)
- [S016: What Is a Simple Reflex Agent? | IBM](https://www.ibm.com/think/topics/simple-reflex-agent)
- [S017: What is a Utility-Based Agent? | IBM](https://www.ibm.com/think/topics/utility-based-agent)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
