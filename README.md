# MIDI Tempo Scaler

A minimal Python utility designed to adjust the tempo (BPM) of a MIDI file while preserving its playback timing and relative note placement.

When you simply change the tempo meta event in a MIDI file, playback speeds up or slows down. This script scales the file's `ticks_per_beat` (resolution) proportionally to the BPM shift, keeping the actual wall-clock playback speed identical while registering the new target BPM header.

---

## Features

* **Tempo Scaling:** Recalculates `ticks_per_beat` to preserve playback speed when shifting BPM.
* **Two Workflows:**
* `midi_tempo_scaler_cli.py`: Command-line interface with customizable arguments.
* `midi_tempo_scaler_quick.py`: Lightweight standalone script for quick code-level edits.


* **Zero Dependencies Beyond Mido:** Uses Python's standard library and the `mido` package.

---

## Requirements

Python 3.6+ and `mido` are required.

```bash
pip install mido

```

---

## Usage

### Option 1: Command-Line Tool (`midi_tempo_scaler_cli.py`)

Run the script from your terminal using flags.

**Default execution:**

```bash
python midi_tempo_scaler_cli.py

```

*(Uses default values: input `input.mid`, output `output.mid`, original BPM `140`, target BPM `100`)*

**Custom parameters:**

```bash
python midi_tempo_scaler_cli.py -i TrackWrong.mid -o TrackRight.mid --orig-bpm 140 --target-bpm 100

```

#### CLI Options

| Flag | Short | Default | Description |
| --- | --- | --- | --- |
| `--input` | `-i` | `input.mid` | Path to the source MIDI file |
| `--output` | `-o` | `output.mid` | Path for the output MIDI file |
| `--orig-bpm` | N/A | `140.0` | Original BPM of the track |
| `--target-bpm` | N/A | `100.0` | Desired target BPM |

---

### Option 2: Quick Script (`midi_tempo_scaler_quick.py`)

If you prefer modifying values directly inside the file without passing terminal flags:

1. Open `midi_tempo_scaler_quick.py` in your code editor.
2. Edit the variables at the top of the script:
```python
INPUT_FILE = 'TrackWrong.mid'
OUTPUT_FILE = 'TrackRight.mid'
ORIGINAL_BPM = 140
TARGET_BPM = 100

```


3. Run the script:
```bash
python midi_tempo_scaler_quick.py

```



---

## How It Works

1. Loads the target MIDI file into memory.
2. Scales `mid.ticks_per_beat` according to the ratio:

$$\text{New Ticks} = \text{Original Ticks} \times \left( \frac{\text{Original BPM}}{\text{Target BPM}} \right)$$


3. Iterates through all tracks, updating existing `set_tempo` header events to match the target BPM.
4. Saves the modified file.
