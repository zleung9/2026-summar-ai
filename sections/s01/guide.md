# Section 1: AI-Native Development & Environment Setup

> Dates: July 29 — July 31

## What This Section Is About

This section is for complete beginners. You are not expected to know Git, GitHub, terminals, virtual environments, or `uv` before you begin.

The goal is not to memorize commands. It is to understand why the tools exist, follow one complete workflow, and know how to check where you are when something goes wrong.

By the end, you should be able to:

- explain what Git, GitHub, and `uv` each do;
- reproduce the course environment on your computer;
- run and debug a Python script and notebook in VS Code; and
- submit a small change through a GitHub pull request.

## Why Learn These Tools?

### Git makes experiments safer

Imagine that you improve a notebook on Monday, break it on Tuesday, and want Monday's version back. Without Git, you may create files such as:

```text
analysis_final.ipynb
analysis_final_v2.ipynb
analysis_final_really_final.ipynb
```

Git gives the project named save points called **commits**. Each commit records what changed, when it changed, and who changed it. This lets you:

- return to an earlier working version;
- experiment on a branch without damaging the main work;
- understand how a result was produced; and
- combine work from several people.

Git is therefore not extra paperwork. It reduces fear: you can try an idea because your earlier work is recoverable.

### GitHub makes Git collaborative

**Git** runs on your computer. **GitHub** stores a remote copy of a Git repository and adds collaboration tools.

| Tool | Main purpose |
|---|---|
| Git | Track versions locally |
| GitHub repository | Share and back up the Git project online |
| Issue | Ask a question or describe work to be done |
| Branch | Work on a change without altering the main line |
| Pull request | Propose a branch for review and discussion |

A pull request is not merely a file upload. It shows the exact changes, preserves the discussion, and lets another person review the work before merging it.

### `uv` makes Python environments reproducible

A Python project normally needs packages such as pandas, scikit-learn, and PyTorch. Installing everything globally creates problems:

- two projects may require different package versions;
- code may work on one computer but fail on another;
- it becomes unclear which Python interpreter is running the code; and
- reinstalling the project becomes slow and error-prone.

`uv` manages Python, packages, and an isolated **virtual environment** for the project. In this repository:

| Item | Meaning |
|---|---|
| `.python-version` | The Python version selected for the course |
| `pyproject.toml` | The direct packages the course requires |
| `uv.lock` | The exact resolved versions for reproducibility |
| `.venv/` | Your local, isolated Python environment |

The first three files are shared through Git. `.venv/` is created separately on each computer and is not committed.

The practical benefit is simple: instead of manually installing many packages, a student runs one command:

```bash
uv sync
```

Then everyone works from the same declared environment.

## Before Typing Commands

- Open a terminal in VS Code with **Terminal → New Terminal**.
- Type one command at a time and press Enter.
- Read the output before continuing.
- Text such as `<github-username>` is a placeholder. Replace it, including the angle brackets, with your own value.
- Commands are run from the repository root unless a step says otherwise.
- If a command fails, do not repeat it blindly. Copy the command and complete error message into a GitHub Issue.

Useful orientation commands:

```bash
pwd
ls
```

On Windows PowerShell, use `Get-Location` instead of `pwd` if necessary. You are in the repository root when `README.md`, `pyproject.toml`, and `sections/` are visible.

## Part 1: Install and Understand Git

### Step 1 — Create the accounts and applications

