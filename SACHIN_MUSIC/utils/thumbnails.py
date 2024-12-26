import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch
from SACHIN_MUSIC import app
from config import YOUTUBE_IMG_URL

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def truncate(text):
    words = text.split(" ")
    text1, text2 = "", ""
    for word in words:
        if len(text1) + len(word) < 30:
            text1 += " " + word
        elif len(text2) + len(word) < 30:
            text2 += " " + word
    return [text1.strip(), text2.strip()]

def crop_center_circle(img, output_size, border=0, crop_scale=1.5):
    half_width, half_height = img.size[0] / 2, img.size[1] / 2
    larger_size = int(output_size * crop_scale)
    img = img.crop((
        half_width - larger_size / 2,
        half_height - larger_size / 2,
        half_width + larger_size / 2,
        half_height + larger_size / 2
    ))
    img = img.resize((output_size - 2 * border, output_size - 2 * border))
    final_img = Image.new("RGBA", (output_size, output_size), "white")
    mask_main = Image.new("L", (output_size - 2 * border, output_size - 2 * border), 0)
    draw_main = ImageDraw.Draw(mask_main)
    draw_main.ellipse((0, 0, output_size - 2 * border, output_size - 2 * border), fill=255)
    final_img.paste(img, (border, border), mask_main)
    return final_img

async def get_thumb(videoid):
    cache_path = f"cache/{videoid}_v4.png"
    if os.path.isfile(cache_path):
        return cache_path

    # Simulated data for testing
    title = "Sample Title for Video"
    duration = "5:30"
    views = "1.2M Views"
    channel = "Sample Channel"

    # Resources
    background_image_path = "SACHIN_MUSIC/assets/20241226_150720.png"  # Adjusted to uploaded file
    font_path_regular = "SACHIN_MUSIC/assets/font.ttf"  # Ensure fonts exist
    font_path_bold = "SACHIN_MUSIC/assets/font3.ttf"

    # Background and setup
    background = Image.open(background_image_path).convert("RGBA")
    background = changeImageSize(1280, 720, background)
    draw = ImageDraw.Draw(background)
    title_font = ImageFont.truetype(font_path_bold, 45)
    regular_font = ImageFont.truetype(font_path_regular, 30)

    # Title text
    title_lines = truncate(title)
    draw.text((565, 180), title_lines[0], fill="white", font=title_font)
    draw.text((565, 230), title_lines[1], fill="white", font=title_font)

    # Channel and views
    draw.text((565, 320), f"{channel} | {views}", fill="white", font=regular_font)

    # Progress bar
    draw.line([(565, 380), (1100, 380)], fill="red", width=9)
    draw.line([(1100, 380), (1145, 380)], fill="white", width=8)

    # Circle thumbnail
    thumbnail_circle = crop_center_circle(background, 400)
    background.paste(thumbnail_circle, (120, 160), thumbnail_circle)

    # Duration
    draw.text((565, 400), "00:00", fill="white", font=regular_font)
    draw.text((1080, 400), duration, fill="white", font=regular_font)

    # Save result
    if not os.path.exists("cache"):
        os.makedirs("cache")
    background.save(cache_path)
    return cache_path
