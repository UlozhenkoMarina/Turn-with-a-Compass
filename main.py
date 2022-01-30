#in this solution dictionary is used, because complexity of its operations is O(1)
def direction(facing, turn):
    try:
        direction = {0: 'N', 45: 'NE', 90: 'E', 135: 'SE', 180: 'S', 225: 'SW', 270: 'W', 315: 'NW'}
        res = (dict(map(reversed, direction.items())).get(facing) + turn)%360
        return direction.get(res)
    except:
        print('''Error occurs: turn is not multile of 45, mistake in dictionary 
        definition(for example not unique values causes error while dictionary reversing) 
        or smth else''')
