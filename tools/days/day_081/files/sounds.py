import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write
import os

sd.default.samplerate = 44100


def generate_beep(filename, duration, frequency=2000):
    """
    Generate a beep sound and save it as a .wav file.

    :param filename: The name of the file to save the beep.
    :param duration: The duration of the beep in seconds.
    :param frequency: The frequency of the beep in Hz (default is 1000 Hz).
    """
    samplerate = 44100
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    wave = 0.1 * np.sin(2 * np.pi * frequency * t)
    # stereo_wave = np.column_stack([wave, wave])
    # write(filename, samplerate, stereo_wave.astype(np.float32))
    fade_in_duration = int(0.025 * samplerate)  # 50 ms fade-in
    fade_out_duration = int(0.025 * samplerate)  # 50 ms fade-out
    fade_in = np.linspace(0, 0.75, fade_in_duration)
    fade_out = np.linspace(0.75, 0, fade_out_duration)
    wave[:fade_in_duration] *= fade_in
    wave[-fade_out_duration:] *= fade_out

    stereo_wave = np.column_stack([wave, wave])
    write(filename, samplerate, stereo_wave.astype(np.float32))


def ensure_beep_files(dir):
    """
    Ensure that the short and long beep sound files exist, creating them if necessary.
    """
    if not os.path.exists(os.path.join(dir, "beep_short.wav")):
        generate_beep(os.path.join(dir, "beep_short.wav"), 0.1)  # Short beep (100 ms)
    if not os.path.exists(os.path.join(dir, "beep_long.wav")):
        generate_beep(os.path.join(dir, "beep_long.wav"), 0.3)  # Long beep (300 ms)


class SoundWaves:
    def __init__(self, directory):
        #' Hint: wave files are only usable if they autoplay, when opening
        # them directly with a sound tool in windows or MACOS
        #' Hint: show your sound devices: print(sd.query_devices())
        self.dir = directory
        self.short_beep = os.path.join(self.dir, "beep_short.wav")
        self.long_beep = os.path.join(self.dir, "beep_long.wav")
        self.sound_array = []
        self.pause = np.zeros([20000, 2], dtype="float32")
        self.longer_pause = np.zeros([120000, 2], dtype="float32")

    def save_char(self, value_encoder):
        """saves the morse sound of one char in list
        :param value_encoder: list of morse_digits for the respective char
        :return None
        """

        for code in value_encoder:
            if code == 1:
                data, fs = sf.read(self.short_beep)
            else:
                data, fs = sf.read(self.long_beep)

            self.sound_array.append(
                data
                # sd.playrec(data, fs, channels=2, dtype="float32", blocking=True)
            )
            self.sound_array.append(self.pause)

    def save_wav_format(self) -> None:
        """saves the morse sound of one char in list
        :param None
        :return soundfile in wav-format (no real return value)
        """
        new = np.vstack(self.sound_array)
        write(os.path.join(self.dir, "output.wav"), 44100, new)

    def add_longer_pause(self) -> None:
        """Adds a long pause after the word
        Is only hearable in the output not when recording
        :param None
        :return None
        """
        self.sound_array.append(self.longer_pause)
