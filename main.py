import matplotlib.pyplot as pyplt
import numpy as np
import re
from scales import a_major_map, c_major_map

def parser(filename):
    header_splitter = re.compile('###\\s+')
    note_splitter = re.compile(',\\s+')
    value_splitter = re.compile(':')
    #note_map = c_major_map()
    note_map = a_major_map()

    pitches = []
    times = []

    content = header_splitter.split(open(filename, 'r').read())
    header, body = content[0], content[1]
    notes = note_splitter.split(body)
    
    for note in notes:
        value, time = value_splitter.split(note)
        pitch = 0
        octave = value[-1]
        if octave == '+':
            pitch += 7
            value = value[:-1]
        elif octave == '-':
            pitch -= 7
            value = value[:-1]

        pitch += note_map[value]

        pitches.append(float(pitch))
        times.append(float(time))

    return pitches, times

def make_colors(pitches):
    clr_map = {-1:'#FFFFFF', 0:'#ee1100', 0.5:'#ff3311', 1:'#ff4422', 1.5:'#ff6644', 2:'#feae2d', 3:'#d0c310', 3.5:'#aacc22', 4:'#69d025', 4.5:'#22ccaa', 5:'#4444dd', 5.5:'#3311bb', 6:'#442299'}
    clrs = []
    for p in pitches:
        if np.isnan(p):
            clrs.append(clr_map[-1])
        elif (p % 7 != 0):
            clrs.append(clr_map[p % 7])
        else:
            clrs.append(clr_map[0])
    return clrs

def set_ticks(times):
    last = times[-1]
    ticks = np.arange(start = 0, stop = last, step = 4)
    return ticks

def main():
    pitches, times = parser('songs/oh_darling.txt')
    #pitches, times = parser('songs/cissy_strut.txt')
    #pitches, times = parser('songs/1612.txt')
    x = np.cumsum(times)
    fig = pyplt.figure(figsize = (100, 10))
    pyplt.yticks(np.arange(start = -8, stop = 16, step = 0.5))
    pyplt.xticks(set_ticks(x))
    #pitches = np.ma.masked_where(pitches == 0, pitches) 
    colors = make_colors(pitches)
    pyplt.scatter(x, pitches, c=colors)
    pyplt.plot(x, pitches)
    #pyplt.savefig('charts/1612.png', bbox_inches = 'tight')
    #pyplt.savefig('charts/cissy_strut.png', bbox_inches = 'tight')
    pyplt.savefig('charts/oh_darling.png', bbox_inches = 'tight')
    
if __name__ == '__main__':
    main()
