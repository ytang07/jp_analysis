import json
import asyncio
import os

from word_cloud import word_cloud
from async_pool import pool

# send parts of it through to orchestrate text analysis at a time

def call_pool(text: str, term: str):
    asyncio.new_event_loop().run_until_complete(pool(text, term))
    
def remove_brackets(text: str):
    while "[" in text:
        index1 = text.find("[")
        index2 = text.find("]")
        text = text[:index1] + text[index2+1:]
    return text

for video_transcript in os.listdir("./jp"):
    with open(f"./jp/{video_transcript}", "r") as f:
        entries = json.load(f)
    text = ""
    texts = []
    for entry in entries:
        text += entry["text"] + " "
        if len(text) > 6000:
            texts.append(text)
            text = ""
    # for index, text in enumerate(texts):
    #     call_pool(text, f"{video_transcript[:-5]}_{index}")
    #     print(f"{video_transcript} {index} done")
        
    full_text = " ".join(texts)
    word_cloud(full_text, f"{video_transcript[:-5]}_cleaned")