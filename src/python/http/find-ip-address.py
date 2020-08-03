import socket


print("******************************************")
hostname = socket.gethostname()
print("Your computer name is: {}".format(hostname))

IPAddress = socket.gethostbyname(hostname)
print("Your computer ip address is: ".format(IPAddress))
print("******************************************")



