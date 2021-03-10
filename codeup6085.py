w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

print('%.2f'%((w*h*b)*(2**-23)), 'MB')