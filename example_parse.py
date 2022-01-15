# example_url = "https://www.youtube.com/watch?v=pN3jRihVpGk&list=PLKiU8vyKB6ti1_rUlpZJFdPaxT04sUIoV&index=1"
# _id = example_url.split("=")[1].split("&")[0]
# print(_id)
from  youtube_transcript_api import YouTubeTranscriptApi

transcripts = YouTubeTranscriptApi.get_transcripts(["pN3jRihVpGk", "F_7xepUPH7E", "d5ib3qjQkwk", "EfY_GG4cqHM"])
for transcript in transcripts[0]:
    print(transcript)