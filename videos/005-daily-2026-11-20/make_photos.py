"""Composites the user-supplied photos into 1920x1080 backdrops: project/assets/scenes/<key>.jpg"""
import os
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance
U = "/root/.claude/uploads/ae63adea-d217-590d-8f90-e5beeb8bb831/"
IDS = "77e33a7d dca1e9aa 8f702c36 0a034cb2 dfbcd3c1 026d4e87 ef0ab982 5cc567e9 3e5d59d3 9dacf694 1409f7bc b3ccb20e 2c51f6f8 d2ee2874 0ce596cd".split()
KEYS = {1: ["intro", "outro"], 2: ["summit"], 3: ["icj"], 4: ["quad"], 5: ["tara"], 6: ["mahanadi"], 7: ["akvan"], 8: ["uproll"], 9: ["ladakh"],
        11: ["khet"], 12: ["q1"], 13: ["q2"], 15: ["q4"]}   # 10 (Ellora temple) and 14 (US Supreme Court) are not used: wrong subject
OUT = "project/assets/scenes"
os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080


def cover(im, w=W, h=H):
    r = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * r) + 1, round(im.height * r) + 1), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def framed(im, fw=1300, fh=470, cy=520):
    bg = cover(im).filter(ImageFilter.GaussianBlur(40))
    bg = ImageEnhance.Brightness(bg).enhance(0.55)
    r = min(fw / im.width, fh / im.height)
    pw, ph = round(im.width * r), round(im.height * r)
    p = im.resize((pw, ph), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 80, 2))
    x, y = (W - pw) // 2, cy - ph // 2
    d = ImageDraw.Draw(bg)
    d.rectangle((x - 8, y - 8, x + pw + 8, y + ph + 8), fill=(255, 255, 255))
    bg.paste(p, (x, y))
    return bg


for n, keys in KEYS.items():
    im = Image.open(f"{U}{IDS[n - 1]}-image.png")
    if n == 1:  # Earth: on black with stars, big on the right
        bg = Image.new("RGB", (W, H), (4, 6, 18))
        d = ImageDraw.Draw(bg)
        import random
        r = random.Random(3)
        for _ in range(160):
            d.ellipse((lambda x, y, s: (x, y, x + s, y + s))(r.randint(0, W), r.randint(0, 800), r.choice([2, 3, 4])), fill=(255, 255, 255))
        g = im.crop((60, 55, 900, 895)).resize((600, 600), Image.LANCZOS)
        m = Image.new('L', (600, 600), 0); ImageDraw.Draw(m).ellipse((6, 6, 594, 594), fill=255)
        bg.paste(g, (W // 2 - 300, 150), m.filter(ImageFilter.GaussianBlur(3)))
        out = bg
    elif n == 4:  # Manila Bay (portrait satellite, caption baked in at the bottom): crop the bay, no caption
        out = framed(im.crop((0, 120, 960, 120 + 540)), 1500, 470)
    elif n == 12:  # Voyager: transparent cut-out on a dark starfield
        rgba = im.convert("RGBA")
        bg = Image.new("RGB", (W, H), (5, 8, 26))
        d = ImageDraw.Draw(bg)
        import random
        r = random.Random(5)
        for _ in range(220):
            d.ellipse((lambda x, y, s: (x, y, x + s, y + s))(r.randint(0, W), r.randint(0, 760), r.choice([2, 3, 4])), fill=(255, 255, 255))
        rgb = Image.new("RGBA", rgba.size, (0, 0, 0, 0))
        px = rgba.load(); o = rgb.load()
        for yy in range(rgba.height):
            for xx in range(rgba.width):
                R, G, B, A = px[xx, yy]
                o[xx, yy] = (R, G, B, 0 if (A < 20 or (R > 238 and G > 238 and B > 238)) else A)
        s = 1000 / rgb.width
        rgb = rgb.resize((1000, round(rgb.height * s)), Image.LANCZOS)
        bg.paste(rgb, ((W - 1000) // 2, 525 - rgb.height // 2), rgb)
        out = bg
    elif im.width >= 900 and im.width / im.height > 1.2:   # big landscape: full-bleed
        out = cover(im)
    else:
        out = framed(im)
    for k in keys:
        out.convert("RGB").save(f"{OUT}/{k}.jpg", quality=92)
        print("saved", k, im.size)
