def get_fwd_node(i, node):
    s = node[i]
    node_list = list(node)
    if s == '9':
        add = '0'
    else:
        add = str(int(s) + 1)
    node_list[i] = add
    return "".join(node_list)


def get_bck_node(i, node):
    s = node[i]
    node_list = list(node)
    if s == '0':
        add = '9'
    else:
        add = str(int(s) - 1)
    node_list[i] = add
    return "".join(node_list)


def openLock(deadends, target: str) -> int:
    if "0000" in deadends:
        return -1
    frontier = ["0000"]
    visited = set(deadends)
    visited.add("0000")
    count = 0
    while frontier:
        if target in frontier:
            return count
        f = []
        for node in frontier:
            visited.add(node)
            for i in range(4):
                fwd_node = get_fwd_node(i, node)
                if fwd_node not in deadends and fwd_node not in visited:
                    f.append(fwd_node)
                back_node = get_bck_node(i, node)
                if back_node not in deadends and back_node not in visited:
                    f.append(back_node)
        frontier.extend(f)
        frontier = list(set(frontier) - set(visited))
        count += 1
    return -1


print(openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
