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

    # Define the command based on the OS and interface name
    command = 'ipconfig' if platform.system() == 'Windows' else 'ip addr'
    if interface_name:
        command += f' | findstr /R /C:"{interface_name}"' if platform.system() == 'Windows' else f' show {interface_name}'

    # Execute the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    output = output.decode().strip()

    # Process the output based on the presence of the interface name
    if interface_name:
        if output and 'cannot find' not in output.lower():
            network_info[interface_name] = output
        else:
            return jsonify(error='Interface not found'), 404
    else:
        network_info = {'interfaces': output}

    return jsonify(network_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
