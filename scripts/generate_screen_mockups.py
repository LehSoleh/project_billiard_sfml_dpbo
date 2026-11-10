import os
import math
from PIL import Image, ImageDraw, ImageFont

TEXTURES_DIR = os.path.abspath("assets/textures")
SCREENS_DIR = os.path.abspath("assets/screens")
os.makedirs(SCREENS_DIR, exist_ok=True)

W, H = 1024, 640

# Fonts
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 38)
    font_h1 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24)
    font_h2 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 18)
    font_btn = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 16)
    font_regular = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
    font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 13)
    font_bold_sm = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 13)
except Exception:
    font_title = font_h1 = font_h2 = font_btn = font_regular = font_small = font_bold_sm = ImageFont.load_default()

def create_base_canvas(title_text="", subtitle_text=""):
    """Membuat latar belakang dasar layar tunggal (tanpa meja/gameplay)"""
    img = Image.new("RGBA", (W, H), (18, 22, 28, 255))
    draw = ImageDraw.Draw(img)

    # Header bar atas jika ada title
    if title_text:
        draw.rectangle([0, 0, W, 70], fill=(26, 32, 42, 255))
        draw.line([(0, 70), (W, 70)], fill=(212, 175, 55, 255), width=2)
        
        # Title
        bbox = font_h1.getbbox(title_text)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) / 2, 16), title_text, fill=(255, 215, 0, 255), font=font_h1)

        if subtitle_text:
            s_bbox = font_small.getbbox(subtitle_text)
            draw.text(((W - (s_bbox[2] - s_bbox[0])) / 2, 46), subtitle_text, fill=(180, 190, 205, 255), font=font_small)

    # Border luar layar
    draw.rectangle([0, 0, W - 1, H - 1], outline=(50, 60, 75, 255), width=1)
    return img

def draw_button(draw, x, y, w, h, text, is_active=False, is_gold=False):
    if is_gold:
        bg_col = (190, 145, 35, 255) if not is_active else (225, 180, 50, 255)
        border_col = (255, 230, 130, 255)
        txt_col = (20, 20, 20, 255)
    else:
        bg_col = (38, 46, 56, 255) if not is_active else (28, 75, 130, 255)
        border_col = (212, 175, 55, 255) if not is_active else (100, 180, 255, 255)
        txt_col = (245, 245, 245, 255)

    draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=bg_col, outline=border_col, width=2)
    bbox = font_btn.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = x + (w - tw) / 2
    ty = y + (h - th) / 2 - 2
    draw.text((tx, ty), text, fill=txt_col, font=font_btn)

# -------------------------------------------------------------------------
# 1. SCREEN MOCKUP: MENU UTAMA (screen_main_menu.png)
# -------------------------------------------------------------------------
def make_main_menu():
    img = create_base_canvas()
    draw = ImageDraw.Draw(img)

    # Frame tengah
    cw, ch = 520, 480
    cx, cy = (W - cw) // 2, (H - ch) // 2
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=16, fill=(24, 30, 40, 255), outline=(212, 175, 55, 255), width=2)

    # Title
    title = "8-BALL BILLIARD"
    bbox = font_title.getbbox(title)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, cy + 40), title, fill=(255, 215, 0, 255), font=font_title)

    sub = "Proyek Desain dan Pemrograman Berorientasi Objek"
    s_bbox = font_regular.getbbox(sub)
    draw.text(((W - (s_bbox[2] - s_bbox[0])) / 2, cy + 95), sub, fill=(185, 195, 210, 255), font=font_regular)

    draw.line([(cx + 40, cy + 130), (cx + cw - 40, cy + 130)], fill=(60, 72, 90, 255), width=1)

    # Buttons
    btn_w, btn_h = 240, 48
    bx = (W - btn_w) // 2
    buttons = ["MULAI MAIN", "PAPAN SKOR", "PENGATURAN", "KELUAR"]
    start_y = cy + 160
    for i, b in enumerate(buttons):
        draw_button(draw, bx, start_y + i * 65, btn_w, btn_h, b, is_gold=(i == 0))

    return img

