# BFD Scripts

This package contains scripts that serve two purposes:

* to adjust the trim of all samples, e.g. to compensate for overly hot recordings that do not fit well with other BFD sample libraries (`bfdTrimAdjust.py`)
* to augment missing kit piece subclass information. If the subclass information is missing, filtering for e.g. high/low/floor toms in BFD3 will not work and kit pieces will only show up when using the superclass "Tom" (`bfdAddSubclass.py`)

The sample library ***BFD London Sessions*** has problems pertaining to both aspects. Its samples are very hot to the point where they induce clipping and will also not combine well with other libraries because they are just plain louder. Furthermore, you cannot conveniently filter for high/floor/rack toms or crash/splash/ride cymbals, because all toms are just "Toms" and all cymbals are just "Cymbals" and do not have the necessary subclass information indicating precisely which type of tom or cymbal it is.

**Applicability.** The trim adjustment script is universal and should apply, without modification, to all BFD3 sample libraries. The subclass augmentation script has some rules that were specifically designed to work with *London Sessions*, but it should be straightforward to adjust/extend the rule set for another library.

## Usage ##

0. The two scripts are written for [Python 2](http://www.python.org "Python 2"), so make sure you have the appropriate interpreter installed. (The scripts could be easily modified to work with Python 3; I believe only the print statements would need to be changed.)

1. Copy the script you want to apply to the BFD sample library location, e.g. to the "BFD London Sessions" directory.

2. Run the script from the command line as described below.

3. Open BFD3 and re-scan the content path of the library that was affected. (Tools - Set up content locations)


### Trim Adjustment

For trim adjustment, supply the desired trim value as an argument. For *London Sessions*, -5 dB works well.

    python bfdTrimAdjust.py -5

*London Sessions* has all trim values set to 0 by default, so it's easy to go back.

### Adding Subclass Information

To add subclass information, run the `bfdAddSubclass.py` script without any arguments.   

    python bfdAddSubclass.py

The script will not change any existing subclass information; it will only add missing information. For the case where the class it would have added is different class from the one that is present, it will tell you so (see log output).
As stated above, the rules the script contains are designed for *London Sessions*, but the logic could presumably be easily adapted to another library.





