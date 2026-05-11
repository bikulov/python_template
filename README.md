# Usage

Install project and development tools:

```bash
uv sync
```

Run the CLI through the installed script entry point:

```bash
uv run python-template first_module --name ksar
[python_template.py:48] INFO     [YYYY-MM-DD HH:MM:SS]  ksar
```

Run tests:

```bash
uv run pytest
```

Format code with Ruff:

```bash
uv run ruff format .
```

Run the Ruff linter:

```bash
uv run ruff check .
```
