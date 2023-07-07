# follow a sequence of instructions to move across a grid

with open('day1_input') as f:
    my_text = f.read()

my_list = my_text.split(", ")

current_position = (0, 0)
current_direction = 0
position_history = [(0, 0)]
position_overlaps = []
history_set = set(position_history)

def turn_left():
    global current_direction
    current_direction = (current_direction - 1) % 4


def turn_right():
    global current_direction
    current_direction = (current_direction + 1) % 4


def get_direction_name():
    if current_direction == 0:
        return "north"
    elif current_direction == 1:
        return "east"
    elif current_direction == 2:
        return "south"
    elif current_direction == 3:
        return "west"

a = 0

for item in my_list:
    item = item.replace(" ", "")
    part_one = item[0]
    part_two = int(item[1:])

    if part_one == "R":
        turn_right()
    else:
        turn_left()

    while part_two > 0:
        if current_direction == 0:
            current_position = (current_position[0], current_position[1] + 1)
        elif current_direction == 1:
            current_position = (current_position[0] + 1, current_position[1])
        elif current_direction == 2:
            current_position = (current_position[0], current_position[1] - 1)
        elif current_direction == 3:
            current_position = (current_position[0] - 1, current_position[1])

        position_history.append(current_position)

        b = len(set(position_history))

        if a == b:
            position_overlaps.append(current_position)

        a = b

        part_two = part_two - 1

print(position_history)
#print(len(set(position_history)))
print("Answer 1: ", abs(sum(position_history[-1])))
print(position_overlaps)
print("Answer 2: ", abs(sum(position_overlaps[0])))

