## Router AP Automation

This project automates the configuration of a Router Access Point (AP) using a browser. It allows users to log in to the router, change the SSID, password, channel, bandwidth, and other settings based on user input. The project uses `pytest` for testing.

## Project Structure

Router_AP_Automation/ 
├── base_driver/ 
│ ├── base_driver.py  
│ └── credentials.json 
├── pages_ap/ 
│ ├── ap_config.py 
│ └── login.py 
└── tests/ 
│ ├── conftest.py
│ └── test_browser.py



## Getting Started

### Prerequisites

- Python 3.x
- `pytest`
- `selenium`
- WebDriver for your browser (e.g., ChromeDriver for Chrome)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rrakshithaa/router-ap-automation.git
    cd router-ap-automation
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your router credentials to `base_driver/credentials.json`:
    ```json
    {
        "router_ip": "http://IP_LINK/",
        "username": "username",
        "password": "password"
    }
    ```

## Usage

1. Run the tests using `pytest`:
    ```bash
    pytest
    ```

2. The script will log in to the router and perform the configurations based on the user input.

## Project Modules

- **base_driver/base_driver.py**: Contains the base driver setup and utility functions.
- **pages_ap/ap_config.py**: Contains functions to configure the AP settings.
- **pages_ap/login.py**: Contains functions to log in to the router.
- **tests/conftest.py**: Contains fixture setup for `pytest`.
- **tests/test_browser.py**: Contains test cases for the browser automation.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

- Thanks to the contributors and the open-source community.