# -------------------------------------------------------------------------
# 2. SCREEN MOCKUP: INPUT NAMA & TINGKAT KESULITAN (screen_player_setup.png)
# -------------------------------------------------------------------------
def make_player_setup():
    img = create_base_canvas("PERSIAPAN PERTANDINGAN (UC-01 & UC-02)", "Konfigurasi data pemain dan tingkat kemampuan lawan komputer")
    draw = ImageDraw.Draw(img)

    pw, ph = 640, 460
    px, py = (W - pw) // 2, 110
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=14, fill=(25, 32, 42, 255), outline=(65, 78, 95, 255), width=2)

    # Field 1: Nama Pemain
    draw.text((px + 50, py + 35), "Nama Pemain:", fill=(240, 240, 240), font=font_h2)
    draw.rounded_rectangle([px + 50, py + 68, px + pw - 50, py + 115], radius=6, fill=(16, 20, 26), outline=(100, 120, 145), width=2)
    draw.text((px + 65, py + 80), "Pemain 1|", fill=(255, 255, 255), font=font_regular)
    draw.text((px + pw - 150, py + 82), "(Ketik Nama Anda)", fill=(120, 135, 150), font=font_small)

    # Field 2: Tingkat Kesulitan AI
    draw.text((px + 50, py + 145), "Pilih Tingkat Kesulitan Lawan Komputer (AI):", fill=(240, 240, 240), font=font_h2)

    diffs = [
        ("Mudah", "Toleransi galat besar,\nbidika acak ringan."),
        ("Sedang", "Toleransi galat sedang,\nkemampuan seimbang."),
        ("Sulit", "Toleransi galat kecil,\nsangat akurat.")
    ]
    card_w = 160
    card_h = 100
    card_gap = 25
    cx = px + (pw - (3 * card_w + 2 * card_gap)) // 2
    cy = py + 180

    for i, (name, desc) in enumerate(diffs):
        x = cx + i * (card_w + card_gap)
        is_sel = (i == 1)
        bg = (28, 70, 120, 255) if is_sel else (20, 25, 34, 255)
        bd = (255, 215, 0, 255) if is_sel else (70, 85, 105, 255)
        draw.rounded_rectangle([x, cy, x + card_w, cy + card_h], radius=8, fill=bg, outline=bd, width=2)
        # Text
        bx_t = font_btn.getbbox(name + (" *" if is_sel else ""))
        draw.text((x + (card_w - (bx_t[2] - bx_t[0])) / 2, cy + 14), name + (" *" if is_sel else ""), fill=(255, 255, 255), font=font_btn)
        
        # Multiline desc
        lines = desc.split("\n")
        for l_idx, line in enumerate(lines):
            bx_d = font_small.getbbox(line)
            draw.text((x + (card_w - (bx_d[2] - bx_d[0])) / 2, cy + 46 + l_idx * 18), line, fill=(195, 205, 220), font=font_small)

    # Bottom action buttons
    draw_button(draw, px + 50, py + 380, 240, 48, "MULAI MAIN", is_gold=True)
    draw_button(draw, px + pw - 290, py + 380, 240, 48, "KEMBALI")

    return img

