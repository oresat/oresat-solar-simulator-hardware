# oresat-solar-simulator-hardware

The hardware repository for our solar simulator for testing [OreSat 1U solar panels](https://github.com/oresat/oresat-solar-hardware)

## General Information

The OreSat Solar Simulator is a benchtop simulator for hardware-in-the-loop testing of CubeSat solar modules. It uses LED and halogen light bulbs to emit light that simulates the sun's solar spectrum in low Earth orbit (Air Mass 0 or 'AM0').

The work for this was done as an MCECS Capstone Project from January to June of 2023 by Bendjy Faurestal, Adam Martinez, Cesar Ordaz-Coronel, and Charles Nasser. Andrew Greenberg was both representing PSAS as the Industry Sponsor and the Faculty Advisor to the students.

## Hardware
Controller board top:
![controller-board-top](https://oresat.github.io/oresat-solar-simulator-hardware/top.png)
Bottom:
![controller-board-bottom](https://oresat.github.io/oresat-solar-simulator-hardware/bottom.png)

The schematic and pcb layout were designed in [kiCAD](https://www.kicad.org/download/). The boards we used were fabricated by [OSHPark](https://oshpark.com/) in Lake Oswego, OR.

The simulators are driven by a Raspberry Pi Pico attached to the board.

## Software

The software for this project lives in the [oresat-solar-simulator-software](https://github.com/oresat/oresat-solar-simulator-software) repository.

## Mechanical

The mechanical components were developed by Zeus Ayala using onShape.

![housing](housing-render.png)
