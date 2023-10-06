def main():
    t = float(input("Temperature: "))
    v = float(input("Velocity: "))
    wind_chill = 35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)
    print("Wind Chill Temperature", f"{wind_chill:0,.2f}")

if __name__ == "__main__":
    main()