# -------------------------------------------------------------------------
# 3. SCREEN MOCKUP: LAYAR PERTANDINGAN (screen_gameplay.png)
# -------------------------------------------------------------------------
def make_gameplay():
    img = Image.new("RGBA", (W, H), (15, 18, 24, 255))
    table_green_path = os.path.join(TEXTURES_DIR, "table_green.png")
    if os.path.exists(table_green_path):
        base_table = Image.open(table_green_path).convert("RGBA")
        img.paste(base_table, (32, 50), base_table)

    draw = ImageDraw.Draw(img)

    # TOP HUD BAR
    draw.rectangle([0, 0, W, 48], fill=(18, 22, 28, 240))
    draw.line([(0, 48), (W, 48)], fill=(60, 70, 80), width=1)

    # Player 1 Info
    draw.text((32, 14), "Pemain: Kamu", fill=(255, 255, 255), font=font_h2)
    draw.rounded_rectangle([170, 13, 275, 37], radius=6, fill=(25, 90, 45), outline=(50, 180, 80))
    draw.text((180, 16), "SOLID (1-7)", fill=(240, 255, 240), font=font_bold_sm)

    # Turn Badge (Center)
    draw.rounded_rectangle([430, 8, 594, 40], radius=8, fill=(180, 140, 20), outline=(255, 220, 80), width=2)
    draw.text((455, 14), "GILIRAN ANDA", fill=(20, 20, 20), font=font_h2)

    # Computer Info
    draw.text((640, 14), "Komputer (Sedang)", fill=(255, 255, 255), font=font_h2)
    draw.rounded_rectangle([820, 13, 935, 37], radius=6, fill=(90, 30, 35), outline=(180, 60, 70))
    draw.text((830, 16), "STRIPES (9-15)", fill=(255, 240, 240), font=font_bold_sm)

    # Pause Button top right
    draw_button(draw, 945, 10, 65, 30, "Esc")

    # Cue ball at (302, 320)
    cue_ball_path = os.path.join(TEXTURES_DIR, "ball_0.png")
    if os.path.exists(cue_ball_path):
        cue_ball = Image.open(cue_ball_path).resize((24, 24), Image.Resampling.LANCZOS)
        img.paste(cue_ball, (302 - 12, 320 - 12), cue_ball)

    # Rack 15 balls at foot spot
    apex_x, apex_y = 680, 320
    dx, r = 21, 12
    rack_nums = [1, 2, 9, 3, 8, 10, 4, 11, 7, 14, 5, 12, 13, 6, 15]
    idx = 0
    for row in range(5):
        rx = apex_x + row * dx
        sy = apex_y - row * r
        for col in range(row + 1):
            by = sy + col * (2 * r + 1)
            num = rack_nums[idx]
            idx += 1
            b_path = os.path.join(TEXTURES_DIR, f"ball_{num}.png")
            if os.path.exists(b_path):
                b_img = Image.open(b_path).resize((24, 24), Image.Resampling.LANCZOS)
                img.paste(b_img, (rx - 12, int(by - 12)), b_img)

    # Aiming Line
    for i in range(1, 16):
        dot_x = 302 + i * 20
        dot_y = 320
        draw.ellipse([dot_x - 3, dot_y - 3, dot_x + 3, dot_y + 3], fill=(255, 255, 255, 180))

    # Cue stick
    cue_img_path = os.path.join(TEXTURES_DIR, "cue_stick.png")
    if os.path.exists(cue_img_path):
        cue_stick = Image.open(cue_img_path)
        cue_stick_flipped = cue_stick.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        img.paste(cue_stick_flipped, (302 - 540 - 25, 320 - 10), cue_stick_flipped)

    # BOTTOM HUD
    draw.rectangle([0, H - 46, W, H], fill=(18, 22, 28, 240))
    draw.line([(0, H - 46), (W, H - 46)], fill=(60, 70, 80), width=1)
    draw.text((32, H - 32), "Petunjuk: Gerakkan mouse untuk membidik. Tahan Klik Kiri untuk mengisi kekuatan pukulan.", fill=(200, 210, 220), font=font_regular)
    draw.text((640, H - 32), "KEKUATAN PUKULAN:", fill=(240, 240, 240), font=font_bold_sm)
    draw.rounded_rectangle([790, H - 36, 1000, H - 12], radius=6, fill=(10, 12, 16), outline=(212, 175, 55), width=2)
    draw.rounded_rectangle([793, H - 33, 793 + int(204 * 0.65), H - 15], radius=4, fill=(230, 160, 30))

    return img

