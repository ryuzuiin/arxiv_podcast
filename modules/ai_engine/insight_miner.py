import json
import openai
from modules.ai_engine.prompt_manager import get_prompt
from modules.ai_engine.insight_parser import parse_structured_text_response
from config.credentials import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_insights(summary_list: list) -> dict:
    joined = "\n\n".join(summary_list)
    prompt = get_prompt("insight_extraction", context=joined)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "あなたは優秀な医学専門のライターであり、必ず日本語の構造化JSON形式で返してください。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )

        content = response["choices"][0]["message"]["content"]
        print("[InsightMiner] raw:", content)

        # primary: JSONで処理
        insights = json.loads(content)
        if "要約の洞察" in insights and isinstance(insights["要約の洞察"], dict):
            insights = insights["要約の洞察"]

        return insights if isinstance(insights, dict) else {}

    except json.JSONDecodeError as je:
        print("[InsightMiner] JSON decode error:", je)
        print("[InsightMiner] fallback to regex parser")
        return parse_structured_text_response(content)

    except Exception as e:
        print(f"[InsightMiner] ⚠️ エラー: {e}")
        return {}

def render_insights_to_markdown(insights: dict) -> str:
    lines = ["# 医療Podcast講稿（構造化）\n"]
    for section, content in insights.items():
        lines.append(f"## {section}\n\n{content}\n")
    return "\n".join(lines)
