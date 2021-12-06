with open('input.txt') as f:
    boxes = f.readlines()

total_ribbon = 0
for box in boxes:
    l, w, h = box.split('x')
    l, w, h = int(l), int(w), int(h)

    x, y = sorted([l, w, h])[:2]
    ribbon = 2 * (x + y) + (l * w * h)
    total_ribbon += ribbon

print(total_ribbon)
