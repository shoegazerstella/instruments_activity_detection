# Instruments Activity Detection using Spleeter and Auditok

Detect individual instruments activity in an audio file.

This project relies on [spleeter](https://github.com/deezer/spleeter) for performing source separation and on [auditok](https://github.com/amsehili/auditok) for the activity detection.

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
python run.py david_bowie life_on_mars
```

## Output

start-end-duration of each instrument is saved as `[instrument].txt` in the `data` dir.

```
Instruments Timeline

     start tags
0      8.0   🎤🎶
265   10.0    🎶
140   10.0    🎹
266   12.0    🎶
210   12.0    🎸
..     ...  ...
136  239.0    🥁
137  239.0    🥁
264  239.0    🎸
138  241.0    🥁
139  243.0    🥁
```


```
 drums 

   start    end  duration
0  35.20  35.51      0.31
1  41.97  42.97      1.00
2  46.13  46.48      0.35
3  49.47  49.83      0.36
4  56.91  61.20      4.29
-------------------

 piano 

   start    end  duration
0   9.99  10.33      0.34
1  11.96  16.96      5.00
2  16.96  21.96      5.00
3  21.96  26.96      5.00
4  26.96  29.23      2.27
-------------------

 vocals 

   start    end  duration
0   8.21  12.98      4.77
1  14.47  17.52      3.05
2  18.61  21.50      2.89
3  22.75  25.95      3.20
4  26.96  30.21      3.25
-------------------

 other 

   start    end  duration
0   8.21   9.21      1.00
1   9.68  11.09      1.41
2  11.87  13.16      1.29
3  13.24  15.55      2.31
4  15.58  20.58      5.00
-------------------

 bass 

   start    end  duration
0  11.89  14.92      3.03
1  14.94  19.55      4.61
2  21.23  23.37      2.14
3  31.82  34.74      2.92
4  35.68  36.83      1.15
-------------------

Instruments and their durations:

other 231.89
bass 206.09
drums 161.37
vocals 159.87
piano 107.38
```
