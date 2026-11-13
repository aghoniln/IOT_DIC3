import os
import subprocess
import markdown

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

base_dir = r"C:\Users\譚人傑\.gemini\antigravity\scratch\2026-11-11-DIC3-ProjectRefactor"
out_dir = os.path.join(base_dir, "delivery", "pdf")
os.makedirs(out_dir, exist_ok=True)

files_to_convert = [
    ("DESIGN.md", os.path.join(base_dir, "DESIGN.md"), os.path.join(out_dir, "DESIGN.pdf")),
    ("02-project-core-A2F-5-3-10", os.path.join(base_dir, "docs", "02-project-core-A2F-5-3-10.md"), os.path.join(out_dir, "02-project-core-A2F-5-3-10.pdf")),
    ("04-introduction", os.path.join(base_dir, "docs", "04-introduction.md"), os.path.join(out_dir, "04-introduction.pdf")),
    ("05-related-work", os.path.join(base_dir, "docs", "05-related-work.md"), os.path.join(out_dir, "05-related-work.pdf")),
    ("references", os.path.join(base_dir, "docs", "references.md"), os.path.join(out_dir, "references.pdf")),
]

html_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<style>
  @page {
    size: A4;
    margin: 20mm 18mm 20mm 18mm;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #24292e;
    background-color: #ffffff;
  }
  h1, h2, h3, h4 {
    color: #1a365d;
    font-weight: 600;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
  }
  h1 { font-size: 18pt; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; }
  h2 { font-size: 14pt; border-bottom: 1px solid #edf2f7; padding-bottom: 4px; }
  h3 { font-size: 12pt; }
  p, li {
    margin-top: 0;
    margin-bottom: 10px;
  }
  code {
    font-family: Consolas, "Courier New", monospace;
    font-size: 9.5pt;
    background-color: #f7fafc;
    border: 1px solid #e2e8f0;
    padding: 2px 4px;
    border-radius: 4px;
    color: #805ad5;
  }
  pre {
    background-color: #f7fafc;
    border: 1px solid #e2e8f0;
    padding: 12px;
    border-radius: 6px;
    overflow-x: auto;
    font-family: Consolas, "Courier New", monospace;
    font-size: 9pt;
    line-height: 1.45;
    page-break-inside: avoid;
  }
  pre code {
    background: transparent;
    border: none;
    padding: 0;
    color: #2d3748;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 12px;
    margin-bottom: 16px;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }
  table, th, td {
    border: 1px solid #cbd5e0;
  }
  th {
    background-color: #ebf8ff;
    color: #2b6cb0;
    font-weight: 600;
    padding: 8px 10px;
    text-align: left;
  }
  td {
    padding: 7px 10px;
    vertical-align: top;
  }
  tr:nth-child(even) {
    background-color: #f7fafc;
  }
  blockquote {
    border-left: 4px solid #3182ce;
    padding: 8px 16px;
    color: #4a5568;
    background-color: #ebf8ff;
    margin: 12px 0;
    border-radius: 0 4px 4px 0;
  }
  hr {
    border: 0;
    height: 1px;
    background: #e2e8f0;
    margin: 20px 0;
  }
</style>
</head>
<body>
__BODY__
</body>
</html>
"""

for label, src_path, pdf_path in files_to_convert:
    print(f"Converting {label}...")
    with open(src_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    full_html = html_template.replace("__TITLE__", label).replace("__BODY__", html_body)

    tmp_html = os.path.join(out_dir, f"{label}_temp.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        tmp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
    print(f"SUCCESS: Created {pdf_path}")

print("ALL CONVERSIONS COMPLETE!")