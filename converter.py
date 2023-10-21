import requests
from datetime import datetime

import config

CHUNK_SIZE = 1024

def main():
    with open("lines.txt", "r") as file:
        for line in file:
            voiceline = line.split("\t")[0]
            file_name = line.split("\t")[1].strip()
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{config.VOICE_ID}"

            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": f"{config.API_KEY}"
            }

            data = {
            "text": f"{voiceline}",
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.3,
                "similarity_boost": 0.8,
                "style": 0.5
                }
            }
            response = requests.post(url, json=data, headers=headers)
            now = datetime.now()
            if response.status_code == 200:
                with open(f'./voice_files/{file_name}.mp3', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
                print(f"Filename: {file_name} converted. Time: {now.time()}")
            else:
                print(f"Quota has run out! File \"{file_name}\" not converted!")
    print("All done!")

if __name__ == "__main__":
    main()
