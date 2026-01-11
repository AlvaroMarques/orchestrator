from dagster import asset


@asset
def hello():
    print("Hello from Dagster 👋")
    return "hello"


@asset
def world(hello: str):
    print(f"{hello} world")
