from youtube_transcript_api import YouTubeTranscriptApi
import json

personality_vid_ids = ["kYYJlNbV1OM", "HbAZ6cFxCeY", "wLc_MC7NQek", 
                       "BQ4VSRg4e8w", "3iLiKMUiyTI", "X6pbJTqv2hw",
                       "YFWLwYyrMRE", "68tFnjkIZ1Q", "4qZ3EsrKPsc",
                       "11oBFCNeTAs", "w84uRYq0Uc8", "pCceO_D4AlY",
                       "AqkFg1pvNDw", "ewU7Vb9ToXg", "G1eHJ9DdoEA",
                       "D7Kn5p7TP_Y", "fjtBDa4aSGM", "MBWyBdUYPgk", 
                       "Q7GKmznaqsQ", "J9j-bVDrGdI"]

mom_vid_ids = ["I8Xc2_FtpHI", "EN2lyN7rM4E", "Us979jCjHu8"
               "bV16NEWld8Q", "RudKmwzDpNY", "nsZ8XqHPjI4",
               "F3n5qtj89QE", "Nb5cBkbQpGY", "yXZSeiAl4PI",
               "7XtEZvLo-Sc", "T4fjSrVCDvA", "6V1eMvGGcXQ"]

for index, _id in enumerate(personality_vid_ids):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(_id)
        with open(f'personality_{index}.json', 'w', encoding='utf-8') as json_file:
            json.dump(transcript, json_file)
    except:
        print(f"{index} not valid")
        
for index, _id in enumerate(mom_vid_ids):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(_id)
        with open(f'mom_{index}.json', 'w', encoding='utf-8') as json_file:
            json.dump(transcript, json_file)
    except:
        print(f"{index} not valid")
        
        
