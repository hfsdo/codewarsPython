def rgb(r, g, b):
    return convert(r)+convert(g)+convert(b)


def convert(i):
    if i > 255:
        i=255 
    if i < 0:
        i=0
    return str(hex(int(i / 16))).replace("0x","").upper() + str(hex(int(i % 16))).replace("0x","").upper()