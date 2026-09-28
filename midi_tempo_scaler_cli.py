import mido

INPUT_FILE = 'input.mid'
OUTPUT_FILE = 'output.mid'
ORIGINAL_BPM = 140
TARGET_BPM = 100

mid = mido.MidiFile(INPUT_FILE)

mid.ticks_per_beat = int(mid.ticks_per_beat * (ORIGINAL_BPM / TARGET_BPM))
new_tempo = mido.bpm2tempo(TARGET_BPM)

for track in mid.tracks:
    for msg in track:
        if msg.type == 'set_tempo':
            msg.tempo = new_tempo

mid.save(OUTPUT_FILE)
print(f"File updated and saved to '{OUTPUT_FILE}'. Tempo set to {TARGET_BPM} BPM.")