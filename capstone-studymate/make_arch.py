"""Схема архітектури StudyMate для слайда 3. Кожен блок названо так, як він
називається в app.py, щоб схему можна було звірити з кодом рядок у рядок."""
from PIL import Image, ImageDraw, ImageFont

W, H = 2720, 900
ORANGE = (255, 87, 34)
DARK = (47, 79, 79)
GREY = (120, 132, 132)
WHITE = (255, 255, 255)
LINE = (198, 206, 206)

F = "C:/Windows/Fonts/calibri.ttf"
FB = "C:/Windows/Fonts/calibrib.ttf"
f_lay = ImageFont.truetype(FB, 34)
f_body = ImageFont.truetype(F, 27)
f_small = ImageFont.truetype(F, 24)
f_tiny = ImageFont.truetype(FB, 22)
f_node = ImageFont.truetype(FB, 28)

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)


def box(x0, y0, x1, y1, fill=WHITE, outline=LINE, w=3, r=14):
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=fill, outline=outline, width=w)


def arrow(x0, y, x1, color=GREY, w=4, head=16):
    d.line([x0, y, x1 - head, y], fill=color, width=w)
    d.polygon([(x1, y), (x1 - head, y - head // 2), (x1 - head, y + head // 2)], fill=color)


def ctext(x0, x1, y, txt, font, fill=DARK):
    tw = d.textlength(txt, font=font)
    d.text(((x0 + x1) / 2 - tw / 2, y), txt, font=font, fill=fill)


# --- користувач ---
box(6, 378, 241, 523, fill=WHITE, outline=DARK, w=4)
ctext(6, 241, 428, "Учень", f_node)
arrow(251, 450, 326)

# --- інтерфейс ---
box(336, 343, 666, 558, fill=WHITE, outline=DARK, w=4)
ctext(336, 666, 388, "Streamlit UI", f_node)
ctext(336, 666, 433, "5 вкладок,", f_small, GREY)
ctext(336, 666, 465, "по одній на режим", f_small, GREY)
arrow(676, 450, 751)

LX0, LX1 = 761, 1935

# --- шар 1 ---
box(LX0, 20, LX1, 330)
d.rounded_rectangle([LX0, 20, LX0 + 10, 330], radius=5, fill=ORANGE)
d.text((LX0 + 38, 42), "Шар 1. Чат", font=f_lay, fill=DARK)
d.text((LX0 + 38, 88), "нативний tool-calling, google-genai", font=f_small, fill=GREY)
d.text((LX0 + 38, 132), "formula_search", font=f_body, fill=DARK)
d.text((LX0 + 38, 172), "study_planner", font=f_body, fill=DARK)
d.text((LX0 + 38, 212), "unit_converter_physics", font=f_body, fill=DARK)
d.text((LX0 + 355, 174), "детерміновані,", font=f_small, fill=GREY)
d.text((LX0 + 355, 206), "без участі LLM", font=f_small, fill=GREY)
# бар'єр retrieval
box(LX0 + 620, 120, LX1 - 30, 305, fill=(255, 243, 239), outline=ORANGE, w=3)
d.text((LX0 + 650, 138), "ДОВІДНИК ФОРМУЛ", font=f_tiny, fill=ORANGE)
d.text((LX0 + 650, 176), "19 формул, gemini-embedding-001", font=f_small, fill=DARK)
d.text((LX0 + 650, 212), "поріг схожості 0.75:", font=f_small, fill=DARK)
d.text((LX0 + 650, 248), "нижче нього відповідь не генерується", font=f_small, fill=DARK)

# --- шар 2 ---
box(LX0, 355, LX1, 560)
d.rounded_rectangle([LX0, 355, LX0 + 10, 560], radius=5, fill=ORANGE)
d.text((LX0 + 38, 377), "Шар 2. Розбір задачі", font=f_lay, fill=DARK)
d.text((LX0 + 38, 423), "Agno, ReasoningTools", font=f_small, fill=GREY)
d.text((LX0 + 38, 468), "think → analyze, кожен крок видно в інтерфейсі", font=f_body, fill=DARK)
d.text((LX0 + 38, 510), "падіння analyze показується користувачу, а не ховається", font=f_small, fill=ORANGE)

# --- шар 3 ---
box(LX0, 585, LX1, 866)
d.rounded_rectangle([LX0, 585, LX0 + 10, 866], radius=5, fill=ORANGE)
d.text((LX0 + 38, 607), "Шар 3. Команда дослідників", font=f_lay, fill=DARK)
d.text((LX0 + 38, 653), "Agno Team", font=f_small, fill=GREY)
d.text((LX0 + 38, 698), "Researcher", font=f_body, fill=DARK)
d.text((LX0 + 38, 738), "Analyst", font=f_body, fill=DARK)
d.text((LX0 + 38, 792), "верифікації між агентами немає", font=f_small, fill=ORANGE)
box(LX0 + 620, 675, LX1 - 30, 790, fill=(255, 243, 239), outline=ORANGE, w=3)
d.text((LX0 + 650, 693), "ВЕБПОШУК", font=f_tiny, fill=ORANGE)
d.text((LX0 + 650, 731), "Bing через ddgs", font=f_small, fill=DARK)

# --- модель ---
MX0, MX1 = 2115, 2712
box(MX0, 293, MX1, 608, fill=WHITE, outline=DARK, w=4)
ctext(MX0, MX1, 333, "LLM", f_tiny, ORANGE)
ctext(MX0, MX1, 378, "gemini-3.5-", f_node)
ctext(MX0, MX1, 418, "flash-lite", f_node)
ctext(MX0, MX1, 483, "один і той самий", f_small, GREY)
ctext(MX0, MX1, 515, "system prompt", f_small, GREY)
ctext(MX0, MX1, 547, "на всі три шари", f_small, GREY)

for y in (175, 450, 725):
    d.line([LX1 + 12, y, 2055, y], fill=LINE, width=4)
d.line([2055, 175, 2055, 725], fill=LINE, width=4)
arrow(2055, 450, MX0 - 10, GREY)

img.save("arch_studymate.png")
print("saved", img.size)
