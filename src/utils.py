import json

with open("../data/transcripts/output_json.json", "r") as file:
    data = json.load(file)

transcript = data["results"]["channels"][0]["alternatives"][0]["transcript"]

with open("../data/transcripts/transcript.txt", "x") as file:
    file.write(transcript)

print(transcript)
