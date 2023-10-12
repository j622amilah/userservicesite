import boto3
import csv

# read the movies CSV and populate the all_notes array with all the of notes
with open("movies.csv", 'r') as fd:
    reader = csv.DictReader(fd, fieldnames=["ResponseId", "Notes"], dialect='excel')
    all_notes = [ row["Notes"] for row in reader ]


from botocore.config import Config
my_config = Config(
    region_name = 'eu-west-3',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)
    
    
client = boto3.client('comprehend', config=my_config)

#####
# Complete the call to batch_detect_sentiment
#####
# LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
response = client.batch_detect_sentiment(TextList=all_notes, LanguageCode='en')

for result in response["ResultList"]:
    index = result["Index"]
    sentiment = result["Sentiment"]

    print(sentiment, all_notes[index])
