# コード解説ドキュメント

## 概要

このスクリプトは、OpenAI の GPT-4 モデルを使用して、与えられた CSV データの内容を解析し、日本語でマークダウン形式のレポートを生成することを目的としています。

## 必要なライブラリ

- `asyncio`: 非同期処理を行うためのライブラリ。
- `openai`: OpenAI の API を呼び出すためのライブラリ。
- `time`: 処理時間を計測するために使用。
- `csv`: CSV ファイルを扱うためのライブラリ。

## スクリプトの流れ

1. `asyncio`を使って非同期の`main`関数を定義します。
2. OpenAI の API キーを`load_api_key`関数から読み込みます。
3. CSV ファイル(`data/data.csv`)を読み込み、テキスト形式に変換します。
4. 処理開始時間を記録します。
5. OpenAI の`ChatCompletion` API を呼び出し、必要な情報と CSV データを含むプロンプトを送信します。
6. 処理終了時間を記録し、経過時間を計算します。
7. API からのレスポンスを表示します。

## 詳細なコード解説

### `async def main():`

- この関数は、スクリプトの主要な処理を非同期的に実行するためのものです。

### API キーの読み込み

```
config = load_api_key(key="open-ai")
openai.api_key = config["key"]
```

load_api_key 関数を使って"open-ai"というキー名で API キーを読み込み、openai.api_key に設定します。

### CSV データの読み込み

```
with open('data/data.csv', newline='', encoding='utf-8') as csvfile:
csv_data = list(csv.reader(csvfile))
csv_text = '\n'.join([','.join(row) for row in csv_data])
```

CSV ファイルを開き、その内容をリストに変換してから、CSV データを文字列形式に変換します。

### OpenAI API の呼び出し

```
response = openai.ChatCompletion.create(
model="gpt-4",
messages=[...]
)
```

ChatCompletion.create 関数を使用して、指定されたメッセージとともに API リクエストを行います。

### 処理時間の計測

```
start_time = time.time()
# API リクエストを送る処理
end_time = time.time()
elapsed_time = end_time - start_time
time.time()を使用して処理開始前と終了後のタイムスタンプを取得し、その差分で処理時間を計測します。
```

### レスポンスの表示

```
print(f"Response time: {elapsed_time:.2f} seconds")
print(response)
print(response["choices"][0]["message"]["content"])
```

処理時間と API からのレスポンス内容をコンソールに表示します。

### 実行方法

このスクリプトは、コマンドラインから以下のコマンドを実行することで起動します。

```
python main.py
```
