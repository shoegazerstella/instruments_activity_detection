# Instruments Activity Detection using Spleeter and Auditok

Detect individual instruments activity in an audio file.
The project relies on [spleeter](https://github.com/deezer/spleeter) for performing source separation and on [auditok](https://github.com/amsehili/auditok) for the activity detection.

## Installation

for Auditok run

```
git clone https://github.com/amsehili/auditok.git
cd auditok
python setup.py install
```

then run

```
pip install -r requirements.txt
```

## Usage

Provide an audio file

```
python run.py -a my_audio_file.mp3
```

use youtube-dl to download from a query of [artist] [song]

```
python run.py billie_eilish bad_guy
```

## Output

start-end-duration of each instrument is saved as `[instrument].txt` in the `data` dir.

```
 drums 

   start    end  duration
0  14.08  19.08       5.0
1  19.08  24.08       5.0
2  24.08  29.08       5.0
3  29.08  34.08       5.0
4  34.08  39.08       5.0
-------------------

 piano 

Empty DataFrame
Columns: [start, end, duration]
Index: []
-------------------

 vocals 

   start   end  duration
0   1.30  1.84      0.54
1   1.91  2.36      0.45
2   2.56  3.24      0.68
3   3.44  3.95      0.51
4   4.05  9.05      5.00
-------------------

 other 

   start    end  duration
0  24.45  24.83      0.38
1  74.54  79.54      5.00
2  79.54  84.54      5.00
3  84.54  87.68      3.14
4  93.88  94.34      0.46
-------------------

 bass 

   start    end  duration
0  14.09  19.09      5.00
1  19.09  24.09      5.00
2  24.09  27.90      3.81
3  28.31  33.31      5.00
4  33.31  38.31      5.00
-------------------

Instruments and their durations:

drums 166.43
vocals 158.41
bass 151.44
other 43.61
piano 0.0
```
