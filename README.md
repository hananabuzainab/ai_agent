# AI Agent

A command-line AI coding agent built with Python and Google's Gemini API. The agent uses function calling to interact with files, execute Python scripts, and perform coding tasks based on natural language instructions.

## Features

- List files and directories.
- Read file contents.
- Create and modify files.
- Execute Python files.
- Use Gemini Function Calling to select and invoke tools.
- Support verbose mode for execution details.

## Technologies

- Python
- Google Gemini 2.5 Flash
- Google Gen AI SDK
- Function Calling
- Python-dotenv

## How It Works

The user submits a task through the command line. Gemini determines which tools are needed, the agent executes the requested functions, and sends their results back to Gemini until a final response is generated.

## Run

```bash
python main.py "Your task here"
```

For detailed execution logs:

```bash
python main.py "Your task here" --verbose
```

## Author

**Hanan Abuzainab**

[GitHub Profile](https://github.com/hananabuzainab)
