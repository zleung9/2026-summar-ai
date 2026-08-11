# CLAUDE.md

This file provides guidance to AI coding agents working in this repository.

## Project Overview

This is an **instructor's repository** for a 24-day summer course: *AI Native Machine Learning Engineer*. The course guides a student (YR) to predict polymer material properties using ML, with two parallel threads:

1. **Top-down**: Use Codex to build, inspect, debug, and review the project end-to-end
2. **Bottom-up**: Learn ML and neural network fundamentals, culminating in Transformers

`summer plan.md` is a living overview rather than a fixed syllabus. Section-level `guide.md` and `homework.md` files contain the most current details. When a section changes, update those files first and then synchronize the summary in `summer plan.md`.

## Pedagogical Model: Self-Study with Safety Net

This course is **self-study first**. The student learns independently; the teacher's role is limited to:

1. **Answering questions** when the student is stuck
2. **Solving problems** the student has tried but cannot resolve alone

The teacher does **not** lecture or deliver content. All learning materials should be designed so a motivated student can work through them without a teacher present.

This shapes everything we generate:

- **Study guides** point the student *where to look* and *what to focus on*, not lecture the content itself — prefer curated resource links and framing questions over explanations
- **Homework and tests** are the primary learning driver — they force engagement and let the student self-assess; each must have clear deliverables and acceptance criteria
- **Starter templates** provide structure and remove boilerplate, but leave the thinking to the student
- **Reference solutions** exist for the teacher to unblock students, not as study material to hand out

## Repository Structure

```
sections/          # Per-section materials (s01–s08, added as course progresses)
  s01/
    guide.md       # Study guide: what to learn, where to find it, framing questions
    homework.md    # Homework / test with deliverables and acceptance criteria
    answer-key.md  # Reference answers to homework/test questions
  ...
data/              # Polymer datasets for the course project
notebooks/         # Reference notebooks (instructor use only)
src/               # Reference Python project after refactor (Section 6)
templates/         # Starter code given to student (scaffolding, not solutions)
```

## Generating Materials

When creating content for this repo:

- Keep the scope concise. Include only enough detail to make the learning goal and workflow clear.
- Put explanations, commands, procedural instructions, resources, and troubleshooting guidance in `guide.md`.
- Keep `homework.md` direct: **Goal**, **Task**, **Deliverables**, and **Acceptance Criteria**. A short hints appendix is acceptable, but it should not turn the homework into another guide.
- Prefer a few relevant videos over long reading lists. Bilibili is the primary source for introductory tutorials; favor popular, focused videos and verify links before adding them.
- Framing questions should ask why a tool or practice matters, what problem it prevents, and how the student should judge AI output. Avoid simple recall questions.
- Favor one authentic end-to-end workflow over several disconnected documents. Whenever practical, students should learn by acting on the course repository: fork or clone it, create a branch, use Issues for questions, and submit work through a pull request.
- Demonstration code should be intentionally simple. The learning objective is the workflow or concept, not unnecessary programming difficulty.
- AI use should be explicit but critical: students inspect changes, run the work, evaluate suggestions, and remain responsible for the result.
- **Study guides** should include a topic list, a small set of recommended videos, 2–3 framing questions, practical guidance, and a concise self-check.
- **Homework and tests** must have clear deliverables and acceptance criteria. Keep the corresponding `answer-key.md` aligned when an answer key is useful.
- **Starter templates** should be incomplete enough to require thinking, but complete enough that the student isn't blocked on boilerplate
- **All student-facing text** (guides, homework, templates) is in English; variable/function names also in English
- **Reference solutions and answer keys** are for the teacher — they explain *why*, so the teacher can diagnose where a student went wrong

## Course Rhythm

Each section spans 3 days. The student works ~3 hours/day independently. The teacher holds:

- **Daily 30-min check-in** (8:00–8:30): answer questions, review blockers
- **Section-end 1-hour session**: review homework, address accumulated problems, adjust pacing if needed

## Key Constraints

- Student has ~3 hours/day; assignments must fit that budget
- The student is new to ML — framing questions in guides should use concrete examples before abstractions
- AI-generated code is expected and encouraged; the student must verify it and demonstrate understanding during check-ins
- Use `uv` for Python virtual environments and dependency management unless a later section has a specific reason to use something else
- Use VS Code for running scripts and notebooks and for introductory debugging
- scikit-learn (Sections 2–3) → PyTorch (Section 4+); don't introduce PyTorch before the deep-neural-network section
- Target property is determined by data availability in Section 2; don't assume a specific dataset upfront

## Commands

```bash
# Run reference notebooks
uv run jupyter notebook notebooks/

# Validate a reference solution
uv run pytest tests/ -v

# Run a single test
uv run pytest tests/test_data_pipeline.py::test_no_data_leakage -v
```
