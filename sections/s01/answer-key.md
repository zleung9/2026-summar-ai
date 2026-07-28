# Section 1 Answer Key

(For teacher use only — do not share with students)

---

## What This Section Tests

Section 1 is not about ML knowledge — it's about readiness. The four homework tasks check whether the student can:

1. Set up and verify a working development environment
2. Use Git and GitHub for version control
3. Communicate effectively with an AI coding assistant
4. Break a large, unfamiliar project into manageable pieces

A student who completes all four tasks successfully is ready to start the technical work in Section 2. A student who struggles with any of them will have compounding problems later — address these now.

---

## Task 1: Development Environment Installation Record

### What to look for

| Element | What matters | Red flags |
|---------|-------------|-----------|
| Python version | 3.10 or higher | Python 2.x, or no version listed |
| Virtual environment | They can create and activate one | They don't mention venv at all |
| Git | Version listed, basic config done | No `user.name` / `user.email` set |
| Claude Code | They've run it and gotten output | They only describe it, no evidence of use |
| Issue documentation | Specific error message + specific fix | "Everything worked fine" or "I had some problems but figured it out" |

### Why this matters

This is a diagnostic task. A student who can't set up their environment independently will be stuck every section. The "one issue" requirement is deliberate — there is always an issue, and students who don't record one are either not paying attention or not being honest. Both are problems.

If a student's only issue is "I forgot to activate the venv" — that's fine. The point is that they noticed, diagnosed, and fixed it.

---

## Task 2: First GitHub Repository

### What to look for

| Element | What matters | Red flags |
|---------|-------------|-----------|
| README | Clear purpose, student's name, what the project is | Empty or auto-generated GitHub template README |
| .gitignore | Covers Python essentials | No `.gitignore`, or one that ignores nothing Python-specific |
| Commit history | 3+ commits with meaningful messages | One giant "initial commit," or messages like "update," "fix," "aaa" |
| Repository structure | Has `sections/s01/` with `env-setup.md` | Flat structure, all files in root |

### Why this matters

This task establishes the habit of version-controlling everything from day one. The 3-commit minimum forces the student to commit incrementally rather than dumping everything at the deadline. The meaningful-message requirement introduces the idea that commit history is communication.

If the student's commits are all within 5 minutes of each other at 11:55 PM on the due date, that's worth a conversation about work habits — not a grade deduction, but a coaching moment.

---

## Task 3: Personal Learning Plan

### What to look for

| Element | What matters | Red flags |
|---------|-------------|-----------|
| Self-assessment | Honest, specific about what they do/don't know | Vague ("I know some programming"), or clearly overconfident |
| Weekly schedule | Specific days and time blocks | "3 hours a day" with no days or times — this plan will not survive contact with reality |
| Section goals | Personal, not copied from the course plan | Paraphrased course topics ("I want to learn about neural networks") with no personal angle |
| Risk list | Concrete risks + concrete mitigations | "I might get busy" with no mitigation — that's a wish, not a plan |
| Prompts used | Shows iteration — prompts evolved based on output | Only one prompt, or all prompts are near-identical |

### Why this matters

The learning plan serves two purposes. First, it's metacognitive — the student thinks about how they learn best. Second, it's a commitment device — writing down a schedule makes it real.

The prompt documentation is the hidden assessment here. A student who pastes one prompt and says "it worked" hasn't learned the core skill of this section: iterating with AI. A student who shows how they refined their prompt based on what the AI produced — that's the behavior we want to see.

### Sample answers worth noting

**Good self-assessment:**
> "I took one Python course two years ago but haven't used it since. I remember loops and functions but not much about libraries. Math-wise, I did calculus in high school but statistics was never my thing. I'm excited about building something real but nervous about the math in the later sections."

This is specific, honest, and gives the teacher something to work with.

**Weak self-assessment:**
> "I know some programming and I'm good at math."

Too vague to be useful. Ask follow-up questions at check-in.

**Good risk + mitigation:**
> "Risk: I have a part-time job that sometimes calls me in for extra shifts. Mitigation: I'll keep Saturday mornings as buffer time. If I miss a weekday session, I move it to Saturday, not skip it."

Specific risk, specific response, accountability built in.

**Weak risk + mitigation:**
> "Risk: Procrastination. Mitigation: I'll try not to procrastinate."

No mechanism. Ask: "What will you do when you notice you're procrastinating? What's the trigger that tells you it's happening?"

---

## Task 4: Polymer Materials Project Task List

### What to look for

| Element | What matters | Red flags |
|---------|-------------|-----------|
| Phases | 4–6 logical groupings | 2 giant phases ("Preparation" and "Everything Else"), or 15 tiny ones |
| Tasks per phase | 3–8 specific, actionable tasks | Tasks like "Do the ML stuff" or "Make it better" — not actionable |
| Dependencies | Shows awareness of what must precede what | No dependencies at all (everything can be done in any order — unlikely) |
| Section mapping | Tasks connected to course sections | All tasks mapped to Section 8, or random mappings |

### Why this matters

This is the student's first attempt at scoping a real project. It will be wrong — probably very wrong — and that's expected. What matters is whether they've thought systematically about the problem.

At the section-end review, ask: "Which task on your list are you most uncertain about? Which one do you think you'll need to break down further?" These questions reveal whether the list is real thinking or perfunctory box-checking.

### Common student misconceptions

1. **"Data collection" as a single task** — Students often underestimate data work. Expect to see "Get polymer data" as one bullet. This is worth discussing: what does "getting data" actually involve? (Searching, downloading, understanding columns, checking for missing values, etc.)

2. **Model training as the main event** — Students often think training the model is 80% of the work. In reality, data preparation and evaluation dominate. If their task list is 70% model tasks and 30% everything else, that's a teaching opportunity.

3. **No iteration** — The task list often reads linearly: collect data → clean data → train model → done. There's no "go back and try a different approach." Ask: "Where in your plan do you stop to check if you're on the right track?"

---

## Section-End Review: Topics to Probe

At the 1-hour review session, use these questions to gauge understanding beyond the deliverables:

1. **"Show me your terminal history from one of the days."** — Reveals whether they're actually using the tools or just following instructions.

2. **"What was the worst piece of code Claude Code generated this week?"** — Tests whether they're reviewing AI output critically.

3. **"If you had to set up everything again from scratch on a new computer, how long would it take?"** — A proxy for genuine understanding vs. copy-pasting.

4. **"What's one thing you learned this section that wasn't in any of the resources I recommended?"** — Rewards curiosity and self-directed learning.

5. **"What question do you wish I had asked?"** — Often surfaces issues the student doesn't know how to bring up.

---

## Grading Notes

Section 1 is pass/fail in practice. A student either has a working environment and a coherent plan, or they don't. The four tasks are interdependent:

- If Task 1 fails (environment not working), nothing else can proceed. Stop and fix this before evaluating anything else.
- If Task 2 fails (no repo / bad Git habits), it's an easy fix — but address it now before the repo accumulates weeks of work.
- If Task 3 fails (no real learning plan), the student will drift. The plan doesn't need to be perfect, but it needs to be specific.
- If Task 4 fails (no project task list), the student hasn't engaged with the purpose of the course. This is the most concerning failure mode.

The section-end review is the real assessment. The written deliverables are conversation starters for that review.
