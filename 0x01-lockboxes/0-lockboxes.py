#!/usr/bin/python3

""" solutions of task """


def canUnlockAll(boxes):

    if(type(boxes)) is not list:
        return False
    elif(len(boxes)) == 0:
        return False

    for n in range(1, len(boxes) - 1):
        boxes_check = False

        for indx in range(len(boxes)):
            boxes_check = n in boxes[indx] and n != indx
            if boxes_check:
                break
        if boxes_check is False:
            return boxes_check
    return True
