import whisper
import sys


def transcribe(model, path) -> str:
    opt = whisper.DecodingOptions()
    audio = whisper.pad_or_trim(whisper.load_audio(path))

    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model. device)

    return whisper.decode(model, mel, opt).text


def enrich(raw_text: str) -> str:
    return raw_text


def main():
    model = whisper.load_model("turbo")
    if len(sys.argv) != 2:
        print("Usage: python transcribe /path/to/audio.mp3")
        exit(1)
    audio_path = sys.argv[1]
    print(transcribe(model, audio_path))


if __name__ == "__main__":
    main()
