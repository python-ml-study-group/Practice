def append_if_exists(grps, num_to_check, num_to_append):
    for i in range(len(grps)):
        if num_to_check in grps[i]:
            grps[i].append(num_to_append)
            return True
    return False

def make_groups(connections):
    grps = []
    for connx in connections:
        if not append_if_exists(grps, connx[0], connx[1]):
            if not append_if_exists (grps, connx[1], connx[0]):
                grps.append([connx[0], connx[1]])
    return grps

connections = {(7,1), (10,2), (3, 4), (2,9), (11, 7), (13,11)}
grps = make_groups (connections)

print (max([len(items) for items in grps]))


