from typer import Typer


app = Typer()


@app.command()
def run():
    print("Hello from orchestrator")
