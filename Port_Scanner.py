import socket
import sys

def Scan_Ports(host):
    for _ in xrange(2**16):
        try:
            result = 1
            connection = socket.socket()
            connection.settimeout(0.01)
            result = connection.connect_ex((host, _))
            connection.close()
            try:
                service_name = socket.getservbyport(_ , "tcp")
            except:
                service_name = "Not Found"

            finally:
                if result == 0:
                    print "Port %d is Open with service %s" % (_ , service_name)
        except socket.error as msg:
            print msg
            sys.exit(1)



def main():
    host = raw_input("Enter Host: ")
    try:
        host_ip = socket.gethostbyname(host)
    except:
        print "Couldn't Locate the Host, Please Check Internet Connection and the Host name"
        sys.exit(1)

    print "Scanning Port of the IP ", host_ip
    Scan_Ports(host)

if __name__ == "__main__":
    main()