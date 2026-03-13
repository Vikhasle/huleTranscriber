from openai import OpenAI
import os

def set_api_key():
    if "ANTHROPIC_API_KEY" not in os.environ:
        os.environ["ANTHROPIC_API_KEY"] = input("Enter your api key: ")


def enrich(raw_text: str) -> str:
    #prompt = f"You are a helpfull assistant which summarizes meeting transcripts. Generate a summary of the followning meeting: {}"
    client = OpenAI()
    message = client.responses.create(
            model="gpt-5.4",
            input=prompt
            )


    return raw_text


def test_interface(prompt: str) -> str:
    client = OpenAI()
    message = client.responses.create(
            model="gpt-5.4",
            input=prompt
            )

    return message.output_text


def main():
    set_api_key()
    while prompt := input('|> '):
        print(test_interface(prompt))


if __name__ == "__main__":
    main()
