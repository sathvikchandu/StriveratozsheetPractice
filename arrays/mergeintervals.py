interval = [[1,3],[2,6],[8,10],[15,18]]
interval.sort()   # sort intervals first

i = 0
j = 1
n = len(interval)
res = []

while i < n:
    start = interval[i][0]
    end = interval[i][1]

    # merge with all intervals that overlap
    while j < n and interval[j][0] <= end:
        end = max(end, interval[j][1])
        j += 1

    res.append([start, end])

    # move i to where j stopped
    i = j
    j = i + 1

print(res)
    