import ctypes
from sound_lib import output, stream

# Initialize audio output with error handling for headless/no-audio systems
try:
    o = output.Output()
except Exception as e:
    print(f"Warning: Could not initialize audio output: {e}")
    print("Running in silent mode (no sound effects)")
    o = None


# this is easy so violence begets violence or something
class SoundCacher:
    def __init__(self):
        self.cache = {}
        self.refs = []  # so sound objects don't get eaten by the gc

    def play(self, file_name, pan=0.0, volume=1.0, pitch=1.0):
        if o is None:
            # Silent mode - no audio device available
            return None

        if file_name not in self.cache:
            with open(file_name, "rb") as f:
                self.cache[file_name] = ctypes.create_string_buffer(f.read())
        sound = stream.FileStream(
            mem=True, file=self.cache[file_name], length=len(self.cache[file_name])
        )
        if pan:
            sound.pan = pan
        if volume != 1.0:
            sound.volume = volume
        if pitch != 1.0:
            sound.set_frequency(int(sound.get_frequency() * pitch))
        sound.play()
        self.refs.append(sound)
        return sound
