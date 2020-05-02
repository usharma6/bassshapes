import matplotlib.pyplot as pyplt
import numpy as np
import re
from a_major import a_major_map

def parser(filename):
    header_splitter = re.compile('###\\s+')
    note_splitter = re.compile(',\\s+')
    value_splitter = re.compile(':')
    #octave_splitter = re.compile('\-+|\++')
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
            pitch -= 8
            value = value[:-1]

        pitch += note_map[value]

        pitches.append(float(pitch))
        times.append(float(time))

    return pitches, times

def make_colors(pitches):
    clr_map = {0:'#FFFFFF', 1:'#ee1100', 1.5:'#ff3311', 2:'#ff4422', 2.5:'#ff6644', 3:'#feae2d', 4:'#d0c310', 4.5:'#aacc22', 5:'#69d025', 5.5:'#22ccaa', 6:'#4444dd', 6.5:'#3311bb', 7:'#442299'}
    clrs = []
    for p in pitches:
        if (p % 8 != 0):
            clrs.append(clr_map[p % 8])
        else:
            if p ==0:
                clrs.append(clr_map[0])
            else:
                clrs.append(clr_map[1])
    return clrs

def set_ticks(times):
    last = times[-1]
    ticks = np.arange(start = 0, stop = last, step = 4)
    print(ticks)
    return ticks

def main():
    pitches, times = parser('oh_darling.txt')
    x = np.cumsum(times)
    #print(pitches)
    #print(times)
    #print(x)
    note_map = a_major_map()
    print(note_map.values())
    values = note_map.values()
    print(values)
    fig = pyplt.figure(figsize = (50, 10))
    pyplt.yticks(np.arange(start = -8, stop = 16, step = 0.5))
    pyplt.xticks(set_ticks(x))
    colors = make_colors(pitches)
    pyplt.scatter(x,pitches, c=colors)
    pyplt.plot(x,pitches)
    pyplt.savefig('oh_darling.png', bbox_inches = 'tight')
    
if __name__ == '__main__':
    main()
    #parser("oh_darling.txt")
