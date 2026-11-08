"""生成 A1 项目标签打印页（纯标准库，无第三方依赖）。

版式：A4 黑白，标签 90x60mm，一页 2列x4行 = 8 个。
二维码：版本 1 / 21x21 / 纠错 M，内容 "xiaoxin"；打印尺寸 24mm，模块 1.14mm。
四角十字基准用于取景/ROI 校正；calibration.html 用于打印前测 px/mm。

产出：
  normal.html                 10 页 = 80 张正常版面（50 正常 + 12 脏污 + 12 折角 + 6 备用）
  missing_text.html           1 页 = 4 张（缺印：文字块缺失）
  missing_qr.html             1 页 = 4 张（缺印：二维码段缺失）
  missing_border.html         1 页 = 4 张（缺印：边框段断裂）
  calibration.html            1 页（100mm 尺 + 5mm 网格 + 一张实际尺寸标签）

打印：A4、100%/实际大小、默认边距、黑白、关页眉页脚；先打 calibration 校验。
"""

import os

# qrcode 库为 "xiaoxin" 生成的 21x21 矩阵（version 1, ERROR_CORRECT_M）
QR_MATRIX = [
    "111111101010001111111",
    "100000100001001000001",
    "101110101101101011101",
    "101110100011101011101",
    "101110100101101011101",
    "100000101101101000001",
    "111111101010101111111",
    "000000000010100000000",
    "101000110000000100101",
    "010010011001011000101",
    "101011100101110110101",
    "111101001111011011000",
    "100000110111111001010",
    "000000001100000010011",
    "111111101100001010101",
    "100000100010100101011",
    "101110100110001101001",
    "101110100111011011100",
    "101110101111110010011",
    "100000100101011001000",
    "111111101001111100001",
]

QR_X, QR_Y, QR_SIZE = 57.0, 24.0, 24.0
MOD = QR_SIZE / len(QR_MATRIX)

CSS = """
@page { size: 210mm 297mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; page-break-after: always; break-after: page; overflow: hidden; }
.page:last-child { page-break-after: auto; break-after: auto; }
.grid { display: grid; grid-template-columns: 90mm 90mm; grid-template-rows: repeat(4, 60mm); gap: 10mm; padding: 13.5mm 10mm; }
.label { width: 90mm; height: 60mm; border: 0.2mm dashed #999; position: relative; overflow: hidden; }
.label svg { display: block; width: 90mm; height: 60mm; }
.cal-page { padding: 15mm 15mm; }
.cal-page svg { display: block; width: 180mm; height: 267mm; }
"""


def fiducials() -> str:
    """四角十字基准，位于标签框外、裁切线内。"""
    arms = 1.2
    out = []
    for cx, cy in ((2.2, 2.2), (87.8, 2.2), (2.2, 57.8), (87.8, 57.8)):
        out.append(
            f'<line x1="{cx-arms:.2f}" y1="{cy}" x2="{cx+arms:.2f}" y2="{cy}" '
            f'stroke="#000" stroke-width="0.3"/>'
        )
        out.append(
            f'<line x1="{cx}" y1="{cy-arms:.2f}" x2="{cx}" y2="{cy+arms:.2f}" '
            f'stroke="#000" stroke-width="0.3"/>'
        )
    return "".join(out)


def qr_rects() -> str:
    """二维码黑色模块。"""
    out = []
    for r, row in enumerate(QR_MATRIX):
        for c, ch in enumerate(row):
            if ch == "1":
                x = QR_X + c * MOD
                y = QR_Y + r * MOD
                out.append(
                    f'<rect x="{x:.3f}" y="{y:.3f}" width="{MOD+0.02:.3f}" '
                    f'height="{MOD+0.02:.3f}" fill="#000"/>'
                )
    return "".join(out)


def label_inner(kind: str = "normal") -> str:
    """标签内部图元（坐标系 0..90 x 0..60）。kind: normal / missing_text / missing_qr / missing_border"""
    defect = {
        "normal": "",
        "missing_text": '<rect x="5.5" y="33.5" width="24" height="5.2" fill="#fff"/>',
        "missing_qr": '<rect x="64" y="30" width="8" height="8" fill="#fff"/>',
        "missing_border": '<rect x="40" y="55.2" width="14" height="3" fill="#fff"/>',
    }[kind]

    return f'''{fiducials()}
  <rect x="3.5" y="3.5" width="83" height="53" fill="none" stroke="#000" stroke-width="1.0"/>
  <rect x="6.5" y="6.5" width="7.5" height="7.5" rx="1.6" fill="#000"/>
  <text x="10.25" y="12.4" font-size="5.6" font-weight="bold" text-anchor="middle" font-family="Arial, sans-serif" fill="#fff">x</text>
  <text x="16.5" y="12.6" font-size="6.6" font-weight="bold" font-family="Arial, sans-serif" fill="#000" letter-spacing="0.15">xiaoxin</text>
  <text x="16.5" y="16.8" font-size="1.85" font-family="Arial, sans-serif" fill="#333" letter-spacing="0.55">INDUSTRIAL PRECISION LABEL</text>
  <rect x="68" y="6.3" width="15.5" height="7" rx="1.2" fill="#000"/>
  <text x="75.75" y="11.1" font-size="2.3" font-family="Arial, sans-serif" fill="#fff" text-anchor="middle" letter-spacing="0.25">QC PASS</text>
  <line x1="6.5" y1="19.2" x2="51" y2="19.2" stroke="#000" stroke-width="0.25"/>
  {qr_rects()}
  <text x="6.5" y="31" font-size="2.8" font-family="Arial, sans-serif" fill="#000">MODEL  LB-10A</text>
  <text x="6.5" y="37" font-size="2.8" font-family="Arial, sans-serif" fill="#000">LOT  20261102-A</text>
  <text x="6.5" y="43" font-size="2.8" font-family="Arial, sans-serif" fill="#000">DATE  2026-11-02</text>
  <text x="6.5" y="51.5" font-size="2.6" font-family="Arial, sans-serif" fill="#000" letter-spacing="0.3">SCAN: xiaoxin</text>
  <text x="6.5" y="55.5" font-size="2.2" font-family="Arial, sans-serif" fill="#333">A1 · V1</text>
  {defect}'''


