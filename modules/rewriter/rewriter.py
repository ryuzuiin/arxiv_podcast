# ✅ modules/rewriter/rewriter.py
def rewrite_insights_to_script(insights: dict, tone: str = "neutral") -> str:
    """
    Convert structured insights (JSON形式) into natural-sounding Japanese podcast script.
    tone: "neutral" | "friendly" | "clinical"
    """
    if not isinstance(insights, dict) or not insights:
        return "この論文の要約情報が見つかりませんでした。"

    lines = ["こんにちは。今日は、最新の医学研究をご紹介します。\n"]

    if "背景" in insights:
        lines.append(f"まず背景ですが、{insights['背景']}。")

    if "目的" in insights:
        lines.append(f"この研究の目的は、{insights['目的']}。")

    if "方法" in insights:
        lines.append(f"研究では、{insights['方法']}という手法が用いられました。")

    if "結果" in insights:
        lines.append(f"その結果、{insights['結果']}ことがわかりました。")

    if "結論" in insights:
        lines.append(f"結論としては、{insights['結論']}という点が挙げられます。")

    if "臨床的意義" in insights:
        lines.append(f"この発見は、臨床的には{insights['臨床的意義']}点で重要です。")

    if "革新性" in insights:
        lines.append(f"さらに、新規性としては{insights['革新性']}が注目されます。")

    lines.append("\n以上、論文の概要でした。ありがとうございました。")
    return "\n".join(lines)
