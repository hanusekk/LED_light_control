
# LED light with dimmable power supply control.

Lighting control circuit built with digital potentiometer, operational amplifier and relay steering by Raspberry Pi 4B. 

# Description

The LED power supplies I used have the ability to control the intensity of the light, after applying a voltage in the range of 0-10 V to the DIM+/- outputs. In order not to load the network when suddenly starting up such a large number of power supplies, this function was used . For this purpose, a circuit was created, which is controlled using a Raspberry Pi. This circuit includes an Adafruit DS1841 digital potentiometer, an LMC6482 operational amplifier and a JQC-3F relay.
The output voltage of the potentiometer is regulated in the range of 0.8-5 V by the Raspberry Pi, which in turn is the input voltage for the operational amplifier. After amplification at the DIM+/- pins of the power supplies, we obtain an output voltage in the range of 1-10V. This is represented by the schematic diagram shown in the figure below.

!



