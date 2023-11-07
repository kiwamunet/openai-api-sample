import asyncio
import openai
import time
import csv
from procedures import load_api_key

async def main():

    print("open-ai testing start ......")

    # config load
    config = load_api_key(key="open-ai")
    openai.api_key = config["key"]

    # Load the CSV data
    with open('data/data.csv', newline='', encoding='utf-8') as csvfile:
        csv_data = list(csv.reader(csvfile))

    # Convert the CSV data to a string format suitable for the prompt
    csv_text = '\n'.join([','.join(row) for row in csv_data])

    start_time = time.time()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "日本語で返答してください"},
            {"role": "system", "content": "あなたは、〇〇専門AIです。"},
            {"role": "system", "content": "あなたの回答は綺麗なレポートになるように返答してください。markdownで表示します。"},
            {"role": "system", "content": "文字数は5000文字程度になるように返答してください。"},
            {"role": "user", "content": f"分析してレポートしてください。以下は利用可能なデータです。\n{csv_text}"},
        ],
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Response time: {elapsed_time:.2f} seconds")
    print(response)
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
