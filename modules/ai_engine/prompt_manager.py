PROMPT_TEMPLATES = {
    "insight_extraction": {
        "ja": """以下は医学論文の複数の要約です。これらを読み取り、次の観点から日本語で簡潔に要約し、**構造化されたJSON形式**で出力してください。JSON形式では、各観点をキー、対応する内容を値としてください。

要求される観点（JSONのキー）:
- 背景
- 目的
- 方法
- 結果
- 結論
- 臨床的意義
- 革新性

出力形式の例：
{{
  "要約の洞察": {{
    "背景": "...",
    "目的": "...",
    "方法": "...",
    "結果": "...",
    "結論": "...",
    "臨床的意義": "...",
    "革新性": "..."
  }}
}}

==== 要約一覧 ====
{context}
""",

        "en": """Below are multiple summaries from a medical research paper. Please extract key insights and output them in **structured JSON format** using the following keys:

- Background
- Objective
- Methods
- Findings
- Conclusion
- Clinical Significance
- Novelty

Example format:
{{
  "insights": {{
    "Background": "...",
    "Objective": "...",
    "Methods": "...",
    "Findings": "...",
    "Conclusion": "...",
    "Clinical Significance": "...",
    "Novelty": "..."
  }}
}}

==== Summaries ====
{context}
"""
    }
}

def get_prompt(task: str, context: str, lang: str = "ja") -> str:
    try:
        template = PROMPT_TEMPLATES[task][lang]
        return template.format(context=context)
    except KeyError:
        raise ValueError(f"No prompt template found for task='{task}', lang='{lang}'")
