# 🤖 GitHub Management AI Agent

A CLI-based AI agent that integrates with the GitHub API to audit, sync, and manage repositories end-to-end. The system combines filesystem inspection, Git operations, and LLM-driven reasoning to detect version drift, automate repository workflows, and provide structured insights.

---

## 🚀 Features

- **AI-Powered Repository Auditing**
  - Scans local filesystem to detect Git repositories
  - Compares local vs remote commits to identify version drift
  - Flags dirty working directories and branch inconsistencies

- **Autonomous Sync & Lifecycle Management**
  - Pulls latest changes for out-of-sync repositories
  - Initializes new GitHub repositories programmatically
  - Supports full repository lifecycle via CLI commands

- **LLM Agent with Tool Calling**
  - Uses an LLM to dynamically decide which actions to take
  - Executes multi-step workflows (scan → compare → fix)
  - Supports natural language commands for repo management

- **Structured CLI Reporting**
  - Outputs clean, readable audit results
  - Designed for extensibility into JSON-based reporting

---
