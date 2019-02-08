# StratoLogger SL100 PreFlight Checklist

This checklist is meant specifically and exclusively for UND-ARC's November
launch of the Stripe rocket using a dual-SL100 altimeter configuration.

## Altimeter Bay Construction

- [ ] Connect battery ground wire to SL100.
- [ ] Connect switch and power wire to SL100.
- [ ] Run [the pre-construction voltage test checklist](#pre-construction-voltage-test).
- [ ] Connect main chute fire command wire to SL100.
- [ ] Connect drogue chute fire command wire to SL100.
- [ ] Connect battery power wire to SL100.
- [ ] Mount altimeter board in altimeter bay.

## Pre-construction Voltage Test

- [ ] Connect battery power wire to the SL100.
- [ ] Establish connection from PC to SL100 using the DT4U and pigtail cable.
- [ ] Launch the DataCap software.
- [ ] Launch the voltage test interface (**Altimeter** -> **Test**).
- [ ] Ensure no loose connections cause a voltage drop.
- [ ] Ensure stable voltage in acceptable range of 4V to 16V.
- [ ] Disconnect battery power wire from the SL100.

## Powerup Sequence

- [ ] Switch altimeter on.
- [ ] Listen for beep codes and expected value:

| Order | Digits | Meaning              | Expected value #1 | Expected value #2 |
| ----- | ------ | -------------------- | ----------------- | ----------------- |
| 1.    | 1      | Selected preset      | 4                 | 4                 |
| 2.    | [3,4]  | Main deploy altitude | 1000              | 950               |
| 2A.   | Cont. tone | Apogee delay != 0 | No tone sounds   | Tone sounds       |
| 3.    | [3,6]  | Ap. alt last flight  | 4078              | 4080              |
| 4.    | [2,3]  | Battery voltage level | In range [4,16]  | In range [4,16]   |

- [ ] Ensure altimeter is outputting continuity status (3 beeps every 0.8sec)

### Diagnostics

| Beeps/0.8sec | Meaning                             |
| ------------ | ----------------------------------- |
| None         | No continuity on any ematchs        |
| 1            | Drogue chute ematch continuity good |
| 2            | Main chute ematch continuity good   |
| 3            | Both ematch continuity good         |
