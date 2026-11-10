import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = os.path.abspath("assets/textures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 1. BOLA BILIAR (16 BOLA) - 48x48 pixel (Rendered at 192x192 with 4x supersampling)
# -------------------------------------------------------------------------
BALL_COLORS = {
    0: (248, 246, 240),  # Cue Ball (Ivory)
    1: (235, 175, 20),   # Yellow
    2: (30, 80, 195),    # Blue
    3: (210, 35, 35),    # Red
    4: (100, 35, 140),   # Purple
    5: (230, 95, 20),    # Orange
    6: (25, 130, 55),    # Green
    7: (120, 25, 40),    # Maroon
    8: (25, 25, 28),     # 8-ball Black
    9: (235, 175, 20),   # Yellow stripe
    10: (30, 80, 195),   # Blue stripe
    11: (210, 35, 35),   # Red stripe
    12: (100, 35, 140),  # Purple stripe
    13: (230, 95, 20),   # Orange stripe
    14: (25, 130, 55),   # Green stripe
    15: (120, 25, 40),   # Maroon stripe
}

def create_ball(number):
    size = 192  # 4x supersampling of 48px
    radius = size // 2 - 4
    cx, cy = size // 2, size // 2
    
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    is_stripe = number >= 9
    color = BALL_COLORS[number]
    ivory = (248, 246, 240)
    
    # Base circle mask
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=255)
    
    # Ball base surface
    surface = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(surface)
    
    if not is_stripe:
        s_draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=color)
    else:
        # Striped ball: White body with horizontal colored band
        s_draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=ivory)
        band_h = int(radius * 1.15)
        # Draw wide colored strip in the center
        stripe_rect = [0, cy - band_h // 2, size, cy + band_h // 2]
        s_draw.rectangle(stripe_rect, fill=color)
    
    # Number circle and text (if not cue ball)
    if number > 0:
        c_radius = int(radius * 0.44)
        s_draw.ellipse([cx - c_radius, cy - c_radius, cx + c_radius, cy + c_radius], fill=(250, 250, 250))
        # Draw number
        font_size = int(c_radius * 1.18)
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        num_str = str(number)
        bbox = font.getbbox(num_str)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        text_x = cx - (bbox[0] + bbox[2]) / 2
        text_y = cy - (bbox[1] + bbox[3]) / 2
        s_draw.text((text_x, text_y), num_str, fill=(20, 20, 20), font=font)
        
        # Underline for 6 and 9 to distinguish
        if number in (6, 9):
            line_y = text_y + text_h + 3
            s_draw.line([cx - 8, line_y, cx + 8, line_y], fill=(20, 20, 20), width=3)
    
    # Apply spherical lighting & 3D shadow map
    # We iterate over pixels or compute lighting map
    light_map = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    light_pixels = light_map.load()
    
    lx, ly = cx - radius * 0.35, cy - radius * 0.35  # light source position
    
    for y in range(size):
        for x in range(size):
            dx = x - cx
            dy = y - cy
            dist_sq = dx*dx + dy*dy
            if dist_sq <= radius * radius:
                dist = math.sqrt(dist_sq)
                # Normalized normal vector on sphere
                nx = dx / radius
                ny = dy / radius
                nz = math.sqrt(max(0.0, 1.0 - (nx*nx + ny*ny)))
                
                # Light direction (towards top-left)
                ldx = (lx - x) / radius
                ldy = (ly - y) / radius
                ldz = 0.8
                l_len = math.sqrt(ldx*ldx + ldy*ldy + ldz*ldz)
                ldx /= l_len
                ldy /= l_len
                ldz /= l_len
                
                # Diffuse shading
                diffuse = max(0.0, nx*ldx + ny*ldy + nz*ldz)
                
                # Specular highlight
                # Reflection vector
                rx = 2 * diffuse * nx - ldx
                ry = 2 * diffuse * ny - ldy
                rz = 2 * diffuse * nz - ldz
                spec = max(0.0, rz) ** 16
                
                # Edge rim shadow / ambient occlusion
                rim = 1.0 - (dist / radius) ** 2.5
                
                # Compute shadow darkening or highlight brightening
                if diffuse < 0.6:
                    shadow_factor = int((0.6 - diffuse) * 180)
                    light_pixels[x, y] = (0, 0, 0, min(230, shadow_factor))
                elif spec > 0.15:
                    highlight_factor = int(spec * 220)
                    light_pixels[x, y] = (255, 255, 255, min(240, highlight_factor))
    
    # Composite surface, lighting, and mask
    final = Image.composite(surface, img, mask)
    final = Image.alpha_composite(final, light_map)
    
    # Soft drop shadow underneath the ball
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_r = radius * 0.95
    sh_draw.ellipse([cx - sh_r, cy - sh_r + 4, cx + sh_r, cy + sh_r + 4], fill=(0, 0, 0, 90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(4))
    
    result = Image.alpha_composite(shadow, final)
    
    # Downscale from 192x192 to 48x48 using high quality Lanczos
    result = result.resize((48, 48), Image.Resampling.LANCZOS)
    return result

print("Generating 16 Billiard Balls...")
for i in range(16):
    ball_img = create_ball(i)
    ball_img.save(os.path.join(OUTPUT_DIR, f"ball_{i}.png"))
print("All 16 balls generated successfully!")
