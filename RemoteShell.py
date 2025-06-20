import paramiko

hostname = 'honeypot ip address'
port = 22
username = 'honeypot username'
password = 'honeypot password'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname, port, username, password)
    print(f"Successfully connected to {hostname}:{port}")
    command = 'uname -a'
    stdin, stdout, stderr = client.exec_command(command)
    print(f"Executing command: {command}")
    for line in stdout:
        print(f"  {line.strip()}")
    error = stderr.read().decode()
    if error:
        print(f"Error: {error}")
except paramiko.AuthenticationException:
    print("Authentication failed.")
except paramiko.SSHException as e:
    print(f"Could not establish SSH connection: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
    print("SSH connection closed.")
