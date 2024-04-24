# RC Car - LEGO Powered by Raspberry Pi CM4 with SaraKIT

Welcome to the official GitHub repository for the "RC Car - LEGO Powered by Raspberry Pi CM4 with SaraKIT" project, featured on [Hackster.io](https://www.hackster.io/sarakit/rc-car-lego-powered-by-raspberry-pi-cm4-with-sarakit-dfc9ac). This project transforms a standard LEGO car into a remotely controlled vehicle using the power of Raspberry Pi CM4 and the versatility of SaraKIT, now with Python and an Xbox One controller for a more intuitive control experience.

![RCCar_shot2](https://github.com/SaraEye/SaraKIT-RCCar-Raspberry-Pi/assets/35704910/4dfd76ce-c000-4830-b9ab-237eaca09b63)
![RCCar_shot5](https://github.com/SaraEye/SaraKIT-RCCar-Raspberry-Pi/assets/35704910/dc234c7c-eb11-41fd-9563-134011135746)

## Overview

This RC Car project demonstrates the integration of SaraKIT with a Raspberry Pi Compute Module 4 to control a LEGO-based vehicle using Python. It highlights the potential of combining traditional toys with modern technology and the practical application of Python in hardware control.

## Features

- **Remote Control via Xbox One Controller**: Control the direction and speed of the LEGO car using an Xbox One controller connected via Bluetooth.
- **Live Camera Feed**: Stream live video from one or two cameras mounted on the car, providing a first-person view (FPV) driving experience.
- **Customizable Speed and Steering**: Detailed control over the car's speed and direction.
- **Cross-Platform Compatibility**: Control software written in Python, running on Raspberry Pi OS.

## Getting Started

### Prerequisites

- Raspberry Pi CM4
- SaraKIT expansion board
- LEGO car setup or similar vehicle platform
- One or two compatible cameras (optional for FPV)
- Xbox One controller with Bluetooth capability
- Basic understanding of Python and Raspberry Pi environment
- Two gimbal motors

### Installation

1. **Set Up Your Raspberry Pi**: Ensure your Raspberry Pi CM4 is set up with the latest Raspberry Pi OS and connected to the same WiFi network as your controller device. Install necessary Python packages and configure the Xbox One controller as described [here](https://github.com/SaraEye/Xbox-Pad-Control-for-Raspberry-Pi-Projects).

2. **Connect the SaraKIT**: Attach the SaraKIT to your Raspberry Pi CM4 as per the instructions provided with the kit.

3. **Assemble Your RC Car**: Build your LEGO car or similar vehicle and integrate the motors and optional cameras with the SaraKIT and Raspberry Pi.

4. **Download the Control Script**: Clone this repository to your Raspberry Pi and navigate to the project directory.

```bash
git clone https://github.com/SaraEye/SaraKIT-RCCar-Raspberry-Pi rccar
cd rccar
```

5. **Run the Python Control Script**: Execute the Python script to start controlling your RC car.

```bash
python rccar.py
```

## Example Code

The repository includes a Python script `rccar.py` that demonstrates basic control logic for steering and speed management using the Xbox One controller.

## Contributing

Contributions are welcome! Whether improving the control logic, adding new features, or creating tutorials, please fork this repository and submit your pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

For more detailed instructions, troubleshooting, and other projects, please visit the [Hackster.io project page](https://www.hackster.io/sarakit/rc-car-lego-powered-by-raspberry-pi-cm4-with-sarakit-dfc9ac) and our homepage: https://sarakit.saraai.com/

Happy building!
