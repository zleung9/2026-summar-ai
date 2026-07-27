# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **instructor's repository** for a 24-day summer course: *AI Native Machine Learning Engineer*. The course guides a student (YR) to predict polymer material properties using ML, with two parallel threads:

1. **Top-down**: Use AI coding tools (Claude Code / Codex) to build the project end-to-end
2. **Bottom-up**: Learn ML and neural network fundamentals, culminating in Transformers

## Pedagogical Model: Self-Study with Safety Net

This course is **self-study first**. The student learns independently; the teacher's role is limited to:

1. **Answering questions** when the student is stuck
2. **Solving problems** the student has tried but cannot resolve alone

The teacher does **not** lecture or deliver content. All learning materials should be designed so a motivated student can work through them without a teacher present.

This shapes everything we generate:

- **Study guides** point the student *where to look* and *what to focus on*, not lecture the content itself — prefer curated resource links and framing questions over explanations
- **Homework and tests** are the primary learning driver — they force engagement and let the student self-assess; each must have clear acceptance criteria and a reference answer
- **Starter templates** provide structure and remove boilerplate, but leave the thinking to the student
- **Reference solutions** exist for the teacher to unblock students, not as study material to hand out

## Repository Structure

```
sections/          # Per-section materials (s01–s08)
  s01/
    guide.md       # Study guide: what to learn, where to find it, framing questions
    homework.md    # Homework / test with deliverables and acceptance criteria
    solution/      # Reference solution (for teacher use only)
    answer-key.md  # Reference answers to homework/test questions
  ...
data/              # Polymer datasets for the course project
notebooks/         # Reference notebooks (instructor use only)
src/               # Reference Python project after refactor (Section 6)
templates/         # Starter code given to student (scaffolding, not solutions)
```

## Generating Materials

When creating content for this repo:

- **Study guides** should include: topic list, recommended reading/watching (with specific chapters/sections), 2–3 framing questions to think about, and a "you know enough when you can answer…" checkpoint
- **Homework and tests** must have: clear deliverables, acceptance criteria, and a separate `answer-key.md` — the student should be able to judge their own progress
- **Starter templates** should be incomplete enough to require thinking, but complete enough that the student isn't blocked on boilerplate
- **All student-facing text** (guides, homework, templates) is in Chinese; variable/function names in English
- **Reference solutions and answer keys** are for the teacher — they explain *why*, so the teacher can diagnose where a student went wrong

## Course Rhythm

Each section spans 3 days. The student works ~3 hours/day independently. The teacher holds:

- **Daily 30-min check-in** (8:00–8:30): answer questions, review blockers
- **Section-end 1-hour session**: review homework, address accumulated problems, adjust pacing if needed

## Key Constraints

- Student has ~3 hours/day; assignments must fit that budget
- The student is new to ML — framing questions in guides should use concrete examples before abstractions
- AI-generated code is expected and encouraged; the student must demonstrate understanding during check-ins
- scikit-learn (Sections 2–4) → PyTorch (Section 5+); don't introduce PyTorch early
- Target property is determined by data availability in Section 2; don't assume a specific dataset upfront

## Commands

```bash
# Run reference notebooks
jupyter notebook notebooks/

# Validate a reference solution
pytest tests/ -v

# Run a single test
pytest tests/test_data_pipeline.py::test_no_data_leakage -v
```
