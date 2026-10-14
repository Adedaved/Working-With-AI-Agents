# Learning

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Learning is improvement from experience, but several mechanisms can produce it. A system may update stored instructions or examples, revise a policy, or train model parameters. These are different operations. In an ordinary agent session, feedback changes the available context and future behavior without automatically retraining the LLM. Name what changed and measure whether it improved results. Otherwise, repeated activity can look like learning while errors remain unchanged.

## Try it: original exercise

1. Run a classification task and save its mistakes with verified corrections.
2. Add a concise rule or example explaining the correction.
3. Repeat the task on fresh cases rather than only the corrected cases.
4. Compare accuracy and error types, documenting which system component changed.

## Check your understanding

Does correcting an agent in chat necessarily update its model weights?

**Answer checkpoint:** No. It normally updates the task context or saved configuration, depending on the system.

## Common mistake

Performance on examples used for correction is not enough evidence of general improvement.

## IBM sources and implementation guides

- [S022: What is AI Agent Learning? | IBM](https://www.ibm.com/think/topics/ai-agent-learning)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
