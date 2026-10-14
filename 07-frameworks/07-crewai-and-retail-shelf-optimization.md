# crewAI and retail shelf optimization

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

crewAI organizes agent work around roles, tasks and a coordinated crew. IBM's retail example combines multimodal observations with specialist analysis to propose shelf-layout improvements. Separate observations visible in an image from conclusions requiring sales or inventory data. A photo may show product placement, but it cannot establish revenue uplift by itself. Use explicit evidence requirements when combining multiple perspectives.

## Try it: original exercise

1. Use a synthetic shelf sketch or permitted image and list directly visible facts.
2. Provide inventory and sales data if the exercise requires business analysis.
3. Assign observation, analysis and recommendation tasks with shared source references.
4. Review recommendations for unsupported claims and operational constraints.

## Check your understanding

Can a shelf image alone prove that a new layout will increase revenue?

**Answer checkpoint:** No. Treat that as a hypothesis requiring appropriate data and measurement.

## Common mistake

Multimodal inputs expand available evidence but can also introduce interpretation errors.

## IBM sources and implementation guides

- [S071: What is crewAI? | IBM](https://www.ibm.com/think/topics/crew-ai)
- [S072: crewAI for retail shelf optimization tutorial | IBM](https://www.ibm.com/think/tutorials/crewai-example-multimodal-agent-retail-shelf-optimization-watsonx)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