# -------------------------------------------------------------------------
# 4. SCREEN MOCKUP: MENU JEDA (screen_pause_menu.png) - STANDALONE
# -------------------------------------------------------------------------
def make_pause_menu():
    img = create_base_canvas("MENU JEDA (UC-05)", "Permainan dihentikan sementara")
    draw = ImageDraw.Draw(img)

    cw, ch = 480, 380
    cx, cy = (W - cw) // 2, 140
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=16, fill=(25, 32, 42, 255), outline=(212, 175, 55, 255), width=2)

    # Header internal
    draw.text((cx + 140, cy + 40), "PERMAINAN DIJEDA", fill=(255, 215, 0), font=font_h1)
    draw.line([(cx + 40, cy + 85), (cx + cw - 40, cy + 85)], fill=(60, 72, 90), width=1)

    btn_w, btn_h = 260, 50
    bx = cx + (cw - btn_w) // 2
    draw_button(draw, bx, cy + 120, btn_w, btn_h, "LANJUTKAN PERMAINAN", is_gold=True)
    draw_button(draw, bx, cy + 190, btn_w, btn_h, "PENGATURAN")
    draw_button(draw, bx, cy + 260, btn_w, btn_h, "MENU UTAMA")

    return img

# -------------------------------------------------------------------------
# 5. SCREEN MOCKUP: PENGATURAN (screen_settings.png) - STANDALONE
# -------------------------------------------------------------------------
def make_settings():
    img = create_base_canvas("PENGATURAN GAME (UC-08)", "Penyesuaian warna kain meja dan volume audio")
    draw = ImageDraw.Draw(img)

    pw, ph = 640, 480
    px, py = (W - pw) // 2, 100
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=14, fill=(25, 32, 42, 255), outline=(65, 78, 95, 255), width=2)

    # 1. Warna Kain Meja
    draw.text((px + 50, py + 35), "Pilih Warna Kain Meja Biliar:", fill=(240, 240, 240), font=font_h2)
    colors = [
        ("Hijau Klasik", (25, 110, 50), True),
        ("Biru Elektrik", (30, 80, 160), False),
        ("Merah Marun", (140, 25, 40), False)
    ]
    cb_w = 160
    for i, (cname, ccode, sel) in enumerate(colors):
        cx = px + 50 + i * (cb_w + 30)
        cy = py + 75
        draw.rounded_rectangle([cx, cy, cx + cb_w, cy + 50], radius=8, fill=ccode, outline=(255, 215, 0) if sel else (100, 100, 100), width=3 if sel else 1)
        bx_t = font_btn.getbbox(cname + (" *" if sel else ""))
        draw.text((cx + (cb_w - (bx_t[2] - bx_t[0])) / 2, cy + 16), cname + (" *" if sel else ""), fill=(255, 255, 255), font=font_btn)

    draw.line([(px + 50, py + 155), (px + pw - 50, py + 155)], fill=(50, 60, 75), width=1)

    # 2. Volume Efek Suara (SFX)
    draw.text((px + 50, py + 175), "Volume Efek Suara (SFX):", fill=(240, 240, 240), font=font_h2)
    draw.rounded_rectangle([px + 50, py + 210, px + pw - 120, py + 224], radius=6, fill=(16, 20, 26), outline=(80, 95, 110))
    draw.rounded_rectangle([px + 50, py + 210, px + 50 + int((pw - 170) * 0.8), py + 224], radius=6, fill=(100, 180, 255))
    draw.ellipse([px + 50 + int((pw - 170) * 0.8) - 10, py + 217 - 10, px + 50 + int((pw - 170) * 0.8) + 10, py + 217 + 10], fill=(255, 255, 255), outline=(50, 100, 180), width=2)
    draw.text((px + pw - 100, py + 208), "80%", fill=(220, 230, 240), font=font_h2)

    # 3. Volume Musik Latar (BGM)
    draw.text((px + 50, py + 265), "Volume Musik Latar (BGM):", fill=(240, 240, 240), font=font_h2)
    draw.rounded_rectangle([px + 50, py + 300, px + pw - 120, py + 314], radius=6, fill=(16, 20, 26), outline=(80, 95, 110))
    draw.rounded_rectangle([px + 50, py + 300, px + 50 + int((pw - 170) * 0.6), py + 314], radius=6, fill=(100, 180, 255))
    draw.ellipse([px + 50 + int((pw - 170) * 0.6) - 10, py + 307 - 10, px + 50 + int((pw - 170) * 0.6) + 10, py + 307 + 10], fill=(255, 255, 255), outline=(50, 100, 180), width=2)
    draw.text((px + pw - 100, py + 298), "60%", fill=(220, 230, 240), font=font_h2)

    draw.line([(px + 50, py + 355), (px + pw - 50, py + 355)], fill=(50, 60, 75), width=1)

    # Save button
    draw_button(draw, px + 50, py + 395, 240, 48, "SIMPAN", is_gold=True)
    draw_button(draw, px + pw - 290, py + 395, 240, 48, "KEMBALI")

    return img

