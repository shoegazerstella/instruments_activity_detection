import os
import sys
import argparse
import subprocess
import pandas as pd
import operator
import numpy as np

from spleeter.separator import Separator

THIS_PATH = os.path.abspath(os.getcwd())


def youtube_download(artist, song, ext='mp3'):
    """
    Downloads first result of search 'artist - song' from youtube. Requires youtube-dl to be installed
    """
    
    outdir = os.path.join(THIS_PATH, 'data')    

    filename = artist + '_' + song
    audio_file = os.path.join(outdir, filename + '.' + ext)

    if not os.path.exists(audio_file):
        search = 'ytsearch1:{} {}'.format( artist.replace('_',' '), song.replace('_',' ') )
        cmd = [ 'youtube-dl', '--extract-audio', '--audio-format', ext, '-o', os.path.join(outdir, filename) + '.' + '%(ext)s', search]
        subprocess.call(cmd)

    return audio_file


def run_spleeter(audio_file, model='spleeter:5stems'):

    print('Performing source separation using', model)

    destination = os.path.splitext(audio_file)[0]

    if not os.path.exists(destination):
        separator = Separator(model)
        separator.separate_to_file(audio_descriptor=audio_file, destination=destination)
    
    return destination


def process(audio_file):
    
    print('processing', audio_file)

    # spleeter separation
    destination = run_spleeter(audio_file)

    instruments = os.listdir(destination)
    instruments = [i for i in instruments if '.wav' in i]

    duration = {}

    for instr in instruments:

        instr = os.path.splitext(instr)[0]
        
        print('\n', instr, '\n')

        input_file = os.path.join(THIS_PATH, destination, instr + '.wav')
        dest_file = os.path.join(THIS_PATH, destination, instr + '.txt')
        
        cmd = [ 'auditok', '-i', input_file]
        output = subprocess.check_output(cmd, encoding='UTF-8')
        output = output.split('\n')
        output = [i.split(' ') for i in output]

        start = []
        end = []

        for i in output:
            
            if len(i) == 3:

                start.append(float(i[1]))
                end.append(float(i[2]))

        df = pd.DataFrame()
        df['start'] = start
        df['end'] = end
        df['duration'] = df['end'] - df['start']

        print(df.head())
        print('-------------------')
        
        df.to_csv(dest_file, sep='\t', index=False)

        duration[instr] = df['duration'].sum()

    duration = dict(sorted(duration.items(),key=operator.itemgetter(1),reverse=True))

    print('\nInstruments and their durations:\n')
    for k, v in duration.items():
        print(k, np.round(v, 2))

    return


def main():

    parser = argparse.ArgumentParser(description='Instruments activity detection.')

    parser.add_argument('-a', '--audio_file', nargs='?',
                        help='path to audio file to process')
    parser.add_argument('artist', nargs='?',
                        help='artist name')
    parser.add_argument('song', nargs='?',
                        help='song title')

    args = vars(parser.parse_args())

    if args['audio_file'] is None:
        if args['artist'] and args['song']:
            print('Downloading audio from youtube..')
            audio_file = youtube_download(args['artist'], args['song'], ext='mp3')
            args['audio_file'] = audio_file
        else:
            raise Exception("Provide either an audio file or artist and song title")
        
    process(audio_file=args['audio_file'])

if __name__ == '__main__':
    main()
