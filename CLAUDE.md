# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **instructor's repository** for a 24-day summer course: *AI Native Machine Learning Engineer*. The course teaches a student (YR) to predict polymer material properties using ML, with two parallel threads:

1. **Top-down**: Use AI coding tools (Claude Code / Codex) to build the project end-to-end
2. **Bottom-up**: Learn ML and neural network fundamentals, culminating in Transformers

The repo holds **all teaching materials** — course plans, assignment specs, reference solutions, slide content, grading rubrics, and scaffolding code for the student.

## Repository Structure

```
sections/          # Per-section teaching materials (s01–s08)
  s01/             # Section 1: AI-native dev & environment setup
    assignment.md  # Assignment specification given to student
    solution/      # Reference solution (do not share with student)
    notes.md       # Teaching notes, common pitfalls, pacing tips
  ...
data/              # Polymer datasets for the course project
notebooks/         # Reference notebooks (instructor demos & solutions)
src/               # Reference Python project after refactor (Section 6)
rubrics/           # Grading rubrics per section
templates/         # Scaffolding code and starter templates given to student
```

## Teaching Workflow

Each section spans 3 days. Daily rhythm:
- **8:00–8:30**: Check-in / Q&A (review previous day's work, unblock student)
- **~45 min**: Student studies theory
- **~90 min**: Student codes with AI assistance
- **~30 min**: Student documents prompts, results, problems
- **~15 min**: Student commits code and writes learning log

Every 3 days (end of section): a 1-hour review session — check assignments, discuss design, adjust pacing.

## Generating Teaching Materials

When creating content for this repo:

- **Assignments** should state clear deliverables and acceptance criteria so the student knows when they're done
- **Reference solutions** go in `solution/` subdirectories — never in the same file as the assignment
- **Starter templates** should be incomplete enough to require thinking, but complete enough that the student isn't blocked on boilerplate
- **All student-facing text** (assignments, templates, comments in starter code) is in Chinese; variable/function names in English
- **Code comments in solutions** should explain *why* something works, not just *what* it does — the student will read these to learn
- **Grading rubrics** should map deliverables to the course plan's stated objectives per section

## Key Course Constraints

- Student has ~3 hours/day; assignments must fit that budget
- The student is new to ML — avoid jargon without definition; prefer concrete examples before abstractions
- AI-generated code is expected and encouraged, but the student must demonstrate understanding during check-ins
- The project uses scikit-learn (Sections 2–4) then PyTorch (Section 5+); don't introduce PyTorch early
- Data availability determines the target property (chosen in Section 2); don't assume a specific dataset upfront

## Commands

```bash
# Run reference notebooks
jupyter notebook notebooks/

# Validate a reference solution
pytest tests/ -v

# Run a single test
pytest tests/test_data_pipeline.py::test_no_data_leakage -v
```
