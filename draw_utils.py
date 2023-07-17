def rotate_str(rot_deg:int, rot_x:int=0, rot_y:int=0) -> str:
    return f"rotate({rot_deg},{rot_x},{rot_y})"

def transl_str(move_x: int, move_y: int) -> str:
    return f"translate({move_x},{move_y})"