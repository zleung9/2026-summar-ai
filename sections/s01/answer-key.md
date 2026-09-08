# Section 1 Answer Key

> For teacher use only — do not share with students before submission.

## What This Section Tests

Section 1 tests whether a student can complete one small, reproducible contribution using the course development workflow. It is primarily a readiness assessment rather than a programming challenge.

The student should demonstrate that they can:

1. use the repository's `uv`-managed Python environment;
2. create and run a Python script and a Jupyter notebook in VS Code;
3. inspect program state with the VS Code debugger;
4. review an AI suggestion and exercise independent judgment; and
5. submit the work through an appropriately named branch and pull request.

## Expected Deliverables

One pull request should contain exactly these two required artifacts under the student's GitHub username:

```text
sections/s01/submissions/<github-username>/polymer_demo.py
sections/s01/submissions/<github-username>/polymer_demo.ipynb
```

Additional evidence may appear in the pull-request description, but extra files are not required.

The pull request should come from:

```text
s01/<github-username>
```

It should be ready for review rather than left as a draft.

## Reference Data and Result

Both artifacts should use these three values:

| Polymer | Tg (°C) |
|---|---:|
| PE | -125 |
| PS | 100 |
| PET | 70 |

The expected count is `3`. The expected mean is:

```text
(-125 + 100 + 70) / 3 = 15.0 °C
```

Equivalent polymer names, variable names, formatting, or output wording are acceptable as long as the count, average, and units are unambiguous.

## Reference Script

One acceptable implementation is:

```python
polymers = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}

polymer_count = len(polymers)
average_tg = sum(polymers.values()) / polymer_count

print(f"Number of polymers: {polymer_count}")
print(f"Average Tg: {average_tg:.1f} °C")
```

Expected output:

```text
Number of polymers: 3
Average Tg: 15.0 °C
```

A function or `main()` wrapper is optional. Do not deduct points for keeping this beginner exercise as a short top-level script.

## Reference Notebook

The notebook should contain:

- at least one Markdown cell explaining what is being calculated;
- executable Python code using the three assigned Tg values;
- the polymer count and average Tg;
- results consistent with the script; and
- saved outputs from a restart-and-run-all execution.

A reasonable structure is:

1. Markdown title and explanation;
2. code cell defining the polymer data;
3. code cell calculating and printing the count and average; and
4. Markdown interpretation stating that the result is `3` polymers with an average Tg of `15.0 °C`.

The exact number of cells is not graded. A single well-explained code cell is acceptable.

## Reproducibility Checks

Run the script from the repository root:

```bash
uv sync
uv run python sections/s01/submissions/<github-username>/polymer_demo.py
```

For the notebook, verify all of the following:

1. it is valid notebook JSON and opens normally;
2. its kernel uses the repository's `.venv` environment;
3. **Restart Kernel and Run All Cells** completes without errors;
4. the saved output contains the count `3` and average `15.0`; and
5. no result depends on manually running cells out of order.

A notebook that can theoretically run but is submitted without saved outputs has not supplied the required runnable evidence. It must be rerun and resubmitted before the section can be marked complete.

## Debugger Evidence

The pull-request description should identify:

- where a breakpoint was placed;
- which variables were inspected; and
- what the observed values showed.

For example:

> I placed a breakpoint before calculating the average. The Variables panel showed three dictionary entries with values `-125`, `100`, and `70`. After stepping over the calculation, `polymer_count` was `3` and `average_tg` was `15.0`.

The wording need not match this example. The evidence should be specific enough to show that the student used the debugger rather than merely running the script.

## AI-Review Evidence

The pull-request description should record at least one concrete Codex suggestion and the student's decision to accept, change, or reject it.

Full-credit evidence includes:

- the specific suggestion;
- the student's decision;
- a reason tied to correctness, readability, scope, or maintainability; and
- confirmation that the final code was rerun after any change.

Acceptable example:

> Codex suggested moving the calculation into a function. I rejected this suggestion because the assignment is a nine-line beginner demonstration and the top-level version is easier to read. I still reran the script and notebook to confirm both produced the same result.

