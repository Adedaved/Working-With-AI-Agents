# Agent control plane

[Chapter overview](README.md) | [Course home](../README.md)

## In plain English

A control plane manages agents across an organization: deployment, configuration, policy, monitoring and ownership. The data plane is where agents perform their actual tasks. This separation helps teams manage many agents consistently while allowing their workloads to differ. A gateway typically mediates individual requests; a control plane manages the broader fleet. Keep configuration versioned so you can explain which policy and prompt a run used.

## Try it: original exercise

1. Create a registry containing each agent's owner, purpose and environment.
2. Track approved model, prompt, tool and policy versions.
3. Define release, rollback and disable procedures.
4. Review a sample run against the configuration active at its start.

## Check your understanding

Where does an agent's ticket-processing work occur?

**Answer checkpoint:** In the data plane; the control plane governs how that workload is deployed and operated.

## Common mistake

A centralized dashboard without enforced ownership or policy is only partial management.

## IBM sources and implementation guides

- [S034: What is an Agent Control Plane? | IBM](https://www.ibm.com/think/topics/agent-control-plane)

The explanation and exercise are original educational writing. Linked IBM implementation guides provide their own prerequisites, code and platform setup; those external labs have not been executed as part of this repository build.
