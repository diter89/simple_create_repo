#!/usr/bin/python3
import requests 

# /// require rich 
from rich.console import Console
from rich import print
from rich.panel import Panel 

# /// class CReate ...
class Create_Github_Repository():
    def __init__(self, token: str ) -> None:
        self.token = token 

    # /// create new repo 
    def create_repo(self, name_repo: str, description: str, status: bool):
        self.name_repo = name_repo 
        self.description = description
        self.status = status

        rr = requests.post("https://api.github.com/user/repos",headers={"Authorization": "token {}".format(self.token),"Accept": "application/vnd.github.v3+json"},json={
            "name": self.name_repo,
            "description": self.description,
            "private": self.status
            })
        if rr.status_code == 201:
            return Panel("Successfuly",border_style="green bold",expand=True)
        else:
            return Panel("Failled {} && Response {}".format(rr.status_code,rr.json()),border_style="red bold",expand=True)