1. Create a [GitHub account](https://github.com/signup).
2. Install [VS Code](https://code.visualstudio.com/Download).
3. Install Git:
   - **Windows:** install [Git for Windows](https://git-scm.com/download/win) using the default options.
   - **macOS:** run `git --version`. If macOS offers to install Command Line Tools, accept. You may also use the [official installer](https://git-scm.com/download/mac).
   - **Ubuntu/Debian:** run `sudo apt update`, then `sudo apt install git`.
4. Restart VS Code after installation.

Check the installation:

```bash
git --version
```

Expected result: a line beginning with `git version`.

### Step 2 — Tell Git who you are

Commits record an author. Set this once on your computer, using the name and email associated with GitHub:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Check the result:

```bash
git config --global user.name
git config --global user.email
```

### Step 3 — Learn the three Git states

Most daily Git work follows this movement:

```text
working files  →  staging area  →  commit history
     edit          git add          git commit
```

- **Working files:** files you are currently changing.
- **Staging area:** the exact changes selected for the next save point.
- **Commit history:** saved checkpoints with messages.

The most useful command for a beginner is:

```bash
git status
```

Run it whenever you are unsure. It tells you the branch, changed files, staged files, and untracked files.

### Step 4 — Practise reading Git without changing anything

After cloning the course repository later, try:

```bash
git status
git log --oneline -5
git branch --show-current
```

These commands are read-only. They answer:

- What has changed?
- What are the latest save points?
- Which branch am I on?

## Part 2: Install and Understand `uv`

### Step 1 — Install `uv`

Use one method for your operating system.

**Windows PowerShell:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS or Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen the terminal, then check:

```bash
uv --version
```

If the terminal says `uv: command not found` or “not recognized,” restart VS Code first. If it still fails, include a screenshot or the full message in an Issue.

### Step 2 — Understand the two commands used most often

```bash
uv sync
uv run python your_script.py
```

- `uv sync` reads `pyproject.toml` and `uv.lock`, creates `.venv/` if needed, and installs the course dependencies.
- `uv run ...` runs a command inside the correct project environment. You do not need to activate the virtual environment manually.

This course repository is already a `uv` project. Do **not** run `uv init`, and do not install the course packages one by one.

### Step 3 — Build the course environment

From the repository root, run:

```bash
uv sync
```

The first run may download Python and many packages. Later runs are usually much faster.

Check that you are using the course Python:

```bash
uv run python --version
```

Check a course package:

```bash
uv run python -c "import pandas; print(pandas.__version__)"
```

Expected result: both commands print a version without an error.

### Step 4 — Connect the environment to VS Code

1. Install Microsoft's **Python** and **Jupyter** extensions in VS Code.
2. Open the Command Palette: `Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows/Linux.
3. Choose **Python: Select Interpreter**.
4. Select the interpreter inside the repository's `.venv` folder.
5. When opening a notebook, choose the same `.venv` environment as its kernel.

If VS Code cannot import a package but `uv run` can, VS Code is probably using the wrong interpreter.

## Part 3: Complete GitHub Workflow, Step by Step

### Step 1 — Fork the course repository

1. Open the course repository on GitHub.
2. Select **Fork**.
3. Keep the default settings and create the fork.

Your fork is your online working copy. The instructor's repository remains the source project.

### Step 2 — Clone your fork

On your fork's GitHub page, select **Code**, copy the HTTPS URL, and run:

```bash
git clone https://github.com/<github-username>/2026-summar-ai.git
cd 2026-summar-ai
```

`clone` creates a local folder, downloads the files and history, and names your fork `origin`.

Check:

```bash
git status
git remote -v
```

### Step 3 — Add the instructor repository

Add the instructor repository under the conventional name `upstream`:

```bash
git remote add upstream https://github.com/zleung9/2026-summar-ai.git
git remote -v
```

You should now see:

- `origin` → your fork;
- `upstream` → the instructor's repository.

### Step 4 — Create your branch

```bash
git switch -c s01/<github-username>
git branch --show-current
```

A branch is a safe workspace for one change. The second command should print the branch name you just created.

### Step 5 — Set up Python

```bash
uv sync
uv run python --version
```

Select `.venv` as the VS Code interpreter before running the script or notebook.

### Step 6 — Create the demonstration

Create your personal folder and these two files:

```text
sections/s01/submissions/<github-username>/polymer_demo.py
sections/s01/submissions/<github-username>/polymer_demo.ipynb
```

Use this small dataset:

```python
polymers = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}
```

Both files should calculate and display the polymer count and average glass-transition temperature (`Tg`). The notebook should use more than one code cell and include a Markdown explanation.

Run the script:

```bash
uv run python sections/s01/submissions/<github-username>/polymer_demo.py
```

Then run every notebook cell with the `.venv` kernel.

### Step 7 — Use the debugger

1. Open `polymer_demo.py` in VS Code.
2. Click to the left of the average-calculation line to create a red breakpoint.
3. Open **Run and Debug** and choose **Python File**.
4. When execution pauses, inspect `polymers` and `polymers.values()`.
5. Continue execution and confirm the final result.

### Step 8 — Review the change before saving it

```bash
git status
git diff
```

Ask Codex to review the script and notebook for correctness and clarity. Decide whether to accept, modify, or reject each suggestion. You remain responsible for the result.

### Step 9 — Stage and commit your files

Replace the username, then run:

```bash
git add sections/s01/submissions/<github-username>/
git status
git commit -m "Complete Section 1 polymer demonstration"
```

`git add` selects the files for the next commit. `git commit` creates the local save point. It does not yet upload anything.

### Step 10 — Push the branch

```bash
git push -u origin s01/<github-username>
```

`push` uploads your local commits to the matching branch on your GitHub fork. The `-u` option connects the local and remote branches, so later pushes can use only `git push`.

### Step 11 — Open the pull request

1. Open your fork on GitHub.
2. Select **Compare & pull request**.
3. Confirm that the change targets the instructor's repository.
4. Summarize what you created and how you tested it.
5. Include the debugger observation and your decision about one Codex suggestion.
6. Create the pull request.

After review feedback, edit the same local files, commit again, and push to the same branch. The pull request updates automatically.

## Asking for Help with Issues

Getting stuck is part of learning the workflow. A useful Issue should contain:

- a descriptive title;
- what you were trying to do;
- the exact command you ran;
- the complete error message;
- what you already tried; and
- your operating system plus `git --version` or `uv --version` when relevant.

Do not post passwords, access tokens, API keys, or private personal information.

## Common Problems

| Symptom | Likely cause | First check |
|---|---|---|
| `git` or `uv` is not recognized | Installation path has not reached the terminal | Restart VS Code and run the version command |
| `uv sync` cannot find a project | Terminal is in the wrong folder | Run `pwd` and `ls`; look for `pyproject.toml` |
| `ModuleNotFoundError` in terminal | Script ran outside the course environment | Use `uv run python ...` |
| Import error only in VS Code | Wrong interpreter or notebook kernel | Select the repository's `.venv` |
| Git asks who you are | Name/email are not configured | Run the two `git config --global` commands |
| `nothing to commit` | Files were not changed, saved, or are in another folder | Run `git status` and check the path |
| Push authentication fails | GitHub sign-in or credentials are incomplete | Sign in to GitHub in VS Code; copy the full error into an Issue |
| You are afraid a Git command will lose work | The repository state is unclear | Stop and run `git status`; ask before using destructive commands |

Never solve a beginner Git problem with `git reset --hard`, forced pushing, or deleting `.git` unless the instructor explicitly directs you.

## Beginner Cheat Sheet

| Command | Plain-language meaning |
|---|---|
| `git status` | Show where I am and what changed |
| `git diff` | Show unsaved-to-Git changes line by line |
| `git add <path>` | Select changes for the next save point |
| `git commit -m "message"` | Create a local save point |
| `git push` | Upload local commits |
| `git log --oneline -5` | Show the latest five save points |
| `uv sync` | Create/update the course environment |
| `uv run python file.py` | Run Python in the course environment |
| `uv tree --depth 1` | Show the main installed course packages |

## Recommended Resources

Use these only when you need another explanation or demonstration.

### Videos

- [简单明了的 Git 入门](https://www.bilibili.com/video/BV1Cr4y1J7iQ/) — Short overview of version control and everyday Git.
- [最简单的 GitHub 入门教程](https://www.bilibili.com/video/av4857819/) — Focus on branches, pull requests, and Issues.
- [虚拟环境：你肯定用过，但不一定了解](https://www.bilibili.com/video/BV1MLkmY4E3t/) — Why isolated Python environments exist.
- [从 pip 到 uv：现代 Python 项目管理](https://www.bilibili.com/video/BV13WGHz8EEz/) — Dependencies, lockfiles, and `uv`.
- [基于 VS Code 实现 Python 开发与调试](https://www.bilibili.com/video/BV18jq8YNE8t/) — Running Python and using the debugger.
- [VS Code + Jupyter 笔记本](https://www.bilibili.com/video/BV1itADeqEB3/) — Running notebooks inside VS Code.

### Official References

- [Git downloads](https://git-scm.com/downloads) and [first-time configuration](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
- [GitHub: cloning and getting remote changes](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)
- [`uv` installation](https://docs.astral.sh/uv/getting-started/installation/) and [working with projects](https://docs.astral.sh/uv/guides/projects/)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)

## Framing Questions

1. **What failure does each tool prevent?** Give one concrete example for Git and one for `uv`.
2. **Where does your work exist?** Explain the difference among your working files, a Git commit, your GitHub fork, and the instructor's repository.
3. **When AI writes the code, who is responsible?** What evidence would make you trust an AI-generated change?

## Self-Check

- [ ] I can explain Git versus GitHub without using the words “basically the same.”
- [ ] I can explain `pyproject.toml`, `uv.lock`, and `.venv` in plain language.
- [ ] I can use `git status` to identify my branch and changed files.
- [ ] I can reproduce the course environment with `uv sync`.
- [ ] I can run a script with `uv run` and select `.venv` in VS Code.
- [ ] I can create a branch, commit my own folder, push it, and open a pull request.
- [ ] I can use a breakpoint to inspect a variable.
- [ ] I can write a useful Issue without exposing secrets.
- [ ] I can critically evaluate a Codex suggestion instead of accepting it automatically.

**You know enough when:** you can explain why each step exists while taking a small Python change from your computer to a reviewed pull request.
