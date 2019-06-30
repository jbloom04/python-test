

batteries=[1,3,7,5]
def light(batt1,batt2):
    # if batt1 % 2 == 0 and batt2 % 2 == 0:
    if batt1 in batteries and batt2 in batteries:
        return True
    else:
        return False


