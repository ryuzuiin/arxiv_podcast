import openai
from config.credentials import OPENAI_API_KEY
from tqdm import tqdm 

openai.api_key = OPENAI_API_KEY

def summarize_chunks(chunks: list) -> list:
    summaries = []
    for i, chunk in enumerate(tqdm(chunks, desc="Summarizing (ChatGPT)", unit="chunk")):
        print(f"[ChatGPT] 要約中: チャンク {i+1}/{len(chunks)}")
        prompt = f"以下の医療論文の一部を日本語で簡単に要約してください：\n\n{chunk}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは日本語が得意な医学専門家です。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=800
            )
            summary = response["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"[ChatGPT] ⚠️ エラー: チャンク{i+1}: {e}")
            summary = f"[要約エラー]: {chunk[:100]}..."
        summaries.append(summary)
    return summaries

# def summarize_merged_text(text: str) -> str:
#     prompt = f"以下は医学論文の複数の要約です。重複を避け、論理的につながるように全体を日本語で簡潔にまとめてください：\n\n{text}"
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "あなたは日本語で医学講義用の講稿を構成する専門家です。"},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.2,
#             max_tokens=1200
#         )
#         return response["choices"][0]["message"]["content"]
#     except Exception as e:
#         print(f"[ChatGPT] ⚠️ 二次要約エラー: {e}")
#         return text  # fallback: return original
