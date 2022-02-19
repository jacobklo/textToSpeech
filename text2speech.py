import os
import sys
import json
from pathlib import Path
from google.cloud import texttospeech_v1 as texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'voice-341704-b002feed1205.json'


sentenceFile = Path(sys.argv[1])

# Instantiates a client
client = texttospeech.TextToSpeechClient()


# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB"
    , ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
    , speaking_rate=0.8
)

lines = []
outputNames = []
with open(sentenceFile) as f:
  jsonData = json.load(f)

  lines = jsonData
    
  for line in lines:
    line = line.rstrip('\n').replace('.','').replace(',','').replace(':','').replace('?','').replace('-','').replace('\'','').replace('\"','')
    lineWordList = [x[0].upper() + x[1:] for x in line.split()]
    outputNames.append(''.join(lineWordList[0:6]))


os.makedirs(sentenceFile.with_suffix('').name, exist_ok=True)

for i in range(len(lines)):
  sentence = lines[i]
  # Set the text input to be synthesized
  synthesis_input = texttospeech.SynthesisInput(text=sentence)

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(
      input=synthesis_input
      , voice=voice
      , audio_config=audio_config
  )

  # The response's audio_content is binary.
  filename = sentenceFile.with_suffix('').name + '/' + outputNames[i] + ".mp3"
  with open(filename, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file ' + filename)
    

