[Back to main page](https://und-arc.github.io/StratoLogger/index.html)

# Interfacing StratoLogger SL100 with a PC

***THIS INTERFACE METHOD IS SUITABLE FOR TESTING THE ALTIMETER ONLY.
THIS METHOD IS NOT SUITABLE FOR CONNECTING THE ALTIMETER TO THE ROCKET.***

Parts needed:
- [StratoLogger SL100][sl100]
- [Pigtail data adapter cable][pigtail]
- [PerfectFlite DT4U adapter board][dt4u]
- Micro-USB to USB-A cable
- PC running [data transfer software][software]
- 9V battery
- [Battery connection cable][batterycable]

Steps to interfacing:
1. Short the "SWITCH" connection on the SL100.
2. Connect the microUSB cable to the DT4U and the PC.
3. Connect the DT4U pigtail cable to the data port on the altimeter and the
   pins on the DT4U.
4. Open the software on the PC.
5. Connect the battery to the screw terminals on the SL100.
6. Immediately select **Data** -> **Acquire**.  This must be done before the
   altimeter completes the powerup sequence.

[sl100]: http://perfectflite.com/sl100.html
[pigtail]: http://perfectflite.com/cabpg.html
[dt4u]: http://perfectflite.com/dt4u.html
[software]: http://perfectflite.com/Download.html
[batterycable]: http://perfectflite.com/CAB9V.html
