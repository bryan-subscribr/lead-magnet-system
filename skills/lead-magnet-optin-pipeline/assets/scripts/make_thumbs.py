# Renders one 1280x720 branded thumbnail per training (used on /trainings-confirmed and in the delivery email).
from PIL import Image, ImageDraw, ImageFont
import os
F = "/System/Library/Fonts/Supplemental/"
BLACK, BOLD = F + "Arial Black.ttf", F + "Arial Bold.ttf"
O, Y, K, C, W = "#ED7D37", "#FBD357", "#0A0A0A", "#FFF2E8", "#FFFFFF"
TONES = [(K, W, Y), (Y, K, K), (O, K, W)]
T = [  # slug, keyword, top line, highlight line, bottom label
    ("script", "SCRIPT", "THE SCRIPT BEHIND", "923,571 VIEWS", "Jordan Welch script breakdown"),
    ("scott", "SCOTT", "DEAD CHANNEL TO", "$40,000/MONTH", "Scott Taylor case study"),
    ("million", "MILLION", "ONE VIDEO.", "1,185,797 VIEWS", "Inayah McMillan case study"),
    ("thumbnails", "THUMBNAILS", "THUMBNAILS THAT GET", "4.4x THE VIEWS", "RP Profits thumbnail formula"),
    ("algorithm", "ALGORITHM", "THE NEW RULES OF", "THE ALGORITHM", "How YouTube picks videos (for 2027)"),
    ("ideas", "IDEAS", "VIDEO IDEAS THAT", "GET YOU SALES", "How to come up with banger ideas"),
    ("edit", "EDIT", "THE EDITING CHECKLIST", "BEHIND 100M VIEWS", "For business YouTube channels"),
    ("claude", "CLAUDE", "EDIT YOUR VIDEOS", "USING CLAUDE", "Full guide, every prompt"),
    ("setup", "SETUP", "THE ONLY SETUP", "GUIDE YOU NEED", "Camera, mic and lights at 3 budgets"),
]
def fit(d, text, font_path, max_w, start):
    s = start
    while s > 20:
        f = ImageFont.truetype(font_path, s)
        if d.textlength(text, font=f) <= max_w: return f
        s -= 4
    return ImageFont.truetype(font_path, s)
out = os.path.join(os.path.dirname(__file__), "thumbs")
for i, (slug, kw, top, hi, label) in enumerate(T):
    bg, fg, acc = TONES[i % 3]
    im = Image.new("RGB", (1280, 720), bg); d = ImageDraw.Draw(im)
    # soft corner glow
    glow = Image.new("RGBA", (1280, 720), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse((820, -260, 1540, 460), fill=(237, 125, 55, 70) if bg != O else (251, 211, 87, 90))
    im.paste(glow, (0, 0), glow); d = ImageDraw.Draw(im)
    pad = 80
    kf = ImageFont.truetype(BOLD, 34)
    kw_w = d.textlength(kw, font=kf)
    d.rounded_rectangle((pad, pad, pad + kw_w + 48, pad + 62), radius=31, outline=acc, width=4)
    d.text((pad + 24, pad + 31), kw, font=kf, fill=acc, anchor="lm")
    tf = fit(d, top, BLACK, 1120, 84)
    d.text((pad, 300), top, font=tf, fill=fg, anchor="ls")
    hf = fit(d, hi, BLACK, 1080, 120)
    hb = d.textbbox((pad + 24, 330), hi, font=hf, anchor="lt")
    hl_bg = Y if bg != Y else K
    hl_fg = K if hl_bg == Y else Y
    d.rectangle((pad, hb[1] - 20, hb[2] + 24, hb[3] + 22), fill=hl_bg)
    d.text((pad + 24, 330), hi, font=hf, fill=hl_fg, anchor="lt")
    lf = ImageFont.truetype(BOLD, 38)
    d.text((pad, 640), label, font=lf, fill=fg, anchor="ls")
    vf = ImageFont.truetype(BLACK, 30)
    d.text((1280 - pad, 640), "VIRAL BANGERS", font=vf, fill=acc if bg != O else K, anchor="rs")
    im.save(os.path.join(out, f"{slug}.jpg"), quality=88)
print("ok")
