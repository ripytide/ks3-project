from sketch.sketch import Window
win = Window(400, 400)
for i in range(6):
    win.circle([[100, 250, 100], [255, 255, 255], [0, 0, 0], [50, 50, 200], [200, 50, 50], [240, 240, 50]][i], [200, 200], 200 - 40 * (i - 1) if i > 0 else 300)
win.display()