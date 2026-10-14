# Working With AI Agents

A beginner-friendly learning path following the ten topic groups in [IBM's AI agents navigation](https://www.ibm.com/think/topics/ai-agents). Learn each idea, try a short exercise, and check your understanding.

**10 chapters | 70 lessons | 108 mapped navigation entries | Source snapshot: 14 October 2026**

[Download the complete tutorial PDF (85 pages)](Working_With_AI_Agents_Tutorial.pdf)

## How to use this tutorial

1. Start with Introduction and Components.
2. Work through Architecture and Protocols to understand how actions are connected.
3. Use Lifecycle and Governance to evaluate and supervise a workflow.
4. Explore Frameworks, Agentic RAG and the application examples as needed.
5. Use the capstone template to document a real task you personally direct and review.

The conceptual lessons and synthetic exercises require no paid account. The included Python demo requires Python 3. IBM implementation labs may require separate software, model downloads or IBM services; use the prerequisites in each linked guide.

## The ten chapters

| Chapter | What you will learn |
|---|---|
| [01. Introduction](01-introduction/README.md) | Understand what agents do, how they differ from assistants, and how to define a useful first task. |
| [02. Components](02-components/README.md) | Understand the capabilities that turn a model into a system that can observe, decide and act. |
| [03. Architecture](03-architecture/README.md) | Choose how the parts fit together, how work is routed, and where execution is controlled. |
| [04. Protocols](04-protocols/README.md) | Distinguish agent-to-tool connections from agent-to-agent communication. |
| [05. Lifecycle and operations](05-lifecycle-and-operations/README.md) | Take an agent from a scoped idea through evaluation, release, operation and retirement. |
| [06. Multi-agent systems](06-multi-agent-systems/README.md) | Design collaboration around responsibilities, shared evidence and measurable outcomes. |
| [07. Frameworks](07-frameworks/README.md) | Recognize the frameworks in IBM's navigation and match their design patterns to a task. |
| [08. Governance](08-governance/README.md) | Define ownership, evaluation, security, supervision and operational accountability. |
| [09. Agentic RAG](09-agentic-rag/README.md) | Retrieve the right evidence, assess its quality, and answer within what it supports. |
| [10. Use cases and applications](10-use-cases-and-applications/README.md) | Apply the same goal-context-tools-review pattern to different business domains. |

## Practical tools

- [Capstone workflow template](CAPSTONE_WORKFLOW.md)
- [Source map: every IBM navigation entry](SOURCE_MAP.md)
- [Actual repository build log](WORKFLOW_LOG.md)
- [Tool-calling runtime demonstration](02-components/tool_calling_demo.py)
- [Synthetic ticket evaluation data](05-lifecycle-and-operations/example_tickets.csv)
- [Verification command](verify_tutorial.py)

```bash
python3 verify_tutorial.py
python3 02-components/tool_calling_demo.py
```

## Source and teaching approach

This is an independent educational tutorial, not an official IBM course or an IBM-endorsed publication. The topic structure and linked source material come from IBM; explanations, toy examples, exercises and answer checkpoints are original. IBM articles and code are linked rather than reproduced.

Overview entries map to chapter READMEs. Related explainer and implementation links share a lesson. Subjects repeated by IBM under Architecture and Multi-agent systems remain in both chapters with different teaching emphasis.

IBM's navigation spells one item "Agent gateaway"; the linked article and this tutorial use "Agent gateway." The IBM Bob MCP link redirects to Bob documentation. ACP's merger into A2A and the AutoGen/AG2 distinction are documented in the relevant lessons.

## What was actually run

Repository structure and source-coverage checks, internal-link checks, and the local deterministic tool-call demo are validated during this build. The full PDF is rendered and visually reviewed before delivery. Linked IBM cloud and framework labs are study resources; they have not been provisioned or run by this build.

## Rebuild the PDF

The PDF is generated from the same Markdown lesson files you read in the repository. Install ReportLab, then run the builder:

```bash
python3 -m pip install -r requirements-pdf.txt
python3 build_pdf.py
```

The builder uses DejaVu fonts when available and falls back to standard PDF fonts. [Recorded validation results](validation_results.json) describe the delivered version; [PDF builder](build_pdf.py) contains the export implementation.
