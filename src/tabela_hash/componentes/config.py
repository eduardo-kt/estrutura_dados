from collections import namedtuple

N = 10
TABELAHASH = [None] * N

setup = namedtuple("setup", ["tabelahash", "n"])
INICIAL = setup(tabelahash=TABELAHASH, n=N)
