def dist_sum(positions, expansion=2):
    total = 0
    open_dist = 0
    current = positions[0]
    count = 1

    dists = []

    for n in positions[1:]:
        if n > current:
            dist_to_prev = (n - current - 1) * expansion + 1
            open_dist += count * dist_to_prev
        dists.append(open_dist)
        total += open_dist
        count += 1
        current = n

    print(dists, sum(dists))

    return total

if __name__ == '__main__':
    pos = [1,3,6,6,9,10]
    print(dist_sum(pos, 2))
