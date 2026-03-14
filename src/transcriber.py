import whisper
from pyannote.audio import Pipeline
import sys
import os
from typing import Dict


def diarization(path: str) -> Dict:
    pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization')

    dz = pipeline(path)

    return dz.speaker_diarization


def transcribe(path: str, word_list: [str], **kwargs) -> Dict:
    model = whisper.load_model("base.en")

    return whisper.transcribe(model, path, verbose=False, *kwargs)


def main():
    if len(sys.argv) != 3:
        print("Usage: python transcribe /path/to/audio.mp3 /path/to/wordlist.txt")
        exit(1)

    audio_path = sys.argv[1]
    with open(sys.argv[2], "r") as wl_file:
        word_list = wl_file.read_lines()

    results = transcribe(audio_path, word_list)
    raw_transcripts = results['text']

    with open("examples/transcript.txt", "w") as tran_f:
        tran_f.write(raw_transcripts)




if __name__ == "__main__":
    main()
