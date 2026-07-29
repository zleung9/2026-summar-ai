# Section 1: AI-Native Development & Environment Setup

> Dates: July 29 — July 31

## What This Section Is About

Set up a reproducible Python workflow and learn how to build with AI without treating its output as automatically correct.

By the end of this section, you should be able to run and debug Python in VS Code, manage dependencies with `uv`, and contribute a small change through GitHub with help from Codex.

## Topics

- **GitHub:** forks, clones, branches, issues, pull requests, and code review
- **VS Code:** run Python scripts and notebooks; use breakpoints and the debugger
- **Python:** virtual environments, dependencies, and `uv`
- **Codex:** give context, request a change, inspect the diff, run tests, and iterate

## Three-Day Map

| Day | Focus | Output |
|---|---|---|
| 1 | Fork and clone the course repository; set up Python, `uv`, and VS Code | A working local copy and environment |
| 2 | Create and run a simple Python script and notebook | Two working Python files and debugging practice |
| 3 | Review the work with Codex and submit it through GitHub | A branch and pull request |

## Recommended Videos

Watch only what helps you complete the day's task.

### Git & GitHub

- [简单明了的 Git 入门](https://www.bilibili.com/video/BV1Cr4y1J7iQ/) — A short overview of version control and everyday Git.
- [最简单的 GitHub 入门教程](https://www.bilibili.com/video/av4857819/) — Focus on **Branches**, **Pull Requests**, and **Issues**.

### VS Code

- [基于 VS Code 实现 Python 开发与调试](https://www.bilibili.com/video/BV18jq8YNE8t/) — Watch the parts on running Python, configuring VS Code, and debugging.
- [VS Code + Jupyter 笔记本](https://www.bilibili.com/video/BV1itADeqEB3/) — A quick introduction to running notebooks inside VS Code.

### Python Environments & `uv`

- [虚拟环境：你肯定用过，但不一定了解](https://www.bilibili.com/video/BV1MLkmY4E3t/) — Explains why virtual environments exist.
- [从 pip 到 uv：现代 Python 项目管理](https://www.bilibili.com/video/BV13WGHz8EEz/) — A concise overview of dependencies, lockfiles, and `uv`.

### AI Coding

- [Codex 新手教程：22 分钟速通](https://www.bilibili.com/video/BV1MHL36QEzU/) — Use it as an orientation; learn the workflow through practice.

## Framing Questions

1. **Why do these tools exist?** What failures do Git/GitHub and `uv` prevent? Which problems are about history and collaboration, and which are about reproducibility?

2. **When AI writes the code, who is responsible for it?** What evidence—reading the diff, running the program, tests, or checking sources—would make you trust an AI-generated change?

3. **Why use both a script and a notebook?** How do their purposes differ, and when is a change ready for a pull request?

## Practical Workflow

The homework follows one contribution cycle.

### 1. Get the Repository

1. Fork the course repository on GitHub.
2. Clone your fork.
3. Add the original course repository as the `upstream` remote.
4. Create a branch named `s01/<github-username>`.

Use `git remote -v` to confirm that your fork is `origin` and the course repository is `upstream`.

### 2. Set Up Python

Create a virtual environment and install notebook support:

```bash
uv venv
uv pip install ipykernel
uv run python --version
```

Open the repository in VS Code and select the Python interpreter inside `.venv`.

### 3. Create the Demonstration

Create these two files:

```text
submissions/<github-username>/polymer_demo.py
submissions/<github-username>/polymer_demo.ipynb
```

Use this small dataset:

```python
polymers = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}
```

Both files should calculate and display the number of polymers and their average glass-transition temperature (`Tg`). The notebook should use more than one code cell and include a Markdown explanation.

Run the script in VS Code and from the terminal:

```bash
uv run python submissions/<github-username>/polymer_demo.py
```

Then run every notebook cell with the `.venv` kernel.

### 4. Debug and Review

Set a breakpoint before the average calculation. Run the VS Code debugger and inspect `polymers` or `polymers.values()`.

Ask Codex to review the script and notebook for correctness and clarity. Decide whether to accept, modify, or reject its suggestions. You remain responsible for the final result.

### 5. Ask Questions

If you get stuck, open a GitHub Issue in the course repository. Include:

- What you are trying to do
- What you already tried
- The result or error message
- Relevant Python and `uv` versions

Use the `question` label if it is available.

### 6. Submit the Change

Commit the files, push your branch to your fork, and open a pull request to the course repository. In the pull request, briefly report:

- Whether the script and notebook ran successfully
- What you inspected with the debugger
- One Codex suggestion you accepted, changed, or rejected
- Links to any Issues you opened

After receiving review feedback, update the same branch and push again. The pull request will update automatically.

## Self-Check

- [ ] Fork and clone a repository and configure its `upstream` remote
- [ ] Create and use a project environment with `uv`
- [ ] Run a Python script and notebook in VS Code
- [ ] Set a breakpoint and inspect a variable
- [ ] Create a GitHub branch and pull request
- [ ] Use a GitHub Issue to ask a clear technical question when needed
- [ ] Ask Codex to review the work and critically evaluate its suggestions
- [ ] Explain why Git, virtual environments, and human review still matter when using AI

**You know enough when:** you can reproduce a project locally, make a small change, and submit evidence that it works.
