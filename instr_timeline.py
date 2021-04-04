import os
import pandas as pd
import numpy as np

d = { "vocals": "🎤",
    "drums": "🥁",
    "piano": "🎹",
    "bass": "🎸",
    "other": "🎶"}

def get_events_per_instrument(instrument, datadir, duration_min=3):
    
    df = pd.read_csv( os.path.join(datadir, instrument), sep='\t')
    df[os.path.splitext(instrument)[0]] = [ d[os.path.splitext(instrument)[0]] ] * len(df)

    # keep if duration > duration_min
    #df = df[df['duration'] >= duration_min]
    
    df.drop(['end', 'duration'], axis='columns', inplace=True)
    
    return df

def instruments_timeline(datadir):

    events = list( d.keys() )
    events = [i + '.txt' for i in events]

    events_df = []

    for instrument in events:
        
        df = get_events_per_instrument(instrument, datadir=datadir)
        events_df.append(df)
            
    df1 = pd.merge(events_df[0], events_df[1],  how='outer', left_on=['start'], right_on = ['start'])

    df2 = pd.merge(df1, events_df[2],  how='outer', left_on=['start'], right_on = ['start'])

    df3 = pd.merge(df2, events_df[3],  how='outer', left_on=['start'], right_on = ['start'])

    df4 = pd.merge(df3, events_df[4],  how='outer', left_on=['start'], right_on = ['start'])

    df4 = df4.replace(np.nan, '', regex=True)

    df4 = df4.sort_values(by=['start'])

    #df4.to_csv(os.path.join(datadir, 'tags_all.txt'), sep='\t')

    # tags merged
    df4['tags'] = df4[df4.columns[1:]].apply(
                lambda x: ''.join(x.dropna().astype(str)),
                axis=1
                )

    df4.drop(['vocals', 'drums', 'piano', 'other', 'bass'], axis='columns', inplace=True)

    # round times
    df4['start'] = df4['start'].round(decimals=0)

    df4.to_csv(os.path.join(datadir, 'tags.txt'), sep='\t')

    return df4
