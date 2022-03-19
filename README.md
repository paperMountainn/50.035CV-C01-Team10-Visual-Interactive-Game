# 50.035CV-C01-Team10-Visual-Interactive-Game

## dataset
/dataset


### baseline model idea
/prelim_trial

Detecting colors of blue marker, create a mask around the blue tip. Detect contours of this mask, then output a point to center of blue area. If point in snare bounding box, then output a snare sound.

* for Pris:bounding box code found in virt_drum.py's while True block, define the x y and width at line 107 onwards before you pass into `cv2.rectangle()`
* code for making sounds is found in make_sound.py. To make new sounds, follow the `play_drum()` method, and add your sound file into `sound_file` dir.

To run the baseline model
```
python make_sound.py
```
