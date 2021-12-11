with open('input.txt') as f:
    boxes = f.readlines()

total_area = 0
for box in boxes:
    l, w, h = box.split('x')
    l, w, h = int(l), int(w), int(h)

    area = 2 * (l*w + w*h + h*l) + min([l*w, w*h, h*l])
    total_area += area

print(total_area)
