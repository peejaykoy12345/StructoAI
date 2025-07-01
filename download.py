# Downloading images for training

import os
from icrawler.builtin import GoogleImageCrawler

def crawl_and_rename(keywords, output_dir, prefix, max_images=50):
    os.makedirs(output_dir, exist_ok=True)

    for kw in keywords:
        crawler = GoogleImageCrawler(storage={'root_dir': output_dir})
        crawler.crawl(keyword=kw, max_num=max_images)

    files = sorted([f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))])

    for i, filename in enumerate(files):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i+1:03d}{ext}"
        os.rename(os.path.join(output_dir, filename), os.path.join(output_dir, new_name))

crawl_and_rename(["ID", "Student ID", "Government ID", "ID example"], "DataSet/ID", "ID_CARD_TRAIN", 30)