
import re

SECTION_KEYS = [
    "背景", "目的", "方法", "結果", "結論", "臨床的意義", "革新性"
]

def parse_structured_text_response(text: str) -> dict:
    """
    GPTがJSONで返さず、プレーンテキストで構造化して返した場合のパーサ。
    - 「- 背景：内容」や「背景: 内容」などの形式に対応。
    """
    insights = {}
    for key in SECTION_KEYS:
        # 「- 背景：」や「背景:」などに対応
        pattern = rf"[-・]?\s*{re.escape(key)}\s*[:：]\s*(.+)"
        match = re.search(pattern, text)
        if match:
            insights[key] = match.group(1).strip()
        else:
            insights[key] = "（未抽出）"

    return insights
