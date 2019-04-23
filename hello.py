import smbus, time, socket, sys

host = '0.0.0.0'
port = 1500
socksize = 1024
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',port))
s.listen(1)
while True:
    try:
        conn, adds = s.accept()
        data = conn.recv(socksize)
        
        bus = smbus.SMBus(1)
##set register for bus
        addr = 0x40
        
##pick servo

        if data == b'1':
    ##first servo run
            bus.write_byte_data(addr,0,0x20)
            time.sleep(.25)
            bus.write_byte_data(addr,0x06,0)

            time.sleep(.25)
##bus.write_byte_data(addr,0xfe, 0x1e)
            bus.write_byte_data(addr,0, 0x20)
    ##bus.write_word_data(addr,0x08,1250)

            time.sleep(2)
            bus.write_word_data(addr,0x08,1600)
            time.sleep(2)
            bus.write_word_data(addr, 0x08, 1664)

        elif data == b'killsrv':
            conn.close()
            sys.exit()
        else:
            bus.write_byte_data(addr,0,0x20)
            time.sleep(.25)

            bus.write_byte_data(addr,0x0A,0)

            time.sleep(.25)
##bus.write_byte_data(addr,0xfe, 0x1e)
            bus.write_byte_data(addr,0, 0x20)
    ##bus.write_word_data(addr,0x0C,1250)

            time.sleep(2)
            bus.write_word_data(addr,0x0C,500)
            time.sleep(2)
            bus.write_word_data(addr, 0x0C, 2000)
    except socket.timeout:print("")
