# OreSat FlatSat

A "flatsat" is a integration and debugging configuration of your satellite that allows you to more easily do system integration, software development, testing, and debugging. It's the "open" satellite that allows you to get at all the signals and ports.

Here's what our OreSat0 flatsat looks like -- note the cards laid out flat on the table, the power supply on the left, the ribbon cable and cards, and the small PC on the upper right (vertical wall) that interfaces everything to the interwebs.

![OreSat 1U Backplane Picture](https://github.com/oresat/oresat-flatsat/raw/master/images/oresat-flatsat.jpg)

Here's a closeup of the cards: the 40 wire ribbon cable mimics our backplane, the "flatsat breakout boards" interface the cards to the ribbon cable backplane, and the "card debug boards" at the bottom of some of the cards are JTAG, serial, USB, and some spare GPIO that's common to all cards.

![OreSat 1U Backplane Picture](https://github.com/oresat/oresat-flatsat/raw/master/images/oresat-flatsat-cards.jpg)

# Some notes

- We ordered 6 inch ribbon cables, but had to cut them down to 4" to pack the cards on our small table. We did that by cutting the ribbon cable and pressing on an IDC connector.
- Don't forget to add termination resistors to both sides of the ribbon cable.
- The "exteranal supply shutdown" board kills the external power supply when the watchdog (or inhibit switches) pull the !SHUTDOWN signal low.
- You need very flexible USB micro cables for this to work well.
- FFCs suck. But, they're still better than anything else.

# LICENSE

Copyright the Portland State Aerospace Society 2021.

This source describes Open Hardware and is licensed under CERN-OHL-S v2 or any later version.

You may redistribute and modify this source and make products using it under the terms of the CERN-OHL-S v2 (https://ohwr.org/cern_ohl_s_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-S v2 for applicable conditions.

Source location: https://github.com/oresat/

As per CERN-OHL-S v2 section 4, should You produce hardware based on this source, You must where practicable maintain the Source Location visible on the external case of the Gizmo or other products you make using this sourc

