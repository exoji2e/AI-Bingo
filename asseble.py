import cv2, glob
from random import shuffle

import numpy as np
import AS

imgs = [g for g in glob.glob('imgs/*.png')]

def create_bingo(img_paths):
    order = [i for i in range(len(img_paths))]
    shuffle(order)
    vs = [img_paths[i] for i in order][:25]
    assert len(vs) == 25
    imgs = [cv2.imread(p) for p in vs]
    hstacks = [np.concatenate(tuple(imgs[i:i+5]), axis=0) for i in range(0, 25, 5)]
    full = np.concatenate(tuple(hstacks), axis=1)
    cv2.imwrite('bingo.png', AS.add_border(full))

create_bingo(imgs)

