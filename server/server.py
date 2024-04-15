from flask import Flask, jsonify, request
import platform
import subprocess

app = Flask(__name__)


# For testing purposes, in order to see current interfaces (on Windows)
# def get_network_interfaces():
#     command = 'ipconfig /all'
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, _ = process.communicate()
#     return output.decode()
#
#
# # Call the function and print the results
# interfaces = get_network_interfaces()
# print(interfaces)


@app.route('/network', methods=['GET'])
# Function to get network information
# Returns the IP address of the specified interface
def get_network_info():
    interface_name = request.args.get('interface', '')
    network_info = {}
    if interface_name:
        # Check the operating system
        if platform.system() == 'Windows':
            # Use 'ipconfig' and 'findstr' to get the interface details
            command = f'ipconfig | findstr /R /C:"{interface_name}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            ip_address, _ = process.communicate()
            ip_address = ip_address.decode().strip()
        else:
            # Use 'ip addr show' for Unix-like systems
            command = f'ip addr show {interface_name}'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            ip_address, _ = process.communicate()
            ip_address = ip_address.decode().strip()

        if ip_address and 'cannot find' not in ip_address.lower():
            network_info[interface_name] = ip_address
        else:
            return jsonify(error='Interface not found'), 404
    else:
        # Get all interfaces
        if platform.system() == 'Windows':
            command = 'ipconfig'
        else:
            command = 'ip addr'
        # Use 'subprocess' to run the command and get the output
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        interfaces, _ = process.communicate()
        interfaces = interfaces.decode().strip()
        network_info = {'interfaces': interfaces}
        # Return the interfaces as JSON
    return jsonify(network_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
