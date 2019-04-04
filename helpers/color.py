def hex2rgb(color):
    return tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2 ,4))

# Decimal number to HEX str
def dec2hex(n):
    n = int(n)
    if (n > 16):
        return str(hex(n).split('x')[-1])
    else:
        return "0" + str(hex(n).split('x')[-1])

# Gradient starting at color "start" to color "stop" with "steps" colors
# Not include start and stop colors to result
def gradient(start, stop, steps):
    out = []
    r = hex2rgb(start)[0]
    g = hex2rgb(start)[1]
    b = hex2rgb(start)[2]
    r_step = (hex2rgb(stop)[0] - r) / steps
    g_step = (hex2rgb(stop)[1] - g) / steps 
    b_step = (hex2rgb(stop)[2] - b) / steps 
    for i in range(steps):
        r = r + r_step
        g = g + g_step
        b = b + b_step
        out.append("#" + dec2hex(r) + dec2hex(g) + dec2hex(b))
    return out