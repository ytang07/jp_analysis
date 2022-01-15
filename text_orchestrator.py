# input: text body
import asyncio

from .async_pool import pool
from .ner_processing import most_common

def orchestrate_text_analysis(text:str, term:str):
    """Step 1"""
    # task to execute all requests
    # summary, ner, mcp, polarity = asyncio.get_event_loop().run_until_complete(pool(text))
    
    """Step 2"""
    # do NER analysis
    # most_common_ners = most_common(ner)
    # summary = summary.replace("\n", "")
    # return summary, most_common_ners, mcp, polarity

# testtext = "Yujian Tang tests Twitter text analysis orchestrator. We should get a summary, the most common ners, the most common phrases, and a polarity rating. This is part 1 of a test. There are multiple parts to this test. Yujian Tang is awesome. The Text API is the most comprehensive Text Analysis API available."
# print(orchestrate_text_analysis(testtext))