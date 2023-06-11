# Create a 2D matrix that acts as a workspace where a robot can move, ( eg: 1-> free space, 0-> obstacle). Create a function to insert obstacles at required/given coordinates. Write functions that can move the robot's(represent robot with other characters or numbers) position in the workspace. Write a function to visually represent the workspace, including the robot to the user on every move or change.

import numpy as np


def insert_obstacle(matrix, x, y, robot_x, robot_y):
    if x == robot_x and y == robot_y:
        print("Can't insert obstacle at the same position")
        return matrix

    matrix[x][y] = 1
    return matrix


# Check if there are obstacle and move, left, right, top ,bottom
# if obstacle is there then print warning and dont move
def move_robot(matrix, x, y, direction):
    ox = x
    oy = y

    if direction == "w":
        x -= 1
    elif direction == "s":
        x += 1
    elif direction == "a":
        y -= 1
    elif direction == "d":
        y += 1
    else:
        print("invalid command\n")
        return ox, oy

    # check out of bound
    if x < 0 or x > 9 or y < 0 or y > 9:
        print("Out of bound\n")
        return ox, oy

    if matrix[x][y] == 1:
        print("There is an obstacle at", x, y, "\n")
        return ox, oy

    return x, y


# print the matrix and obstacle and robot
def print_matrix(matrix, x, y):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == x and j == y:
                print("*", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    # create 10 * 10 matix
    matrix = np.zeros((10, 10), dtype=np.int8)
    robot_x, robot_y = 0, 0
    print_matrix(matrix, robot_x, robot_y)

    # take user input
    while True:
        print("\n\n* is robot\n1. Add obstacle")
        print("2. Move robot(a,s,d,f)")
        print("3. Quit")
        option = input("Enter your option: ")
        if option == "1":
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            matrix = insert_obstacle(matrix, x, y, robot_x, robot_y)
            print_matrix(matrix, robot_x, robot_y)
        elif option == "2":
            while True:
                direction = input("Enter direction: ")
                if direction == "q":
                    break
                robot_x, robot_y = move_robot(matrix, robot_x, robot_y, direction)
                print_matrix(matrix, robot_x, robot_y)
        elif option == "3":
            break
