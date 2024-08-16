import os

def modify_httpd_conf(httpd_conf_path, output_path, server_name, document_root, listen_port=80):
    """
    Modify the httpd.conf file based on the system settings provided.
    
    :param httpd_conf_path: Path to the input httpd.conf file
    :param output_path: Path to save the modified httpd.conf file
    :param server_name: The ServerName directive value
    :param document_root: The DocumentRoot directive value
    :param listen_port: The port number to listen on (default is 80)
    """
    with open(httpd_conf_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip().startswith('ServerName'):
            line = f"ServerName {server_name}\n"
        elif line.strip().startswith('DocumentRoot'):
            line = f"DocumentRoot \"{document_root}\"\n"
        elif line.strip().startswith('Listen'):
            line = f"Listen {listen_port}\n"
        modified_lines.append(line)

    with open(output_path, 'w') as file:
        file.writelines(modified_lines)

    print(f"Modified httpd.conf saved at: {output_path}")

def main():
    httpd_conf_path = input("Enter the path to your httpd.conf file: ")
    output_path = input("Enter the path to save the modified httpd.conf file: ")
    server_name = input("Enter the ServerName: ")
    document_root = input("Enter the DocumentRoot path: ")
    listen_port = input("Enter the Listen port (default is 80): ")

    # Use default port 80 if no port is specified
    if not listen_port.isdigit():
        listen_port = 80
    else:
        listen_port = int(listen_port)

    # Check if the input file exists
    if not os.path.exists(httpd_conf_path):
        print("The specified httpd.conf file does not exist.")
        return

    # Modify the httpd.conf file
    modify_httpd_conf(httpd_conf_path, output_path, server_name, document_root, listen_port)

if __name__ == "__main__":
    main()