Weak evidence includes “Codex said the code was good,” an unexplained list of suggestions, or a claim that does not match the submitted files.

## Pull-Request Description Checklist

The description should include:

- how the script was run and its output;
- how the notebook was run and confirmation that it matches the script;
- the debugger breakpoint and observation;
- the Codex suggestion and the student's decision; and
- links to GitHub Issues opened for this work, or `None` if no Issue was opened.

Descriptions of problems written only inside the pull request are not GitHub Issue links. Do not require a student to invent an Issue when no question or blocker occurred.

## Grading Guidance

Use the course-wide 100-point rubric in the repository `README.md`. Apply its seven dimensions to Section 1 as follows.

| Dimension | Points | Section 1 full-credit evidence |
|---|---:|---|
| Required deliverables and scope | 10 | Both correctly named files are in the student's required directory and perform the assigned three-polymer calculation. |
| Technical correctness and reproducibility | 25 | The script runs through `uv`; the notebook is valid, runs top-to-bottom in the course environment, has saved outputs, and both report `3` and `15.0 °C`. |
| Core concepts and critical reasoning | 25 | The student can explain the dictionary, count, average, script/notebook relationship, virtual environment, breakpoint observation, and reason for the AI-review decision. |
| Evidence and evaluation | 15 | Console output, saved notebook output, debugger details, and verification statements support the student's claims. |
| Communication and organization | 10 | Names, units, Markdown explanation, code layout, and pull-request description are clear and internally consistent. |
| AI-native workflow and independent judgment | 10 | A specific Codex suggestion is documented and thoughtfully accepted, changed, or rejected; the final submission reflects the stated decision. |
| Git and professional submission workflow | 5 | The branch is `s01/<github-username>`, the pull request contains the required metadata and Issue links/`None`, and it is ready for review. |
| **Total** | **100** | |

## Completion Gates

The following failures override the numerical score and prevent the section from being marked complete:

1. **Missing core artifact:** either required file is absent, incorrectly replaced by an unrelated project, or cannot be reviewed.
2. **Missing runnable evidence:** the script fails, the notebook cannot run from a clean restart, or the notebook is not saved with outputs.
3. **Incorrect core result:** the count or average is wrong in either artifact.
4. **Missing workflow defense:** the student cannot explain the debugger observation or an important AI-generated part of the submitted work during review.
5. **Unsupported evidence:** the pull-request claims materially conflict with the submitted files or outputs and are not corrected.

A score of 80 or above counts as complete only after all applicable gates pass. A student may correct the affected evidence and request regrading.

## Common Problems and Feedback

### Correct code but notebook outputs are missing

Ask the student to select the repository `.venv` kernel, restart the kernel, run all cells, save the notebook, and update the pull request. Keep the result at **Revision required** until the saved outputs are present.

### Script and notebook use different calculations

Ask the student to make both artifacts use the assigned values and produce the same result. The notebook should not contain a manually typed result that disagrees with its code.

### Notebook is invalid or only works after out-of-order execution

Ask the student to recreate or repair the notebook, restart the kernel, run from the first cell to the last, and save it. This fails the runnable-evidence gate.

### Pull request says a suggestion was accepted, but the code does not contain it

Ask the student to reconcile the description and final files. The student may either implement the suggestion or accurately explain why it was ultimately rejected.

### Work is technically more advanced but does not answer the task

Grade the assigned scope, not effort or complexity. An unrelated simulation, report, or visualization cannot replace the required count-and-average demonstration.

### Branch name or pull-request metadata is wrong

Deduct from Git and professional workflow. If the files and execution evidence are otherwise valid, this alone does not normally fail a completion gate.

## Section-End Review Questions

Use a short live review to confirm independent understanding:

1. What problem does `uv` solve, and how do you know VS Code is using the same environment?
2. Show where you placed the breakpoint. What changed after you stepped over the average calculation?
3. Why did you accept, change, or reject the recorded Codex suggestion?
4. If a fourth polymer were added, which outputs would change and why?
5. How would you rerun both artifacts from a clean clone of the repository?

The goal is not memorization. A satisfactory answer should connect the tool or code to the concrete work the student submitted.
