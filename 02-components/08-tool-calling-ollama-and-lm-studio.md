# Tool calling: Ollama and LM Studio

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

Tool calling is a structured request to execute an available function. The model selects a tool and arguments; a runtime validates and executes the function, then returns its result. Ollama and LM Studio can support local model workflows, but model and runtime support must be checked. IBM's guides demonstrate local tool calling through those platforms. The essential pattern is the same: declare the capability, validate the call, execute it and feed the result back.

## Try it: original exercise

1. Run the included tool_calling_demo.py to inspect a simulated structured call.
2. Read its allowlist and argument checks before the local calculation executes.
3. For an actual local-model lab, choose either IBM's Ollama or LM Studio guide and follow its prerequisites.
4. Check that the selected model emits a tool request and that the runtime really executes it.

## Worked aid

Run from the repository root:

```bash
python3 02-components/tool_calling_demo.py
```

Expected result: `42`. No cloud account or third-party Python package is required.

## Check your understanding

Does a model outputting JSON run the function by itself?

**Answer checkpoint:** No. Host software must validate and dispatch the call, then return the observed result.

## Common mistake

The bundled demo is a deterministic runtime example, not an LLM or a complete AI agent.

## IBM sources and implementation guides

- [S027: What Is Tool Calling? | IBM](https://www.ibm.com/think/topics/tool-calling)
- [S028: Ollama tool calling | IBM](https://www.ibm.com/think/tutorials/local-tool-calling-ollama-granite)
- [S029: Use LM Studio to build automatic tool calling with Granite | IBM](https://www.ibm.com/think/tutorials/use-lm-studio-to-build-automatic-tool-calling-granite)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
