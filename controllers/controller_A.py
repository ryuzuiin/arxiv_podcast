# controllers/controller_A.py

from fetchers.fulltext_retriever import retrieve_fulltext
from fetchers.html_extractor import extract_html_main_text
from fetchers.pdf_extractor import extract_pdf_text
from fetchers.text_cleaner import clean_text
from modules.splitter import split_into_chunks
from modules.ai_engine.summarizer import summarize_chunks
from modules.ai_engine.insight_miner import extract_insights
from modules.rewriter.rewriter import rewrite_insights_to_script
from modules.renderer import output_markdown
from modules.tts import synthesize_speech

import time

def run_pipeline(article_id: str, source_type: str = "html", file_path: str = None):
    print(f"[A線] 処理開始: article_id={article_id}, source_type={source_type}")

    # 1. 全文取得
    if source_type == "html":
        html = retrieve_fulltext(article_id)
        raw_text = extract_html_main_text(html)
    elif source_type == "pdf" and file_path:
        raw_text = extract_pdf_text(file_path)
    else:
        raise ValueError("Invalid source_type or missing file_path for PDF")

    start = time.time()

    # 2. テキストクリーニングとチャンク分割
    cleaned = clean_text(raw_text)
    chunks = split_into_chunks(cleaned)

    # 3. 各チャンクをChatGPTで要約
    summaries = summarize_chunks(chunks)

    # 4. 要約リストからInsight抽出（構造化）
    insights = extract_insights(summaries)

    if not insights:
        print("❌ [FAILURE] Insight抽出に失敗しました。JSONの形式や内容を確認してください。")
        return

    # 5. ナチュラルなPodcastトークスクリプト生成
    spoken_text = rewrite_insights_to_script(insights, tone="neutral")

    # 6. Markdown形式で保存
    output_markdown(spoken_text, article_id)

    # 7. TTS音声生成
    synthesize_speech(spoken_text, f"data/audio/{article_id}.mp3")

    end = time.time()
    print(f"✅ [SUCCESS] A線 完了: {end - start:.2f} 秒")