# -------------------------------------------------------------------------
# 6. SCREEN MOCKUP: PAPAN SKOR (screen_highscore.png) - STANDALONE
# -------------------------------------------------------------------------
def make_highscore():
    img = create_base_canvas("PAPAN SKOR TERTINGGI (UC-07)", "Daftar riwayat skor tertinggi yang tersimpan di berkas lokal")
    draw = ImageDraw.Draw(img)

    pw, ph = 740, 480
    px, py = (W - pw) // 2, 100
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=14, fill=(25, 32, 42, 255), outline=(65, 78, 95, 255), width=2)

    # Table Header
    headers = ["Peringkat", "Nama Pemain", "Skor Akhir", "Tingkat", "Tanggal"]
    cols_x = [px + 30, px + 150, px + 330, px + 470, px + 590]
    draw.rectangle([px + 20, py + 25, px + pw - 20, py + 65], fill=(35, 45, 58))
    for i, h_text in enumerate(headers):
        draw.text((cols_x[i], py + 34), h_text, fill=(255, 215, 0), font=font_h2)

    rows = [
        ("Juara 1", "Raka", "1850", "Sedang", "08 Nov 2026"),
        ("Juara 2", "Soleh", "1620", "Sulit", "07 Nov 2026"),
        ("Juara 3", "Budi", "1400", "Sedang", "06 Nov 2026"),
        ("Juara 4", "Andi", "1250", "Mudah", "05 Nov 2026"),
        ("Juara 5", "Dewi", "980", "Mudah", "04 Nov 2026"),
    ]

    for r_idx, row in enumerate(rows):
        ry = py + 75 + r_idx * 52
        bg_col = (20, 26, 34) if r_idx % 2 == 0 else (16, 21, 28)
        draw.rectangle([px + 20, ry, px + pw - 20, ry + 46], fill=bg_col)
        for c_idx, val in enumerate(row):
            txt_color = (255, 215, 0) if c_idx == 0 else (240, 240, 240)
            draw.text((cols_x[c_idx], ry + 13), val, fill=txt_color, font=font_regular)

    # Back button
    draw_button(draw, px + (pw - 240) // 2, py + 395, 240, 48, "KEMBALI KE MENU", is_gold=True)
    return img

print("Generating 6 Clean Standalone Screen Mockup Images...")
make_main_menu().save(os.path.join(SCREENS_DIR, "screen_main_menu.png"))
make_player_setup().save(os.path.join(SCREENS_DIR, "screen_player_setup.png"))
make_gameplay().save(os.path.join(SCREENS_DIR, "screen_gameplay.png"))
make_pause_menu().save(os.path.join(SCREENS_DIR, "screen_pause_menu.png"))
make_settings().save(os.path.join(SCREENS_DIR, "screen_settings.png"))
make_highscore().save(os.path.join(SCREENS_DIR, "screen_highscore.png"))
print("All 6 Clean Standalone Mockups generated successfully!")
