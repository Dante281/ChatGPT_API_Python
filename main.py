import openai
import config
import typer
from rich import print
from rich.table import Table


def main():

    openai.api_key = config.api_key  #We call openAI through the API

    print("[bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Description")
    table.add_row("exit", "Salir de la app")
    table.add_row("new", "Nuevo Chat")

    print(table)

    # Contexto del asistente
    context = [{"role": "system", 
             "content": "Eres un asistente muy útil"}]
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":      #We start the chat from scracth
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        # https://platform.openai.com/docs/guides/chat
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": "response_content"})

        print(f"[bold green]response_content[/bold green]")


def __prompt() -> str:
        prompt = typer.prompt("\n¿sobre qué quieres hablar? ")

        if prompt == "exit":   #if we write exit we can go out from the while
            exit = typer.confirm("Estás seguro?")
            if exit:
                print("Hasta luego")
                raise typer.Abort()
            
            return __prompt()
        
        return prompt


if __name__ == "__main__":
    typer.run(main)


#tutorial by MoureDev
#https://www.youtube.com/watch?v=b8COygWdvmw
