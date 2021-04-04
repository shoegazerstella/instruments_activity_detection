import os
import pygame
import numpy as np
import time
import pandas as pd
from pygame.locals import *

THIS_PATH = os.path.abspath(os.getcwd())


def get_tags(path):

    tags_path = os.path.join(THIS_PATH, 'data', path, path)
    df = pd.read_csv( os.path.join(tags_path, 'tags.txt'), sep='\t')

    events = np.round( df['start'].tolist() )
    tags = df['tags'].tolist()

    events_dict = dict(zip(events, tags))

    return events_dict


def viz(path):

    pygame.init()  
    pygame.mixer.init()

    events_dict = get_tags(path)

    sound_path = os.path.join(THIS_PATH, 'data', path + '.mp3')
    soundObj = pygame.mixer.Sound(sound_path)

    while True:

        soundObj.play()
        start_time = 0

        while True:

            time_since_enter = pygame.time.get_ticks() - start_time

            try:
                time.sleep(0.2) # add some delay
                print('\n\n', events_dict[ np.round(time_since_enter/1000.0) ]) # end=' ')

            except Exception as e:
                pass

if __name__ == '__main__':

    path='david_bowie_life_on_mars'

    viz(path=path)