import click
from rich.console import Console
from simple_create_repo import Create_Github_Repository

@click.command()
@click.option('--token', prompt='GitHub token', help='GitHub personal access token')
@click.option('--name', prompt='Repository name', help='Name of the repository to create')
@click.option('--description', prompt='Description', help='Description of the repository')
@click.option('--private', is_flag=True, help='Create a private repository')
def main(token, name, description, private):
    console = Console()
    repo_creator = Create_Github_Repository(token)
    response_panel = repo_creator.create_repo(name, description, private)
    console.print(response_panel)

if __name__ == "__main__":
    main()
