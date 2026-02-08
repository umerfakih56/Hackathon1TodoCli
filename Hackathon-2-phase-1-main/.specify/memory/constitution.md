<!--
SYNC IMPACT REPORT
==================
Version Change: [Not versioned] → 1.0.0
Rationale: Initial constitution ratification establishing foundational principles for Python CLI Todo application

Modified Principles:
  - NEW: I. Code Quality & Maintainability
  - NEW: II. In-Memory Runtime Constraint
  - NEW: III. Command-Line User Experience
  - NEW: IV. Architectural Separation
  - NEW: V. Transparency & Reviewability
  - NEW: VI. Technology Compliance

Added Sections:
  - Core Principles (6 principles)
  - Development Workflow
  - Quality Gates
  - Governance

Removed Sections: None (initial version)

Template Consistency Status:
  ✅ .specify/templates/spec-template.md - Reviewed: User scenarios and functional requirements align with UX and quality principles
  ✅ .specify/templates/plan-template.md - Reviewed: Constitution Check section will reference these 6 principles; Python 3.13+ and UV noted in Technical Context
  ✅ .specify/templates/tasks-template.md - Reviewed: Task structure supports testability and separation of concerns principles
  ✅ .claude/commands/*.md - Reviewed: Agent-specific guidance aligns with transparency and spec-driven workflow

Follow-up TODOs: None - all placeholders resolved
-->

# Todo Application Constitution

## Core Principles

### I. Code Quality & Maintainability

Code MUST be readable, well-structured, and logically organized. Functions MUST follow single-responsibility principles. All code MUST adhere to PEP-8 conventions and Python best practices.

**Rationale**: Maintainability and clarity are non-negotiable for team collaboration, future extensions, and long-term sustainability. Single-responsibility and PEP-8 compliance reduce cognitive load and enable rapid onboarding.

### II. In-Memory Runtime Constraint

All application data MUST exist only in memory during execution. File system, database, or external persistence mechanisms are PROHIBITED.

**Rationale**: This constraint simplifies deployment, removes external dependencies, and ensures fast, deterministic behavior. It aligns with the CLI's transient-session nature and reduces attack surface.

### III. Command-Line User Experience

CLI commands MUST be simple, predictable, and self-explanatory. Output MUST be clearly formatted and easy to read. Invalid input MUST be handled gracefully with meaningful feedback.

**Rationale**: A well-designed CLI reduces user friction, minimizes support burden, and enhances user satisfaction. Clear error messages and predictable behavior build user trust and productivity.

### IV. Architectural Separation

There MUST be clear separation between command handling, business logic, and data models. The CLI layer MUST NOT contain business rules.

**Rationale**: Separation of concerns enables independent testing, reusability of business logic, and cleaner evolution of the CLI interface. This prevents tangled dependencies and ensures testability.

### V. Transparency & Reviewability

All development steps MUST be traceable through generated artifacts. Specifications, plans, and task breakdowns MUST be preserved for review.

**Rationale**: Traceability ensures accountability, enables audits, and supports knowledge transfer. Preserved artifacts allow teams to understand decision history and rationale at any point in the project lifecycle.

### VI. Technology Compliance

- Python version MUST be 3.13 or higher
- UV MUST be used for environment management
- Development MUST be executed using Claude Code and Spec-Kit Plus

**Rationale**: Standardizing on Python 3.13+ ensures access to modern language features and performance improvements. UV provides reproducible, fast environment management. Claude Code and Spec-Kit Plus enforce spec-driven discipline and AI-augmented workflows.

## Development Workflow

All feature development MUST follow the Spec-Driven Development workflow:

1. **Specify**: Create feature specification using `/sp.specify` with prioritized user stories and acceptance criteria
2. **Plan**: Generate implementation plan using `/sp.plan` with architecture decisions and technical context
3. **Task Breakdown**: Create actionable tasks using `/sp.tasks` organized by user story priority
4. **Implement**: Execute tasks using `/sp.implement` following TDD discipline when tests are required
5. **Commit & PR**: Use `/sp.git.commit_pr` to document changes and create pull requests

**Constitution Check**: All plans MUST pass constitution compliance verification before implementation begins.

## Quality Gates

All code changes MUST satisfy these gates before merge:

- **PEP-8 Compliance**: All code formatted according to PEP-8 standards
- **No Persistence**: Static analysis confirms no file I/O, database calls, or external persistence
- **Architectural Boundaries**: CLI layer contains no business logic; separation verified
- **Error Handling**: All invalid inputs produce clear, actionable error messages
- **Documentation**: All functions and modules include docstrings; user-facing commands documented
- **Artifact Completeness**: Spec, plan, and task files exist and are current for the feature

## Governance

This Constitution supersedes all other development practices. All PRs and code reviews MUST verify compliance with these principles.

**Amendment Procedure**: Amendments require:
1. Documented justification in an ADR (Architecture Decision Record)
2. Review and approval from project maintainers
3. Migration plan for existing code if applicable
4. Version bump following semantic versioning

**Versioning Policy**:
- MAJOR: Backward-incompatible principle removals or redefinitions
- MINOR: New principles added or material expansions to existing principles
- PATCH: Clarifications, wording improvements, non-semantic refinements

**Compliance Review**: Constitution compliance MUST be checked during:
- Feature planning (`/sp.plan` command includes Constitution Check section)
- Pull request review (reviewers verify principle adherence)
- Quarterly architecture reviews (identify systemic violations)

**Runtime Guidance**: Use `CLAUDE.md` for agent-specific development instructions and workflow automation.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
