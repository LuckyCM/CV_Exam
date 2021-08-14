

# a) bilinear interpolation
# At Pixel 33:
Red = R33
Green = (G23+G34+G32+G43) / 4
Blue = (B22+B24+B42+B44) / 4
# At Pixel 34:
Red = (R33+R35) / 2
Green = G34
Blue = (B24+B44) / 2
# At Pixel 43:
Red = (R33+R53) / 2
Green = G43
Blue = (B42+B44) / 2
# At Pixel 44:
Red = (R33+R35+R53+R55) / 4
Green = (G34+G43+G45+G54) / 4
Blue = B44

# b) smooth hue transition interpolation
# Interpolation of green pixels as above, call these values G33, G34, G43, and G44.
# At Pixel 33:
Red = R33
Blue = G33 * (B22 / G22 + B24 / G24 + B42 / G42 + B44 / G44)/4
# At Pixel 34:
Red = G34 * (R33 / G33 + R35 / G35)/2
Blue = G34 * (B24 / G24 + B44 / G44)/2
# At Pixel 43:
Red = G43 * (R33 / G33 + R53 / G53)/2
Blue = G43 * (B42 / G42 + B44 / G44)/2
# At Pixel 44:
Red = G44 * (R33 / G33 + R35 / G35 + R53 / G53 + R55 / G55)/4
Blue = B44

# c) edge-directed interpolation
# At Pixel 33:
∆H = ||G32-G34|| ∆V = ||G23-G43||
Green = (G32+G34)/2 if ∆H < ∆V
Green = (G23+G43)/2 if ∆H > ∆V
Green = (G32+G34+G23+G43)/4 if ∆H = ∆V
# At Pixel 34:
Green = G34
# At Pixel 43:
Green = G43
# At Pixel 44:
∆H = ||G43-G45|| ∆V = ||G34-G54||
Green = (G43+G45)/2 if ∆H < ∆V
Green = (G34+G54)/2 if ∆H > ∆V
Green = (G43+G45+G34+G54)/4 if ∆H = ∆V
# Interpolation of Red and Blue pixels as in (b)