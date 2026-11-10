import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = os.path.abspath("assets/textures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 2. MEJA BILIAR (3 WARNA: HIJAU, BIRU, MERAH) - Ukuran 960 x 540 px
# -------------------------------------------------------------------------
TABLE_FELT_COLORS = {
    "green": {
        "base": (20, 105, 50),
        "dark": (14, 75, 35),
        "cushion": (12, 65, 30),
        "cushion_highlight": (30, 135, 65),
    },
    "blue": {
        "base": (25, 75, 140),
        "dark": (18, 55, 105),
        "cushion": (15, 45, 90),
        "cushion_highlight": (38, 105, 185),
    },
    "red": {
        "base": (125, 25, 38),
        "dark": (90, 18, 28),
        "cushion": (75, 15, 24),
        "cushion_highlight": (160, 38, 52),
    }
}

def create_table(color_name):
    # Render at 2x (1920 x 1080) for ultra smooth anti-aliased curves and downscale to 960 x 540
    W, H = 1920, 1080
    pad = 120  # Rail width (60px in 1x)
    
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Outer wooden frame (Mahogany wood look)
    # Background wood gradient
    for y in range(H):
        factor = 0.85 + 0.3 * math.sin(y / 60.0)
        # Deep warm mahogany
        r = int(min(255, 75 * factor + 10))
        g = int(min(255, 38 * factor + 5))
        b = int(min(255, 20 * factor + 3))
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
    
    # Frame bevel border
    frame_corner = 60
    draw.rounded_rectangle([10, 10, W - 10, H - 10], radius=frame_corner, outline=(120, 70, 40, 255), width=8)
    draw.rounded_rectangle([20, 20, W - 20, H - 20], radius=frame_corner - 10, outline=(40, 20, 10, 255), width=6)
    
    # Gold corner plates at 4 corners
    corner_size = 140
    gold_fill = (212, 175, 55, 255)
    gold_dark = (140, 105, 25, 255)
    
    # 2. Diamonds / Sights along the rails (Small mother-of-pearl dots)
    play_x0, play_y0 = pad, pad
    play_x1, play_y1 = W - pad, H - pad
    play_w = play_x1 - play_x0  # 1680 (840 * 2)
    play_h = play_y1 - play_y0  # 840 (420 * 2)
    
    dot_radius = 8
    dot_color = (235, 235, 220, 255)
    dot_border = (60, 40, 20, 255)
    
    def draw_dot(x, y):
        draw.ellipse([x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius], fill=dot_color, outline=dot_border, width=2)
    
    # Short rails (left and right): 3 sights each (at 1/4, 2/4, 3/4 of height)
    rail_mid_x_left = pad // 2
    rail_mid_x_right = W - pad // 2
    for i in range(1, 4):
        y_pos = play_y0 + (play_h * i) // 4
        draw_dot(rail_mid_x_left, y_pos)
        draw_dot(rail_mid_x_right, y_pos)
        
    # Long rails (top and bottom): 3 sights left half, 3 sights right half
    rail_mid_y_top = pad // 2
    rail_mid_y_bottom = H - pad // 2
    for i in range(1, 4):
        # Left half
        x_pos_l = play_x0 + (play_w // 2 * i) // 4
        draw_dot(x_pos_l, rail_mid_y_top)
        draw_dot(x_pos_l, rail_mid_y_bottom)
        # Right half
        x_pos_r = play_x0 + play_w // 2 + (play_w // 2 * i) // 4
        draw_dot(x_pos_r, rail_mid_y_top)
        draw_dot(x_pos_r, rail_mid_y_bottom)

    # 3. Cushions (Rubber bumper shadow and highlights)
    cushion_w = 26
    cush_color = TABLE_FELT_COLORS[color_name]["cushion"]
    cush_hi = TABLE_FELT_COLORS[color_name]["cushion_highlight"]
    
    # Draw cushion background
    draw.rectangle([play_x0 - cushion_w, play_y0 - cushion_w, play_x1 + cushion_w, play_y1 + cushion_w], fill=cush_color)
    draw.rectangle([play_x0, play_y0, play_x1, play_y1], outline=cush_hi, width=3)
    
    # 4. Felt playing surface (Cloth)
    felt_base = TABLE_FELT_COLORS[color_name]["base"]
    felt_dark = TABLE_FELT_COLORS[color_name]["dark"]
    
    # Soft vignette on felt
    felt = Image.new("RGBA", (play_w, play_h), felt_base)
    f_draw = ImageDraw.Draw(felt)
    # Subtle gradient towards center (overhead table lamp light)
    for i in range(play_h // 2):
        factor = (i / (play_h / 2.0)) ** 1.8
        col = (
            int(felt_base[0] * (1.0 + 0.15 * (1 - factor))),
            int(felt_base[1] * (1.0 + 0.15 * (1 - factor))),
            int(felt_base[2] * (1.0 + 0.15 * (1 - factor))),
            255
        )
        f_draw.rectangle([int(factor * 50), i, play_w - int(factor * 50), play_h - i], outline=col)
    
    img.paste(felt, (play_x0, play_y0))
    
    # 5. Table Markings (Lines & Spots)
    mark_draw = ImageDraw.Draw(img)
    line_col = (255, 255, 255, 75)
    spot_col = (255, 255, 255, 120)
    
    # Head string line (at 1/4 of length from left)
    head_x = play_x0 + play_w // 4
    mark_draw.line([(head_x, play_y0 + 10), (head_x, play_y1 - 10)], fill=line_col, width=3)
    
    # Head spot
    head_spot_y = play_y0 + play_h // 2
    mark_draw.ellipse([head_x - 6, head_spot_y - 6, head_x + 6, head_spot_y + 6], fill=spot_col)
    
    # Center spot
    center_x = play_x0 + play_w // 2
    mark_draw.ellipse([center_x - 6, head_spot_y - 6, center_x + 6, head_spot_y + 6], fill=spot_col)
    
    # Foot spot (where triangle rack is placed: at 3/4 of length)
    foot_x = play_x0 + (play_w * 3) // 4
    mark_draw.ellipse([foot_x - 6, head_spot_y - 6, foot_x + 6, head_spot_y + 6], fill=spot_col)

    # 6. Pockets (Lubang 6 buah)
    # Corner pockets radius ~56px (at 2x)
    # Side pockets radius ~50px
    pockets = [
        # (x, y, radius, is_side)
        (play_x0, play_y0, 60, False),                # Top-Left
        (play_x1, play_y0, 60, False),                # Top-Right
        (play_x0, play_y1, 60, False),                # Bottom-Left
        (play_x1, play_y1, 60, False),                # Bottom-Right
        (play_x0 + play_w // 2, play_y0 - 8, 52, True), # Top-Center
        (play_x0 + play_w // 2, play_y1 + 8, 52, True)  # Bottom-Center
    ]
    
    for px, py, pr, is_side in pockets:
        # Brass / leather pocket rim
        mark_draw.ellipse([px - pr - 14, py - pr - 14, px + pr + 14, py + pr + 14], fill=(70, 50, 30, 255), outline=gold_dark, width=6)
        # Deep black drop pocket with smooth falloff
        for r_step in range(pr, 0, -4):
            val = int(25 * (r_step / pr))
            mark_draw.ellipse([px - r_step, py - r_step, px + r_step, py + r_step], fill=(val, val, val, 255))
            
    # Resize down to 960 x 540 with high quality Lanczos
    res = img.resize((960, 540), Image.Resampling.LANCZOS)
    return res

print("Generating Billiard Tables...")
for name in TABLE_FELT_COLORS:
    tbl = create_table(name)
    tbl.save(os.path.join(OUTPUT_DIR, f"table_{name}.png"))
print("All 3 tables generated!")

# -------------------------------------------------------------------------
# 3. STIK BILIAR (CUE STICK) - Ukuran 540 x 20 px
# -------------------------------------------------------------------------
def create_cue_stick():
    # Render at 2x: 1080 x 40 px, tip at (0, 20) pointing left
    W, H = 1080, 40
    mid_y = H // 2
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Diameters taper from tip (16px at 2x) to butt (34px at 2x)
    for x in range(W):
        # Interpolate thickness
        t = x / float(W)
        radius = int(8 + 9 * t)
        y0 = mid_y - radius
        y1 = mid_y + radius
        
        # Decide material segment along length
        if x < 14:
            # Blue chalked leather tip
            base_col = (45, 110, 185)
        elif x < 48:
            # White ivory ferrule
            base_col = (245, 245, 240)
        elif x < 680:
            # Maple wood shaft (light creamy wood with subtle grain)
            grain = 5 * math.sin(x / 4.0)
            base_col = (int(232 + grain), int(205 + grain), int(160 + grain))
        elif x < 710:
            # Joint collar (black with brass rings)
            if 690 <= x <= 696 or 704 <= x <= 708:
                base_col = (212, 175, 55)  # Brass ring
            else:
                base_col = (30, 30, 30)     # Black phenolic
        elif x < 860:
            # Forearm (Dark mahogany with inlaid points)
            base_col = (90, 40, 22)
        elif x < 1030:
            # Grip / Wrap (Black textured linen wrap)
            grid = 20 if (x // 6 + (mid_y) // 4) % 2 == 0 else 0
            base_col = (35 + grid, 35 + grid, 35 + grid)
        else:
            # Butt sleeve & rubber bumper
            if x >= 1065:
                base_col = (20, 20, 20)      # Rubber bumper
            else:
                base_col = (75, 30, 15)      # Dark wood butt
        
        # Draw 3D cylinder vertical column with specular reflection
        for y in range(y0, y1 + 1):
            ny = (y - mid_y) / float(radius)
            nz = math.sqrt(max(0.0, 1.0 - ny*ny))
            # Light from top
            diffuse = max(0.1, 0.4 * nz - 0.7 * ny + 0.3)
            spec = max(0.0, nz) ** 10
            
            r = min(255, int(base_col[0] * diffuse + spec * 70))
            g = min(255, int(base_col[1] * diffuse + spec * 70))
            b = min(255, int(base_col[2] * diffuse + spec * 70))
            draw.point((x, y), fill=(r, g, b, 255))
            
    # Resize to 540 x 20
    res = img.resize((540, 20), Image.Resampling.LANCZOS)
    return res

print("Generating Cue Stick...")
cue = create_cue_stick()
cue.save(os.path.join(OUTPUT_DIR, "cue_stick.png"))
print("Cue stick generated!")

# -------------------------------------------------------------------------
# 4. ASET UI: BUTTONS, POWER BAR, POPUP PANEL
# -------------------------------------------------------------------------
def create_button(text, state="normal"):
    # Size 220 x 48 px
    W, H = 220, 48
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    if state == "normal":
        bg_col_top = (45, 52, 60)
        bg_col_bot = (28, 32, 38)
        border_col = (180, 140, 60)
        txt_col = (245, 245, 245)
    elif state == "hover":
        bg_col_top = (65, 78, 92)
        bg_col_bot = (40, 50, 62)
        border_col = (240, 200, 80)
        txt_col = (255, 255, 255)
    else:  # pressed
        bg_col_top = (22, 26, 32)
        bg_col_bot = (35, 42, 50)
        border_col = (140, 110, 45)
        txt_col = (210, 210, 210)
        
    # Draw button gradient
    for y in range(H):
        t = y / float(H)
        r = int(bg_col_top[0] * (1 - t) + bg_col_bot[0] * t)
        g = int(bg_col_top[1] * (1 - t) + bg_col_bot[1] * t)
        b = int(bg_col_top[2] * (1 - t) + bg_col_bot[2] * t)
        draw.line([(6, y), (W - 7, y)], fill=(r, g, b, 255))
        
    # Rounded border
    draw.rounded_rectangle([2, 2, W - 3, H - 3], radius=10, outline=border_col, width=2)
    
    # Highlight on top edge
    draw.line([(10, 3), (W - 10, 3)], fill=(255, 255, 255, 60), width=1)
    
    return img

print("Generating UI Buttons...")
create_button("DEFAULT", "normal").save(os.path.join(OUTPUT_DIR, "button_normal.png"))
create_button("DEFAULT", "hover").save(os.path.join(OUTPUT_DIR, "button_hover.png"))
create_button("DEFAULT", "pressed").save(os.path.join(OUTPUT_DIR, "button_pressed.png"))

def create_power_bar():
    # Power bar frame (240 x 24)
    W, H = 240, 24
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f_draw = ImageDraw.Draw(frame)
    f_draw.rounded_rectangle([0, 0, W - 1, H - 1], radius=8, fill=(20, 20, 25, 230), outline=(200, 160, 60), width=2)
    frame.save(os.path.join(OUTPUT_DIR, "power_bar_frame.png"))
    
    # Power bar fill (Gradient Green -> Yellow -> Red)
    inner_w, inner_h = W - 6, H - 6
    fill_img = Image.new("RGBA", (inner_w, inner_h), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(fill_img)
    for x in range(inner_w):
        t = x / float(inner_w)
        if t < 0.5:
            # Green to Yellow
            sub_t = t / 0.5
            r = int(40 + 200 * sub_t)
            g = 210
            b = 40
        else:
            # Yellow to Red
            sub_t = (t - 0.5) / 0.5
            r = 240
            g = int(210 * (1 - sub_t))
            b = 30
        p_draw.line([(x, 0), (x, inner_h)], fill=(r, g, b, 255))
        
    # Highlight on top
    p_draw.line([(0, 1), (inner_w, 1)], fill=(255, 255, 255, 120), width=1)
    fill_img.save(os.path.join(OUTPUT_DIR, "power_bar_fill.png"))

print("Generating Power Bar...")
create_power_bar()

def create_panel_box():
    # Modal dialog / popup panel (540 x 400)
    W, H = 540, 400
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(panel)
    
    # Outer glow / shadow
    p_draw.rounded_rectangle([8, 8, W - 9, H - 9], radius=16, fill=(18, 22, 28, 240), outline=(212, 175, 55, 255), width=3)
    p_draw.rounded_rectangle([14, 14, W - 15, H - 15], radius=12, outline=(60, 70, 85, 180), width=1)
    
    # Header bar
    for y in range(16, 56):
        t = (y - 16) / 40.0
        r = int(40 * (1 - t) + 25 * t)
        g = int(48 * (1 - t) + 30 * t)
        b = int(60 * (1 - t) + 38 * t)
        p_draw.line([(16, y), (W - 17, y)], fill=(r, g, b, 255))
    p_draw.line([(16, 56), (W - 17, 56)], fill=(212, 175, 55, 180), width=2)
    
    panel.save(os.path.join(OUTPUT_DIR, "panel_box.png"))

print("Generating Panel Box...")
create_panel_box()
print("All Assets Created Successfully!")
