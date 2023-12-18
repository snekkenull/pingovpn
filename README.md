# pingovpn

This Python script converts domain names in OpenVPN configuration files to IP addresses. It's useful when you want to avoid DNS resolution issues or improve connection speed.

## Usage

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine:
   ```
   git clone https://github.com/snekkenull/pingovpn.git
   ```

3. Navigate to the cloned repository:
   ```
   cd pingovpn
   ```

4. Run the script with the OpenVPN configuration file as an argument:
   ```
   python run.py filename.ovpn
   ```
   Replace `filename.ovpn` with the actual path to your OpenVPN configuration file.

The script will create a new file with 'modified_' prepended to the original filename. This new file will have the same content as the original file, but with the domain names replaced by their corresponding IP addresses.

## Note

- The script checks for duplicate IP addresses and only adds an IP address to the new file if it has not been used before.
- If the script cannot resolve a domain, it leaves the domain as is in the new file.
- Remember to run this script with a user that has the necessary permissions to read the input file and write the output file.

