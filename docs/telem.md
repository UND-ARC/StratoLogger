# Telemetry interfacing notes

<div style="text-align:center">
    <!-- sorry about this if you're reading this file as text or offline... -->
    <img src="https://github.com/und-arc/StratoLogger/raw/master/docs/pinout.png"/>
</div>


| Pin # | Function           |
| ----- | ------------------ |
| 1     | No connect         |
| 2     | +3.3V (don't use!) |
| 3     | RX (unused)        |
| 4     | TX                 |
| 5     | Ground             |

| Serial port setting | Value     |
| ------------------- | --------- |
| Baud rate           | 9,600BPS  |
| Data width          | 8 bits    |
| Parity              | None      |
| Stop bits           | 1         |

## Output Formatting

Output data format is ASCII text based with a `<CR><LF>` character as line endings.

### OnPad telemetry

With the SL telemetry set on `OnPad`, the first value is the approximate gorund elevation and all subsequent data is AGL altitude:

```
800<CRLF>  # Best guess MSL altitude
0<CRLF>    # start of AGL altitude
0<CRLF>
0<CRLF>
5<CRLF>
25<CRLF>
56<CRLF>
```

### OnLaunch telemetry

With the SL telemetry set on `OnLaunch`, all data is AGL altitude:
```
198<CRLF>    # AGL altitude
248<CRLF>
300<CRLF>
349<CRLF>
```


