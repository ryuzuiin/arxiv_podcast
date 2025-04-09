import traceback

def log_start(process_name: str):
    print(f"🔹 [START] {process_name} 開始処理中...")

def log_success(process_name: str):
    print(f"✅ [SUCCESS] {process_name} 完了")

def log_failure(process_name: str, error: Exception):
    print(f"❌ [FAILURE] {process_name} 失敗: {error}")
    print(traceback.format_exc())

def run_pipeline_by_mode(mode: str, article_id: str, source_type: str = "html", file_path: str = None):
    if mode == "A":
        from controllers.controller_A import run_pipeline as run_A
        try:
            log_start("A線（全文処理）")
            run_A(article_id=article_id, source_type=source_type, file_path=file_path)
            log_success("A線")
        except Exception as e:
            log_failure("A線", e)

    elif mode == "B":
        from controllers.controller_B import run_pipeline as run_B
        try:
            log_start("B線（要約処理）")
            run_B(article_id=article_id)
            log_success("B線")
        except Exception as e:
            log_failure("B線", e)

    elif mode == "C":
        from controllers.controller_C import run_pipeline as run_C
        try:
            log_start("C線（拡張処理）")
            run_C(article_id=article_id)
            log_success("C線")
        except Exception as e:
            log_failure("C線", e)

    else:
        print(f"⚠️ 無効なモード指定: {mode}")
