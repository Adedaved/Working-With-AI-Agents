# Repository build: actual workflow record

Date: 14 October 2026.

## Goal and approvals

The user requested an easy-to-understand tutorial in ten repository folders matching IBM's site, followed by a PDF. The user approved IBM's AI agents page as the source, original beginner exercises, and a separate branch with a pull request for review before merging.

## Inputs inspected

- Existing repository: only a title in README.md on main.
- IBM's AI agents navigation: ten instructional groups and 108 linked entries.
- Linked IBM explainers, tutorials and the redirected IBM Bob documentation.

## Decisions and corrections grounded in sources

- Overview pages map to chapter READMEs; related explainer and tutorial links share a lesson.
- Repeated Architecture and Multi-agent systems topics retain both placements with distinct emphasis.
- IBM's ACP explainer reports its merger into A2A; the tutorial retains ACP and explains its migration status.
- IBM distinguishes Microsoft AutoGen from AG2; the relevant lesson warns against assuming interchangeable package APIs.
- The local tool demo is explicitly a deterministic simulation. External IBM labs are linked learning resources and have not been provisioned or run during this build.

## Checks

Validation results are recorded below after they run. The pull request provides the actual changes for human review. Merge remains a separate approval decision.

Initial verification passed: exactly 10 chapter folders, 70 lessons, 108 source entries, 364 local Markdown links, all six synthetic ticket IDs, a correct tool calculation and rejection of three invalid call cases. No linked IBM cloud lab was executed.

## PDF export and review

The PDF was generated after the initial repository tutorial commit. Rendering exposed awkward splits between lessons and checkpoints; the layout was revised to keep each lesson together. The final export is 85 pages. Every concept paragraph and all 108 source IDs are present in the extracted text, with no replacement glyphs. All final pages were rendered and visually inspected. The source links, tables, capstone template and local code example are included.

The PDF, generator and validation record are added on the same review branch. The user must review and approve the pull request before merge to main.
