import argparse
from controllers.controller_utils import run_pipeline_by_mode

def main():
    parser = argparse.ArgumentParser(description="📚 PubMed Podcast Generator")
    parser.add_argument("--mode", type=str, choices=["A", "B", "C"], required=True, help="処理モード: A（全文）、B（要約）、C（拡張）")
    parser.add_argument("--article_id", type=str, required=True, help="PMC IDまたはローカルファイル名")
    parser.add_argument("--source_type", type=str, choices=["html", "pdf"], default="html", help="ソースタイプ: htmlまたはpdf")
    parser.add_argument("--file_path", type=str, default=None, help="PDFファイルのパス（source_type=pdfの場合）")

    args = parser.parse_args()
    run_pipeline_by_mode(
        mode=args.mode,
        article_id=args.article_id,
        source_type=args.source_type,
        file_path=args.file_path
    )

if __name__ == "__main__":
    main()
