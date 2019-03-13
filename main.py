import numpy as np
import time


class Photo:
    def __init__(self, i, o, n, t):
        self.i = i
        self.o = o
        self.n = n
        self.t = t
        self.u = False


class Slide:
    def __init__(self, p, t):
        self.p = p
        self.t = t

class Process(Photo):
    def __init__(self):
        self.gallery_v = []
        self.gallery_h = []

    def load(self, filename):
        f = open(filename, 'r')
        for i, l in enumerate(f):
            if i == 0:
                continue
            pic = l.rstrip().split()
            photo = Photo(i, pic[0], pic[1], pic[2:])
            if photo.o == 'H':
                self.gallery_h.append(photo)
            elif photo.o == 'V':
                self.gallery_v.append(photo)
    
    def interest_factor(self, p1, p2):
        size1 = len(set(p1) - set(p2))
        size2 = len(set(p1).intersection(set(p2)))
        size3 = len(set(p2) - set(p1))
        return min(size1, size2, size3)

    def display(self):
        for el in self.h_tmp:
            print(el.t)

    def strat1(self):
        self.slideshow = []
        self.v_tmp = sorted(self.gallery_v, key=lambda p: p.n)
        self.h_tmp = sorted(self.gallery_h, key=lambda p: p.n)
        for i in range(len(self.h_tmp)):
            if self.h_tmp[i].u:
                continue
            
            for j in range(len(self.v_tmp)):
                if self.v_tmp[j].u:
                    continue

                v = self.v_tmp
                vv = []
                for x in range(len(v)):
                    vv.append(interest_factor(self.h_tmp[i], v[x]))

                

if __name__ == '__main__':
    start = time.time()
   
    p = Process()
    p.load('../data/a_example.txt')
    p.strat1()
    p.display()

    print('\nExecution finished in {:.2f}s'.format(time.time() - start))
