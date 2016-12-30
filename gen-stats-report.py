#!/usr/bin/env python3

MAX_NUM_NEEDED_FREECELLS = 5


def collect_stats():
    stats = [0] * (MAX_NUM_NEEDED_FREECELLS + 1)
    with open('msfc32k-min-fc', 'r') as f:
        for l in f:
            stats[int(l.split()[1])] += 1
    return stats


def print_stats(stats):
    total = sum(stats)
    if total != 32000:
        raise "total is wrong"

    def percent(i):
        return float(i)/total*100
    running = 0
    for i, s in enumerate(stats):
        running += s
        print(("%4d %10d %10d %20.3f%% %20.3f%%") %
              (i, s, running, percent(s), percent(running)))


stats = collect_stats()
print_stats(stats)
