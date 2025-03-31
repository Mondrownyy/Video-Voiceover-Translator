import json

with open("../data/transcripts/output_json.json", "r") as file:
    data = json.load(file)

transcript = data["results"]["channels"][0]["alternatives"][0]["transcript"]

print(transcript)
