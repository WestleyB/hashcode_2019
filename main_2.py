import sys


def load_data():
    file = open(sys.argv[1])

    v_gallery = []
    h_gallery = []
    
    nb_photos = 0
    
    for i, l in enumerate(file):
        if i == 0:
            nb_photos = int(l)
            continue
        
        l = l.rstrip().split(" ")
        orientation = l[0]
        nb_tags = l[1]
        tags = l[2:]
        
        if orientation == 'H':
            h_gallery.append({
                'id': i-1,
                'nb_tags': nb_tags,
                'tags':tags,
                'used': False
                })
        
        if orientation == 'V':
            v_gallery.append({
                'id': i-1,
                'nb_tags': nb_tags,
                'tags':tags,
                'used': False})
    
    h_gallery = sorted(h_gallery, key=lambda p: p['nb_tags'])
    v_gallery = sorted(v_gallery, key=lambda p: p['nb_tags'])
    
    return nb_photos, h_gallery, v_gallery

def interest_factor(tags1, tags2):
    size1 = len(set(tags1) - set(tags2))
    size2 = len(set(tags1).intersection(set(tags2)))
    size3 = len(set(tags2) - set(tags1))

    return min(size1, size2, size3)

def submission(filename, slide_show):
    with open(filename, "w") as output_file:
        output_file.write(str(len(slide_show)) + "\n")

        for i in slide_show:
            output_file.write(i)
            output_file.write("\n")

if __name__ == '__main__':

    nb_photos, h_gallery, v_gallery = load_data()
    
    slide_show = []
    
    v_nb_used = 0
    
    for i in range(len(h_gallery)):
        photo1 = h_gallery[i]
        tags1 = h_gallery[i]['tags']
        slide_show.append(str(photo1['id']))

        if v_nb_used == len(v_gallery):
            continue

        max_match = 0
        tag_max = []

        for j in range(len(v_gallery)):

            photo2 = v_gallery[j]
            if photo2['used']:
                continue
            tags2 = v_gallery[j]['tags']
            photo2['used'] = True

            if interest_factor(tags1, tags2) >  max_match:
                photo_max = v_gallery[j]
                tag_max = tags2
                max_match = interest_factor(tags1, tags2)

            max_match_v = 0

            for k in range(len(v_gallery)):
                photo3 = v_gallery[::-1][k]
                if photo3['used']:
                    continue
                tags3 = v_gallery[::-1][k]['tags']

                if interest_factor(tag_max, tags3) > max_match_v:
                    max_match_v = interest_factor(tag_max, tags3)
                    slide_show.append(str(photo_max['id']) + ' ' + str(photo3['id']))
                    photo3['used'] = True
                    v_nb_used += 2
                    break
            break


    submission(sys.argv[2], slide_show)
