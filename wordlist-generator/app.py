import datetime
from google.cloud import translate
import os
import csv
import logging

# create filename with timestamp
logfilename = "logs/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".log"

# initialize logger
logging.basicConfig(filename=logfilename, level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def translate_files(input_path, output_path):
    output_records = []
    for file in os.listdir(input_path):
        if file.endswith(".csv"):
            with open(os.path.join(input_path, file), "r") as f:
                data = csv.reader(f)
                for row in data:
                    pa_row = translate_text(row[0])
                    print(f"English: {row[0]} | Punjabi: {pa_row}")
                    output_records.append([row[0], pa_row])

        print(output_records)
        with open(os.path.join(output_path, file), "a") as f:
            writer = csv.writer(f)
            writer.writerows(output_records)


def translate_text(text="Hello, world!", project_id="gurmukhidb"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "pa",
        }
    )

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))
        return translation.translated_text


translate_text()

if __name__ == "__main__":
    print("Starting translation")
    print(os.getcwd())
    input_path = os.path.join(os.getcwd(), "data/en-US/")
    output_path = os.path.join(os.getcwd(), "data/pa/")
    logger.info("Input path: {}".format(input_path))
    logger.info("Output path: {}".format(output_path))

    translate_files(input_path, output_path)
