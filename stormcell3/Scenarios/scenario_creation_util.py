from math import cos, sin

from node import Node


def apply_to_locs(fun, tupes):
    return [fun(tup) for tup in tupes]


def apply_to_conns(fun, conns):
    return [(fun(tup1), fun(tup2)) for tup1, tup2 in conns]


def mult_locs(tupes, scalar): return apply_to_locs(lambda tup: mult(tup, scalar), tupes)
def mult_conns(conns, scalar): return apply_to_conns(lambda conn: mult(conn, scalar), conns)
def mult(tup, scalar):
    tupx, tupy = tup
    return tupx * scalar, tupy * scalar

def xshift_locs(tupes, val): return apply_to_locs(lambda tup: xshift(tup, val), tupes)
def xshift_conns(conns, val): return apply_to_conns(lambda conn: xshift(conn, val), conns)
def xshift(tup, val):
    tupx, tupy = tup
    return (tupx + val, tupy)

def yshift_locs(tupes, val): return apply_to_locs(lambda tup: yshift(tup, val), tupes)
def yshift_conns(conns, val): return apply_to_conns(lambda conn: yshift(conn, val), conns)
def yshift(tup, val):
    tupx, tupy = tup
    return (tupx, tupy + val)

def x_mirror_locs(tupes, max_x_i): return apply_to_locs(lambda tup: x_mirror(tup, max_x_i), tupes)
def x_mirror_conns(conns, max_x_i): return apply_to_conns(lambda conn: x_mirror(conn, max_x_i), conns)
def x_mirror(tup, max_x_i):
    tupx, tupy = tup
    return (max_x_i - tupx, tupy)

def y_mirror_locs(tupes, max_y_i): return apply_to_locs(lambda tup: y_mirror(tup, max_y_i), tupes)
def y_mirror_conns(conns, max_y_i): return apply_to_conns(lambda conn: y_mirror(conn, max_y_i), conns)
def y_mirror(tup, max_y_i):
    tupx, tupy = tup
    return (tupx, max_y_i - tupy)

def rotate_conns(loc_center, conns, rad): return apply_to_conns(lambda conn: rotate(loc_center,conn,rad), conns)
def rotate_locs(loc_center, tupes, rad): return apply_to_locs(lambda tup: rotate(loc_center,tup, rad), tupes)
def rotate(loc_center, loc, in_rad):
    rad = -in_rad
    x, y = loc
    x_c, y_c = loc_center
    x_rot = (x-x_c)*cos(rad)-(y-y_c)*sin(rad) + x_c
    y_rot = (x-x_c)*sin(rad)+(y-y_c)*cos(rad) + y_c
    return x_rot, y_rot



def nodify(tupes):
    return [Node(tup) for tup in tupes]


def connectify(nodes, conns):
    loc_node_map = {node.location : node for node in nodes}
    for conn in conns:
        loc1, loc2 = conn
        node1 = loc_node_map.get(loc1, None)
        node2 = loc_node_map.get(loc2, None)
        if node1 is None:
            print(f"{loc1} not found in node map")
        elif node2 is None:
            print(f"{loc2} not found in node map")
        else:
            node1.connect(node2)

def uniq(vals):
    return list(set(vals))