# Setup Instructions

## Table of Contents

1. [Project Setup](#project-setup)
1. [Code Formatting and Quality Tools](#code-formatting-and-quality-tools)
1. [Commit Rules](#commit-rules)
1. [Directory Structure](#directory-structure)
1. [Debugging](#debugging)

## Project Setup

### Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Create Essential Files

```bash
touch .gitignore
touch requirement.txt
touch README.md
```

`.gitignore`
```
__pycache__
.DS_Store
.vscode
.gitignore
venv
```

### install essential dependencies
```bash
pip3 install fastapi uvicorn sqlalchemy python-multipart
```

## Code Formatting and Quality Tools
### Install Formatter
```bash
pip3 install black
black .
```

## Commit Rules
### Pre Commit Hook
```bash
pip3 install pre-commit
touch .pre-commit-config.yaml
pre-commit install
pre-commit run
```
