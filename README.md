# Claude Code from Scratch

A minimal Python implementation of the AI coding assistant, built from the ground up. The goal was to understand how tools like Claude Code actually work under the hood (agent loops, tool execution, LLM communication) by building one myself.

## What it does

The assistant runs from the command line and takes a prompt as input:

```bash
./your_program.sh -p "Delete the old readme file."
```

It connects to an LLM via the OpenRouter API and runs an **agent loop**: it sends the prompt, checks if the model wants to use a tool, executes it, sends the result back, and repeats until the model has a final answer.

Currently supports three tools:

- **Read** — reads a file and returns its contents to the model
- **Write** — writes content to a file
- **Bash** — executes a shell command and returns the output

## Setup

Set your OpenRouter API key:

```bash
export OPENROUTER_API_KEY=your_key_here
```

Then run:

```bash
./your_program.sh -p "your prompt here"
```

## Future ideas

A few things I'm thinking about adding:

- **Session persistence** ~ save conversation history so that I can resume a previous session or pick up where I left off
- **Web search** ~ let the model search the web when it needs up-to-date information it doesn't have
- **MCP server support** ~ connect to external tools and data sources via the Model Context Protocol
- **Skills system** ~ define reusable, named capabilities the model can call on for specific tasks
