# Simple Create Repo Library

A Python library to create GitHub repositories using GitHub API and rich for styling output.

## Installation

```bash
pip install simple_create_repo

...usege:

from simple_create_repo import Create_Github_Repository

token = "your_github_token"
repo_name = "my-new-repo"
description = "This is a new repository created via API"
status = False

repo_creator = Create_Github_Repository(token)
response_panel = repo_creator.create_repo(repo_name, description, status)
print(response_panel)

