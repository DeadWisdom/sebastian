#!/usr/bin/env python

import random

from sebastian.lilypond.interp import parse
from sebastian.midi.write_midi import SMF
from sebastian.core import OSequence
from sebastian.core.transforms import transpose


patterns = [
    r"\relative c' { \acciaccatura c8 e4 \acciaccatura c8 e4 \acciaccatura c8 e4 }",  # 1
    r"\relative c' { \acciaccatura c8 e8 f8 e4 }",
    r"\relative c' { r8 e8 f8 e8 }",
    r"\relative c' { r8 e8 f8 g8 }",
    r"\relative c' { e8 f8 g8 r8 }",  # 5
    r"\relative c'' { c1~ c1 }",
    r"\relative c' { r4 r4 r4 r8 c16 c16 c8 r8 r4 r4 r4 r4 }",
    r"\relative c'' { g1. f1~ f1 }",
    r"\relative c'' { b16 g16 r8 r4 r4 r4 }",
    r"\relative c'' { b16 g16 }",  # 10
    r"\relative c' { f16 g16 b16 g16 b16 g16 }",
    r"\relative c' { f8 g8 b1 c4}",
    r"\relative c'' { b16 g8. g16 f16 g8 r8. g16~ g2. }",
    r"\relative c'' { c1 b1 g1 fis1 }",
    r"\relative c'' { g16 r8. r4 r4 r4 }",  # 15
    r"\relative c'' { g16 b16 c16 b16 }",
    r"\relative c'' { b16 c16 b16 c16 b16 r16 }",
    r"\relative c' { e16 fis16 e16 fis16 e8. e16 }",
    r"\relative c'' { r4. g'4. }",
    r"\relative c' { e16 fis16 e16 fis16 g,8. e'16 fis16 e16 fis16 e16 }",  # 20
    r"\relative c' { fis2.}",
    r"\relative c' { e4. e4. e4. e4. e4. fis4. g4. a4. b8 }",
    r"\relative c' { e8 fis4. fis4. fis4. fis4. fis4. g4. a4. b4 }",
    r"\relative c' { e8 fis8 g4. g4. g4. g4. g4. a4. b8 }",
    r"\relative c' { e8 fis8 g8 a4. a4. a4. a4. a4. b4. }",  # 25
    r"\relative c' { e8 fis8 g8 a8 b4. b4. b4. b4. b4. }",
    r"\relative c' { e16 fis16 e16 fis16 g8 e16 g16 fis16 e16 fis16 e16}",
    r"\relative c' { e16 fis16 e16 fis16 e8. e16 }",
    r"\relative c' { e2. g2. c2. }",
    r"\relative c' { c'1. }",  # 30
    r"\relative c'' { g16 f16 g16 b16 g16 b16 }",
    r"\relative c' { f16 g16 f16 g16 b16 f16~ f2. g4. }",
    r"\relative c'' { g16 f16 r8 }",
    r"\relative c'' { g16 f16 }",
    r"\relative c' { f16 g16 b16 g16 b16 g16 b16 g16 b16 g16 r8 r4 r4 r4 bes4 g'2. a8 g8~ g8 b8 a4. g8 e2. g8 fis8~ fis2. r4 r4 r8 e8~ e2 f1. }",  # 35
    r"\relative c' { f16 g16 b16 g16 b16 g16 }",
    r"\relative c' { f16 g16 }",
    r"\relative c' { f16 g16 b16 }",
    r"\relative c'' { b16 g16 f16 g16 b16 c16 }",
    r"\relative c'' { b16 f16 }",  # 40
    r"\relative c'' { b16 g16 }",
    r"\relative c'' { c1 b1 a1 c1 }",
    r"\relative c'' { f16 e16 f16 e16 e8 e8 e8 f16 e16 }",
    r"\relative c'' { f8 e8~ e8 e8 c4 }",
    r"\relative c'' { d4 d4 g,4 }",  # 45
    r"\relative c'' { g16 d'16 e16 d16 r8 g,8 r8 g8 r8 g8 g16 d'16 e16 d16 }",
    r"\relative c'' { d16 e16 d8 }",
    r"\relative c'' { g1. g1 f1~ f4 }",
    r"\relative c' { f16 g16 bes16 g16 bes16 g16 }",
    r"\relative c' { f16 g16 }",  # 50
    r"\relative c' { f16 g16 bes16 }",
    r"\relative c'' { g16 bes16 }",
    r"\relative c'' { bes16 g16 }",
]


# make a separate MIDI file for each pattern

def separate_files():
    for num, pattern in enumerate(patterns):
        sequence = parse(pattern)
        f = open("in_c_%s.mid" % (num + 1), "w")
        s = SMF([sequence])
        s.write(f)
        f.close()


# make a single MIDI file with all the patterns in a row

def one_file():
    seq = OSequence([])
    for num, pattern in enumerate(patterns):
        seq = seq + parse(pattern) * 10
    f = open("in_c_all.mid", "w")
    s = SMF([seq])
    s.write(f)
    f.close()

# performance


def performance():
    tracks = []
    for track_num in range(8):  # 8 tracks
        seq = OSequence([])
        for pattern in patterns:
            seq += parse(pattern) * random.randint(2, 5)  # repeat 2-5 times
        tracks.append(seq | transpose(random.choice([-12, 0, 12])))  # transpose -1, 0 or 1 octaves
    f = open("in_c_performance.mid", "w")
    s = SMF(tracks)
    s.write(f)
    f.close()


performance()
