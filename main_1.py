import numpy as np
import math

folder = './inputs/'
file_name = 'a_example.txt'
path = folder + file_name 


def load_data(filename):
    file = open(folder + filename)
    
    lines = []
    nb_photos = 0
    for i, l in enumerate(file):
        if i == 0:
            nb_photos = int(l)
            continue
        
        l = l.rstrip()
        line = l.split(" ")
        lines.append(line)

    data = np.array(lines)

    return nb_photos, data

def process(data, nb_photos):
    score = 0
    for i in range(nb_photos - 1):
        direction = data[i][0]
        nb_tags = int(data[i][1])
        tags = data[i][2:]
        score += interest_factor(tags, data[i+1][2:])
    return score

def submission(nb_photos, photos_indexes)
    for i in range(nb_photos):
        photos_indexes[i, :]
        

def interest_factor(p1, p2):
    size1 = len(set(p1) - set(p2))
    size2 = len(set(p1).intersection(set(p2)))
    size3 = len(set(p2) - set(p1))

    return min(size1, size2, size3)

if __name__ == "__main__":
    nb_photos, data = load_data(file_name)
    score = process(data, nb_photos)
    print("Score of the slideshow : {}".format(score))



