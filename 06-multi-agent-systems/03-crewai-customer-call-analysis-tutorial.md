# crewAI customer call analysis tutorial

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

IBM's call-analysis example uses crewAI and watsonx.ai to coordinate specialist roles around a customer-service transcript. The learning objective is to see how a shared input becomes several focused assessments and one combined output. You can first practice the division of labor manually with a synthetic transcript, then use the IBM guide for the implementation. Check conclusions against the actual words in the transcript.

## Try it: original exercise

1. Write a short synthetic call: the customer reports a missing parcel and the representative promises an investigation.
2. Assign tasks for issue extraction, response-quality assessment and follow-up drafting.
3. Require each conclusion to cite the relevant transcript sentence.
4. Combine the results without inventing a refund, replacement or delivery promise.

## Check your understanding

May the final report say a refund was approved when the transcript only promises investigation?

**Answer checkpoint:** No. The report must preserve the scope of what was actually said.

## Common mistake

Role-specific analysis must not become permission to manufacture facts or commitments.

## IBM sources and implementation guides

- [S060: Multi-agent Collaboration for Customer Call Analysis using Watsonx.ai and CrewAI | IBM](https://www.ibm.com/think/tutorials/multi-agent-collaboration-call-analysis-watsonx-ai-crewai)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
