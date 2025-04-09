# modules/renderer.py

import os

def output_markdown(text: str, article_id: str, title: str = "医療Podcast講稿"):
    output_dir = "./data/outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{article_id}.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(text)

    print(f"[📝 Markdown出力完了] {output_path}")
