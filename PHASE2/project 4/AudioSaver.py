import pyaudio
import wave

def record_audio(file_name, duration=15, sample_rate=44100, channels=2, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    try:
        stream = audio.open(
            format=format,
            channels=channels,
            rate=sample_rate,
            input=True,
            frames_per_buffer=1024
        )

        print("Recording...")

        frames = []
        for _ in range(0, int(sample_rate / 1024 * duration)):
            data = stream.read(1024)
            frames.append(data)

        print("Finished recording.")

        stream.stop_stream()
        stream.close()

        audio.terminate()

        with wave.open(file_name, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(format))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
            print(f"Audio saved to {file_name}")

    except KeyboardInterrupt:
        print("Recording stopped.")

if __name__ == "__main__":
    file_name = "recorded_audio.wav"
    record_audio(file_name)