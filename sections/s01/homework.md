# Section 1 Homework

> Due: July 31 (before the section-end review session)

## What You're Submitting

Four items this section. Each one is concrete — there's a clear "done" state. If you're unsure whether something qualifies, check the acceptance criteria at the bottom of this page.

---

## Task 1: Development Environment Installation Record

**What to do:** Set up the following tools on your computer, and document the process as you go:

- Python 3.10+ (with `pip` and `venv`)
- Git
- A GitHub account
- Claude Code (or access through claude.ai/code)
- A code editor (VS Code recommended)

**Deliverable:** A file named `env-setup.md` in your course repository. It should include:

1. **Installation log** — For each tool, note: what you installed, which version, one command that confirms it works (with its output).
2. **One issue you hit** — Something that didn't work on the first try. What was the error? How did you fix it? (If everything went perfectly, you probably weren't paying attention — dig deeper.)
3. **Your terminal setup** — A screenshot or a text description of your terminal after running `python --version`, `git --version`, and `claude --version` (or equivalent).

---

## Task 2: Your First GitHub Project Repository

**What to do:** Create a GitHub repository for this course. It will hold all your work for the next 24 days.

**Deliverable:** A link to your public GitHub repository. The repo must contain:

1. **A README.md** — Describe what this repository is for. At minimum: the course name, what you're building (the polymer materials ML project), and your name.
2. **A `.gitignore`** — Use [gitignore.io](https://www.toptal.com/developers/gitignore) or ask Claude Code to generate one for Python. You should know what it ignores and why.
3. **A `sections/` directory** — With a `s01/` subdirectory containing your `env-setup.md` from Task 1.
4. **At least 3 commits** — Each with a meaningful commit message. Not "update" or "fix stuff." The commit history should tell a story.

---

## Task 3: Personal Learning Plan

**What to do:** Use Claude Code to help you create a personalized learning plan for this course. This isn't a copy of the course plan — it's *your* plan, reflecting *your* goals, *your* schedule, and *your* baseline.

**How to approach this:**

1. Tell Claude Code about yourself: your programming background (if any), your math comfort level, what you find interesting about ML, and how much time you realistically have each day.
2. Ask Claude Code to generate a learning plan that covers all 8 sections, adapted to your situation.
3. **Don't accept the first draft.** Read it critically. Ask Claude Code to adjust anything that doesn't feel right. This exercise is as much about learning to iterate with AI as it is about the plan itself.

**Deliverable:** A file named `learning-plan.md` in `sections/s01/`. It should include:

1. **Self-assessment** — A short paragraph on your current level: programming experience, math background, what you're excited about, what you're nervous about.
2. **Weekly schedule** — Which days and times you'll study. Be specific ("Monday/Wednesday/Friday 2–5 PM," not "3 hours a day").
3. **Section-by-section goals** — For each of the 8 sections, one sentence on what you personally want to get out of it. (Not what the course says you should learn — what *you* want to learn.)
4. **Risk list** — At least two things that could derail your plan, and what you'll do if they happen.
5. **The prompts you used** — At the bottom, paste the 2–3 most important prompts you gave Claude Code to create this plan. Include the one that produced the best result and the one that needed the most revision.

---

## Task 4: Polymer Materials Project Task List

**What to do:** Break the polymer materials ML project into concrete, ordered tasks.

This project spans the entire course. You don't need to know how to do each task yet — you need to know *what* needs to happen, in roughly what order. This is a planning exercise, and it's okay if the list evolves.

**How to approach this:**

1. Read the course plan in the repository. Identify every mention of the polymer materials project.
2. Ask Claude Code: "I'm building an ML project to predict polymer material properties. Based on a typical ML workflow, what are the major phases and tasks? Give me a detailed task breakdown."
3. Review the output. Remove tasks that don't apply. Add tasks specific to this course (like "write a README" and "prepare a demo"). Order them.

**Deliverable:** A file named `project-tasks.md` in `sections/s01/`. It should include:

1. **Phases** — Group tasks into 4–6 phases (e.g., "Data Preparation," "Baseline Model," "Model Improvement," "Project Polish").
2. **Tasks per phase** — Each phase should have 3–8 specific, actionable tasks. Each task should be something you could complete in 1–3 hours.
3. **Dependencies** — For each task, note which other tasks must be done first (if any).
4. **Course section mapping** — Next to each task, note which course section (1–8) you expect to tackle it in.

---

## Acceptance Criteria

Before you submit, go through this checklist. If you can check every box, you're done. If not, you know what to fix.

### Task 1 — Environment Record
- [ ] Running `python --version` prints "Python 3.10" or higher
- [ ] Running `git --version` prints a version number
- [ ] You can create and activate a Python virtual environment without looking up the commands
- [ ] `env-setup.md` includes the output of at least one verification command per tool
- [ ] `env-setup.md` describes at least one issue you encountered and how you resolved it

### Task 2 — GitHub Repository
- [ ] The repo is public and the link works (open it in an incognito window to verify)
- [ ] `README.md` explains what the repo is for and who you are
- [ ] `.gitignore` exists and covers at minimum: `__pycache__/`, `.venv/`, `.env`, `.DS_Store`
- [ ] The repo has at least 3 commits, each with a message that explains *why* the change was made

### Task 3 — Learning Plan
- [ ] `learning-plan.md` exists and is at least one page long
- [ ] It includes a concrete weekly schedule (specific days and times)
- [ ] It acknowledges specific risks and has mitigation plans
- [ ] You can point to at least one thing in the plan that changed after you asked Claude Code to revise it

### Task 4 — Project Task List
- [ ] `project-tasks.md` has at least 4 phases
- [ ] Each phase has at least 3 tasks
- [ ] Dependencies between tasks are noted (even if your guess turns out to be wrong later)
- [ ] At least half the tasks are mapped to a course section

### Overall
- [ ] All four files are committed and pushed to your GitHub repository
- [ ] You can explain — without reading from notes — what each deliverable is and why it matters
- [ ] You have at least one question written down for the section-end review session
