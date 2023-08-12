import os
from PIL import Image
import secrets
from flask import current_app

def save_picture_p(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/Proj_img', picture_fn)
    output_size = (1200, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def get_embed_link(youtube_link):
    if "youtube.com" in youtube_link or "youtu.be" in youtube_link:
        video_id = None
        
        if "youtube.com" in youtube_link:
            video_id = youtube_link.split("?v=")[1]
        elif "youtu.be" in youtube_link:
            video_id = youtube_link.split("/")[-1]
        
        if video_id:
            embed_link = f"https://www.youtube.com/embed/{video_id}"
            return embed_link
        else:
            return None
    else:
        return None