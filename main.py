def on_data_received():
    serial.redirect_to_usb()
serial.on_data_received(serial.delimiters(Delimiters.SPACE), on_data_received)

serial.set_baud_rate(BaudRate.BAUD_RATE9600)
serial.write_string("This is space. ")

def on_forever():
    pass
basic.forever(on_forever)
