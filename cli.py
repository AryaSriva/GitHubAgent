import typer
from agent_llm import build_agent

app = typer.Typer()
agent = build_agent()


@app.command()
def run(query: str):
    response = agent.run(query)
    print(response)


if __name__ == "__main__":
    app()
