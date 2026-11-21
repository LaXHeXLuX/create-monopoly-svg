# create-monopoly-svg

A program to create all necessary files for your own customized Monopoly game, whether for a digital game or printable board game.

## Quick guide
- Clone the repo.
- Change confs (relating to [game logic](conf/game.py), [visuals](conf/ui.py), or [texts](conf/texts.py) and [long texts](conf/long_texts.py)) where necessary.
- Add missing decal files.
- Run `python main.py a`.
- Check output folder for svg files, change confs if necessary.
- If you need to convert them to png/pdf/..., you must do so yourself.

## Configuration
Configuration is divided into four files:
- [game.py](conf/game.py) &mdash; for board layout, property values, rents, house costs, etc. If you plan to follow the standard rules then you don't need to change anything here.
- [texts.py](conf/texts.py) &mdash; for customizing property names, the game name, as well as other small strings that show up on the board or cards.
- [long_texts.py](conf/long_texts.py) &mdash; like the last one, but for longer multi-line strings, like on the utility cards and chance/community cards. Texts respect newline (`\n`) characters.
- [ui.py](conf/ui.py) &mdash; for customizing anything visual, like colors, fonts, or game board dimensions. If you want the standard Monopoly look then you don't need to change those. However, you will need to change IMAGE_SCALE values so your decals look good on the board and cards, and might need to edit the *special* dict in the *image_file* method as well (explained in the next section).

All texts are currently customized for an Estonian Hiiumaa-oriented game.

## Adding your images
I've included decals of the community chest and chance icons, the tax tile icons, and the GO square arrow. As a placeholder, the chance icon also replaces everything else, so you can test the program before adding your images.

Add your images to the decals folder and name them as such:
- Community chest: "CH.svg"
- Chance: "CC.svg"
- Free Parking (one of the corners): "FP.svg"
- Go arrow (one of the corners): "GO.svg"
- Go to jail (one of the corners): "GTJ.svg"
- Station: "S.svg"
- First tax: "T0.svg"
- Second tax: "T1.svg"
- First utility: "U0.svg"
- Second utility: "U1.svg"

If any of your decals isn't an svg file, you must add their whole filename (with the corresponding tag) to the *special* dict in the *image_file* method. For example, if your station image is a jpg named `kings cross.jpg`, then add `"S": "kings cross.jpg"` to the *special* dict.

## Text in fragile places
Probably the most finnicky part of the program is creating the corners. If you change a text in the `#corners` section of [texts.py](conf/texts.py) and the resulting board corner looks wrong, you may have to look around in [corner.py](generators/corner.py) and see if you can fix it yourself. 

The same might go for other small-detail texts on cards, e.g. the "plus four houses" text or the logo text on chance/community cards.