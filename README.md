# MAC Changer

## Developed by Avinash Mandal

## Description

MAC Changer is a command-line tool designed to change the hardware (MAC) address of network interfaces on your computer. It provides a simple and convenient way to modify the MAC address, allowing you to enhance your privacy, bypass certain network restrictions, and perform other network-related tasks.

## Features

- Change the MAC address of network interfaces
- View the current MAC address of network interfaces
- Restore the original MAC address of network interfaces
- Cross-platform compatibility (Linux)

## Installation

### Prerequisites

- Python 3.11

### Instructions

1. Clone the repository:

```bash
git clone https://github.com/avinashmandal-in/MacAddChanger.git
```

2. Change to the project directory:

```bash
cd MacAddChanger
```

## Usage

To change the MAC address of a network interface, open a terminal or command prompt and navigate to the project directory. Then, run the following command:

```bash
python mac_changer.py -i <interface> -m <new_mac_address>
```

Replace `<interface>` with the name of the network interface you want to modify (e.g., eth0, wlan0). Replace `<new_mac_address>` with the desired MAC address (e.g., 00:11:22:33:44:55).

Additional options:

- `-i` or `--interface'
- `-m` or `--new_mac'
- `-h` or `--help`

**Note:** Changing the MAC address of a network interface may temporarily disrupt your network connection. Exercise caution when using this tool.

## Examples

- Change the MAC address of the Wi-Fi interface to a specific address:

```bash
python mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## Acknowledgments

- The MAC Changer project is inspired by the need for network privacy and customization.
- Thanks to the open-source community for providing valuable resources and libraries.

## Contact

For any questions or inquiries, feel free to contact the project maintainer at (code.abhinash@gmail.com) [](mailto:code.abhinash@gmail.com).
