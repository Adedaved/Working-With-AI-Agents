# AI agent evaluation

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Evaluation measures whether the agent performs the intended task to the required standard. Combine output checks with trajectory checks: task completion, factual grounding, tool selection, latency, cost and adherence to constraints. Use representative cases and a reviewed answer set. Automated grading can help scale review, but calibrate it against human judgments and objective checks. Keep failure examples so improvements can be tested against them.

## Try it: original exercise

1. Define a rubric before running the agent: completeness, accuracy and constraint compliance.
2. Include normal, ambiguous and missing-source cases.
3. Inspect both artifacts and tool actions, recording specific failures.
4. Revise one relevant part of the setup and evaluate fresh cases.

## Check your understanding

Why inspect the trajectory as well as the final answer?

**Answer checkpoint:** A correct-looking answer can come from the wrong source or an unauthorized action.

## Common mistake

Do not change the grading standard after seeing results simply to make the score look better.

## IBM sources and implementation guides

- [S085: What is AI Agent Evaluation? | IBM](https://www.ibm.com/think/topics/ai-agent-evaluation)
- [S086: AI Agent Evaluation from Prompts to Metrics | IBM](https://www.ibm.com/think/tutorials/ai-agent-evaluation)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
