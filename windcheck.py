# SL100 Preflight Wind check

import math
import sys

assert sys.version_info.major == 3, "Must be run in Python 3"

def psf_to_inhg(psf):
    """Convert lb/ft^2 to inches of mercury."""
    return psf * 0.014139030952735

def inhg_to_psf(inhg):
    """Convert inches of mercury to lb/ft^2."""
    return inhg * 70.72620488228

def pres_to_elev(inhg):
    """Given a pressure in inHg, determine the altitude (MSL) it normally
    occurs at (distance from 29.92)."""
    return inhg * 100

def elev_to_pres(elev):
    """Given an elevation in feet, determine the pressure level it normally
    occurs at."""
    return elev / 100

def determine_suitable_lda(displace_elev, margin):
    """Given a displacement elevation and safety marign, determine the
    minimum acceptable LDA settings."""
    return displace_elev * margin

def main():
    wind_speed = float(input("Enter wind speed in miles per hour: "))
    lda_alt = float(input("Enter launch detect altitude in feet: "))
    margin = float(input("Enter safety margin in percent: ")) / 100 + 1
    lda_alt *= margin
    wind_pres = wind_speed**2 * 0.00256      # lb/ft^2
    wind_pres = psf_to_inhg(wind_pres)       # inHg
    displace_elev = pres_to_elev(wind_pres)  # feet

    print("===========================================")
    print("Debug/verification information:")
    print("lda_alt: {} ft".format(lda_alt))
    print("wind_pres: {} inHg".format(wind_pres))
    print("displace_elev: {} ft".format(displace_elev))
    print("===========================================")
    print("Launch advice:")

    if displace_elev*margin > 300:
        print("Displacement elevation outside tolerable standards; abort launch")
    elif displace_elev > lda_alt:
        print("Displacement elevation greater than current lauch detection altitude;"
              " increase LDA to {} or greater".format(
              determine_suitable_lda(displace_elev, margin)))
    else:
        max_wind_pres = inhg_to_psf(elev_to_pres(lda_alt * margin))
        max_wind_speed = math.sqrt(max_wind_pres / 0.00256)
        max_wind_speed = math.floor(max_wind_speed)
        print("Launch conditions acceptable.  "
              "Maximum wind for given LDA is {} mph".format(max_wind_speed))

    print("===========================================")

if __name__ == '__main__':
    main()
