import asyncio
import aiohttp
import json

from text_config import apikey

# configure request constants
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
text_url = "https://app.thetextapi.com/text/"
summarize_url = text_url+"summarize"
ner_url = text_url+"ner"
mcp_url = text_url+"most_common_phrases"
polarity_url = text_url+"text_polarity"

"""fix yelling at me error"""
from functools import wraps
 
from asyncio.proactor_events import _ProactorBasePipeTransport
 
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper
 
_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
"""fix yelling at me error end"""

# configure request bodies
# return a dict of url: body
def configure_bodies(text: str):
    _dict = {}
    _dict[summarize_url] = {
        "text": text,
        "proportion": 0.1
    }
    _dict[ner_url] = {
        "text": text,
        "labels": "ARTICLE"
    }
    _dict[mcp_url] = {
        "text": text,
        "num_phrases": 5
    }
    _dict[polarity_url] = {
        "text": text
    }
    return _dict

# configure async requests
# configure gathering of requests
async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)
    async def sem_task(task):
        async with semaphore:
            return await task
    
    return await asyncio.gather(*(sem_task(task) for task in tasks))

# create async post function
async def post_async(url, session, headers, body):
    async with session.post(url, headers=headers, json=body) as response:
        text = await response.text()
        return json.loads(text)
    
async def pool(text: str, term: str):
    conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    session = aiohttp.ClientSession(connector=conn)
    urls_bodies = configure_bodies(text)
    conc_req = 4
    summary, ner, mcp, polarity = await gather_with_concurrency(conc_req, *[post_async(url, session, headers, body) for url, body in urls_bodies.items()])
    await session.close()
    
    # write docs
    with open(f"summaries/{term}.txt", "w") as f:
        f.write(summary["summary"])
    
    ners = ner["ner"]
    list_ners = []
    for ner in ners:
        list_ners.append(" ".join(ner))
    
    with open(f"ners/{term}.txt", "w") as f:
        for ner in list_ners:
            f.write(ner + '\n')
        
    mcps = mcp["most common phrases"]
    with open(f"mcps/{term}.txt", "w") as f:
        for mcp in mcps:
            f.write(mcp + '\n')
    
    with open(f"polarities/{term}.txt", "w") as f:
        f.write(str(polarity["text polarity"]))
         