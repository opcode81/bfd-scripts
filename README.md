# BFD Scripts

This package contains scripts for several purposes:

* **Trim Adjustment.** This allows you to adjust the trim of all samples, e.g. to compensate for overly hot recordings that do not fit well with other BFD sample libraries (`bfdTrimAdjust.py`)
* **Kit Piece Subclass Augmentation**. This allows you to augment missing kit piece subclass information. If the subclass information is missing, filtering for e.g. high/low/floor toms in BFD3 will not work and kit pieces will only show up when using the superclass "Tom" (`bfdAddSubclass.py`)
* **Kit Piece Naming** (for *Platinum Samples Evil Drums*). This function improves the naming of kit pieces for Evil Drums, adding manufacturer and model names; the default names (e.g. "EFB Kit 5 Snare") are uninformative. (`bfdEvilDrumsKitPieceNames.py`)

The first two functions were written for *BFD London Sessions*, which has problems pertaining to both aspects. Its samples are very hot to the point where they induce clipping and will also not combine well with other libraries because they are just plain louder. Furthermore, you cannot conveniently filter for high/floor/rack toms or crash/splash/ride cymbals, because all toms are just "Toms" and all cymbals are just "Cymbals" and do not have the necessary subclass information indicating precisely which type of tom or cymbal it is.

**Applicability.** The trim adjustment script is universal and should apply, without modification, to all BFD3 sample libraries. The subclass augmentation script has some rules that were specifically designed to work with *London Sessions*, but it should be straightforward to adjust/extend the rule set for another library.

## Usage ##

0. The scripts are written for [Python 3](http://www.python.org "Python 3"), so make sure you have the appropriate interpreter installed.
1. Copy the script you want to apply to the BFD sample library location, e.g. to the "BFD London Sessions" directory.
2. Run the script from the command line as described below, or, under Windows, by double-clicking them in Windows Explorer (provided that .py files are opened by the Python 3 interpreter).
3. Make sure the changes take effect:
   * For trim adjustment, 
     * delete the file named `KitPiece.database` and the folder named `LoudnessCache` in BFD3's user data directory (under Windows, find them under `C:\Users\<user>\AppData\Roaming\FXpansion\BFD3`), and then
     * open BFD3 and, under Tools/Set up content locations, rescan all content locations.
   * For subclass/kit piece naming information, open BFD3 and, under Tools/Set up content locations, rescan (or remove and re-add) the content path of the library that was affected for the changes to take effect.


### Trim Adjustment

For trim adjustment, supply the desired trim value as an argument. For *London Sessions*, -5 dB works well.

    python bfdTrimAdjust.py -5

*London Sessions* has all trim values set to 0 by default, so it's easy to go back.

### Adding Subclass Information

To add subclass information, run the `bfdAddSubclass.py` script without any arguments.   

    python bfdAddSubclass.py

The script will not change any existing subclass information; it will only add missing information. For the case where the class it would have added is different class from the one that is present, it will tell you so (see log output).
As stated above, the rules the script contains are designed for *London Sessions*, but the logic could presumably be easily adapted to another library.

### Kit Piece Naming

To improve the kit piece names in Platinum Samples Evil Drums run `bfdEvilDrumsKitPieceNames.py` without any arguments in the Evil Drums library folder.

    python bfdEvilDrumsKitPieceNames.py

The script will adapt all the `Info.xml` files in the library, creating backup files `Info.xml.orig` beside each file. 
