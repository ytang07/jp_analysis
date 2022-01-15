import requests
import json
from text_config import apikey
from get_filenames import get_filenames
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
mcp_url = "https://app.thetextapi.com/text/most_common_phrases"
# get most common phrases
def collect_mcps():
    filenames = get_filenames()
    for filename in filenames:
        with open(f"./mcps/{filename}.txt", "r") as f:
            entries = f.read()
        body = {
            "text": entries,
            "num_phrases": 5
        }
        response = requests.post(mcp_url, headers=headers, json=body)
        _dict = json.loads(response.text)
        mcps = _dict["most common phrases"]
        with open(f"./mcps/{filename}_re.txt", "w") as f:
            for mcp in mcps:
                f.write(mcp + '\n')
            
            
collect_mcps()