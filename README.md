# Carbon Black Sensor Management

## Process Notes
- Get a list of graduated seniors from Ethan or the Registrar
- Create a text file of all graduated usernames
- Create a text file of all graduated asset tags
- Run both of these files through device_info.py

### Issues
- There will be discrepencies:
    - Some usernames will show up on desktops, these can be removed from the list.
    - Some usernames will show up on multiple assets
    - Some assets will return different usernames. These assets have most likely been reprovisioned.

- Check the following:
    - Remedyforce CMDB to determine if the asset has been turned in or reprovisioned.
    - Userquery to verify if the username in question has actually graduated.
    - The original list to ensure the asset or username has in fact graduated.

- All discrepencies should be handled manually:
    - Once the devices that need to be removed are identified:
        - Uninstall the sensor
        - Delete from the console

- Once manual actions have been performed re-run the original files through device_info.py.


