# Section 1 Homework

> Due: July 31, before the section-end review

## Goal

Complete one small contribution using Python, VS Code, `uv`, GitHub, and Codex.

## Task

Fork the course repository and add a simple polymer-temperature demonstration on your own branch. Create both a Python script and a Python notebook, run them, inspect the script with the debugger, and submit the work through a pull request.

If you have questions or encounter problems, ask them through GitHub Issues.

## Deliverables

Submit **one pull-request link** containing:

1. `sections/s01/submissions/<github-username>/polymer_demo.py`
2. `sections/s01/submissions/<github-username>/polymer_demo.ipynb`
3. A short pull-request description covering:
   - How you verified both files
   - What you inspected with the VS Code debugger
   - One Codex suggestion you accepted, changed, or rejected
   - Links to any GitHub Issues you opened, or “None”

## Acceptance Criteria

- [ ] The work is on a branch named `s01/<github-username>`
- [ ] The project uses a `uv`-managed virtual environment
- [ ] The script prints the polymer count and average `Tg`
- [ ] The notebook produces the same result and includes a Markdown explanation
- [ ] Both files run successfully in VS Code
- [ ] The pull request includes the debugger observation and AI-review reflection
- [ ] The pull request is ready for review

## Appendix: Hints

Use three polymers with `Tg` values of `-125`, `100`, and `70`. Their average is `15.0`.

Useful commands:

```bash
git remote -v
uv sync
uv run python sections/s01/submissions/<github-username>/polymer_demo.py
```

See [guide.md](guide.md) for the complete workflow.