def label_svg(kind: str = "normal") -> str:
    """一张 90x60mm 标签。"""
    return f'<svg viewBox="0 0 90 60" xmlns="http://www.w3.org/2000/svg">{label_inner(kind)}</svg>'


def page(kind: str, count: int = 8) -> str:
    cells = "".join(f'<div class="label">{label_svg(kind)}</div>' for _ in range(count))
    cells += '<div class="label"></div>' * (8 - count)
    return f'<div class="page"><div class="grid">{cells}</div></div>'


def calibration_svg() -> str:
    """100mm 尺 + 5mm 网格 + 一张实际尺寸标签。"""
    parts = ['<svg viewBox="0 0 180 267" xmlns="http://www.w3.org/2000/svg">']
    parts.append('<text x="10" y="12" font-size="6" font-weight="bold" font-family="Arial">A1 LABEL CALIBRATION</text>')
    parts.append('<text x="10" y="19" font-size="3" font-family="Arial">PRINT AT 100% / ACTUAL SIZE. Do not use "fit to page".</text>')
    parts.append('<text x="10" y="30" font-size="3" font-family="Arial">Measure this line with a ruler: it must be exactly 100 mm.</text>')
    y = 40
    x0 = 10
    parts.append(f'<line x1="{x0}" y1="{y}" x2="{x0+100}" y2="{y}" stroke="#000" stroke-width="0.5"/>')
    for i in range(101):
        x = x0 + i
        h = 4 if i % 10 == 0 else 1.8
        parts.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-h}" stroke="#000" stroke-width="0.25"/>')
        if i % 10 == 0:
            parts.append(f'<text x="{x}" y="{y+4}" font-size="2.2" text-anchor="middle" font-family="Arial">{i}</text>')
    parts.append('<text x="10" y="58" font-size="3" font-family="Arial">5 mm grid (each square = 5 x 5 mm):</text>')
    gx, gy, n = 10, 64, 10
    parts.append(f'<rect x="{gx}" y="{gy}" width="{n*5}" height="{n*5}" fill="none" stroke="#000" stroke-width="0.3"/>')
    for i in range(1, n):
        parts.append(f'<line x1="{gx+i*5}" y1="{gy}" x2="{gx+i*5}" y2="{gy+n*5}" stroke="#999" stroke-width="0.2"/>')
        parts.append(f'<line x1="{gx}" y1="{gy+i*5}" x2="{gx+n*5}" y2="{gy+i*5}" stroke="#999" stroke-width="0.2"/>')
    parts.append('<text x="10" y="128" font-size="3" font-family="Arial">Actual label (90 x 60 mm):</text>')
    parts.append(f'<g transform="translate(10,134)">{label_inner("normal")}</g>')
    steps = [
        "1. Print this page at 100%. Measure the 100 mm line; if it is not 100 mm, fix the print scale.",
        "2. Put a ruler in the camera view at your planned distance (20 cm) and take one photo.",
        "3. Count pixels for 10 mm. Aim for >= 30 px per 10 mm (1 mm >= 3 px).",
        "4. If 1 mm < 2.5 px: move the camera closer or use a phone at 1280 x 960.",
    ]
    for i, s in enumerate(steps):
        parts.append(f'<text x="10" y="{218 + i*6}" font-size="2.8" font-family="Arial">{s}</text>')
    parts.append('</svg>')
    return "".join(parts)


def document(pages: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>A1 label</title>
<style>{CSS}</style></head>
<body>{pages}</body></html>'''


FILES = {
    "normal.html": document(page("normal") * 10),
    "missing_text.html": document(page("missing_text", 4)),
    "missing_qr.html": document(page("missing_qr", 4)),
    "missing_border.html": document(page("missing_border", 4)),
    "calibration.html": document(
        f'<div class="page cal-page">{calibration_svg()}</div>'
    ),
}


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    for name, html in FILES.items():
        path = os.path.join(here, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("written:", path)


if __name__ == "__main__":
    main()
