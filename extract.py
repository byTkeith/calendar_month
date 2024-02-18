# programme to extract from raw data
# NYVTEN001
# 10 April 2022
import math
def location(block):
    return "Cape Town" if block else ""


def temperature(block):
    temp = block.split(" ")[1].split("_")[0]
    return float(temp)


def x_coordinate(block):
    x_coord = block.split(" ")[1].split(":")[1].split(",")[0]
    return x_coord
    
    
def y_coordinate(block):
    y_coord = block.split(" ")[1].split(":")[1].split(",")[1]
    return y_coord


def pressure(block):
    pres = block.split(" ")[1].split("_")[1].split(":")[0]
    return float(pres)


def get_block(data):
    START_INDEX = data.index("BEGIN")
    END_INDEX = data.index("END")+3
    return data[START_INDEX:END_INDEX]