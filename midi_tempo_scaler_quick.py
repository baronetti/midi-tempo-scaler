import argparse
import mido

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default='input.mid')
parser.add_argument('-o', '--output', default='output.mid')
parser.add_argument('--orig-bpm', type=float, default=140.0)
parser.add_argument('--target-bpm', type=float, default=100.0)
args = parser.parse_args()

mid = mido.MidiFile(args.input)

mid.ticks_per_beat = int(mid.ticks_per_beat * (args.orig_bpm / args.target_bpm))
new_tempo = mido.bpm2tempo(args.target_bpm)

for track in mid.tracks:
    for msg in track:
        if msg.type == 'set_tempo':
            msg.tempo = new_tempo

mid.save(args.output)
print(f"File updated and saved to '{args.output}'. Tempo set to {args.target_bpm} BPM.")