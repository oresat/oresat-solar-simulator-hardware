# oresat-kicad
All things KiCAD for OreSat; libraries, tools, settings, etc.

## Getting started

To start using these libraries, you should set up an environment variable within KiCAD pointing to `oresat-kicad` on your system.

* In the KiCAD menu open Preferences > Configure Paths.
* Under "Environment Variables" click the "+" button to add a new environment variable and name it `ORESAT_LIBRARIES`.
* In the path area, enter (or browse for) the `oresat-kicad` repository on your system.
* Click Ok.

That's it! Now when you open a project that uses these libraries with the `ORESAT_LIBRARIES` variable, KiCAD will use the path you provided to locate them.

## Adding libraries to your project

Once you've set up the `ORESAT_LIBRARIES` environment variable, you can also start adding these libraries to your own projects.

* Open up your project.
* In the project panel, choose Preferences > Manage Symbol Libraries.
* Select the "Project Specific Libraries" tab.
   * MAKE SURE YOU ADD THE LIBRARY TO "Project Specific Libraries" AND NOT "Global Libraries".
* Click on the Folder icon below.
   * THIS IS IMPORTANT. DO NOT CLICK ON "+". CLICK ON THE FOLDER.
* In your project folder, navigate to `oresat-kicad/oresat-symbols` and choose the symbol(s) you want. You can include all of them if you want!
* Choose Open, then OK.
* Back in the project panel, choose Preferences > Manage Footprint Libraries.
* Select the "Project Specific Libraries" tab.
   * MAKE SURE YOU ADD THE LIBRARY TO "Project Specific Libraries" AND NOT "Global Libraries".
* Click on the Folder icon below.
   * THIS IS IMPORTANT. DO NOT CLICK ON "+". CLICK ON THE FOLDER.
* In your project folder, navigate to `oresat-kicad/oresat-footprints` and choose the footprint libraries you want.
* Choose Open, then OK.

At this point, your project should be pointing to your oresat-kicad repository and you should be good to go!

# Library files

These are both symbol (.kicad\_sym) and footprint (.pretty) names

- `oresat-connectors` = all connectors
- `oresat-diodes` = all diodes, including LEDs
- `oresat-graphics` = logos, graphics, etc.
- `oresat-ics` = all ICs, including digital and analog, power, oscillators, etc.
- `oresat-misc` = Batteries, HW, test points, switches
- `oresat-passives` = Resistors, capacitors, inductors, crystals, ferrite beads, fuses, TVS, etc.
- `oresat-pcbs` = all pcbs, including card and end cap outlines, and SBC shields / capes, etc.
- `oresat-transistors` = All transistor types

# LICENSE

Copyright the Portland State Aerospace Society 2022.

This source describes Open Hardware and is licensed under CERN-OHL-S v2 or any later version.

You may redistribute and modify this source and make products using it under the terms of the CERN-OHL-S v2 (https://ohwr.org/cern_ohl_s_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-S v2 for applicable conditions.

Source location: https://github.com/oresat

As per CERN-OHL-S v2 section 4, should You produce hardware based on this source, You must where practicable maintain the Source Location visible on the external case of the Gizmo or other products you make using this source.

