
# LED light with dimmable power supply control.

Lighting control circuit built with digital potentiometer, operational amplifier and relay steering by Raspberry Pi 4B. 

# Description

The LED power supplies I used have the ability to control the intensity of the light, after applying a voltage in the range of 0-10 V to the DIM+/- outputs. In order not to load the network when suddenly starting up such a large number of power supplies, this function was used . For this purpose, a circuit was created, which is controlled using a Raspberry Pi. This circuit includes an Adafruit DS1841 digital potentiometer, an LMC6482 operational amplifier and a JQC-3F relay.
The output voltage of the potentiometer is regulated in the range of 0.8-5 V by the Raspberry Pi, which in turn is the input voltage for the operational amplifier. After amplification at the DIM+/- pins of the power supplies, we obtain an output voltage in the range of 1-10V. This is represented by the schematic diagram shown in the figure below.

![Rysunek9 (1)](https://user-images.githubusercontent.com/92868145/213869015-c4be9014-fdb0-42e4-a854-a70a7ad6719f.png)
## Connections 

The figure shows the idea of connecting the various devices. The microcontroller is to control the potentiometer via the I2C bus. Changing the resistance in the potentiometer will change the voltage at the RW terminal in the range of 0.8-5V. The RW pin is to be coupled to the non-inverting input of an operational amplifier. The amplifier's output is to produce an amplified voltage $U_{wy}$ in the range of 1-10V, which is to be coupled to the normally open contact on the JQC-3F relay controlled from the Raspberry Pi's GPIO17 pin. The normally closed contact of the relay is connected to ground, thus guaranteeing 0 V. The voltage is routed to the DIM+ connector on the LED power supplies. The ground is connected to the DIM- connector. 
If the relay coil is not driven, then the DIM+ terminal receives 0 V, which causes the LED lights to be turned off. By driving the relay coil by putting the GPIO17 pin high, the relay contacts are switched, NO shorting and NC opening. A voltage from the output of the operational amplifier is then directed to the DIM+ pin. Then changing the resistance in the potentiometer from the microcontroller via the I2C bus causes the lighting to brighten or dim.  

![adafruitds1841](https://user-images.githubusercontent.com/92868145/213869173-95c21ba1-460d-48c8-b888-be0a1a96cf62.png)

## Operational Amplifier

To obtain the desired output voltage of the operational amplifier, use the formula for calculating the gain of the circuit. Knowing that the maximum voltage that can be obtained at the input of the amplifier is about 4.8V and knowing the output voltage is 10V, the amplifier gain was calculated. Using the circuit gain formula $A_{(V)}$, the resistance ratio $R_{2}$ to $R_{1}$ was calculated and resistors were used accordingly: $R_{1}=7.5 k\Omega$ and $R_{2}=10 k\Omega$.

```math
 A_{(V)}= \frac{U_{wy}} {U_{we}} = 1 + \frac{R_{2}} {R_{1}}
 ```
![Wzmacniacz_schemat](https://user-images.githubusercontent.com/92868145/213869889-53a78ee1-268e-41b4-b274-74e07cab1b7a.png)

# Code
What follows is defining the use of the I2C interface, setting the wiper to a minimum voltage value and defining the use of GPIO pin 17 as an output.  
```
    i2c = I2C(0)
    GPIO.setmode(GPIO.BCM)
    ds1841 = adafruit_ds1841.DS1841(i2c)
    ds1841.wiper=127
    RELAIS_1_GPIO = 17
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, 1)   
```
In the while loop, the lighting is turned on and the wiper is changed. The next step should be to run the PV panel test function. After that, the output is set low and the wiper value is set to 127. Break ends the loop.   
```
  while True:
        GPIO.output(RELAIS_1_GPIO, 0)
        sleep(0.2)
        ds1841.wiper=75
        sleep(0.2)
        ds1841.wiper=50
        sleep(0.2)
        ds1841.wiper=25
        sleep(0.2)
        ds1841.wiper=3
        #At this point, the function that examines the PV panel should be called.
        sleep(0.2)
        GPIO.output(RELAIS_1_GPIO, 1)
        ds1841.wiper=127
        break
```
The code that controls the lighting can be found in the file LedControl.py
 
