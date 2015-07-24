# x^2-y^2-z^2=n
# (y+k)^2-y^2-(y-k)^2=n
# (y^2+2yk+k^2)-y^2-(y^2-2yk+k^2)=n
# 4yk-y^2=n => y(4k-y)=n
# { y > 0
# { 4k-y > 0 => 4k > y } => y//4 < k < y
# { y-k > 0 => y > k   }

LIMIT = 50 * 10 ** 6
ways = [0] * LIMIT
for y in xrange(1, LIMIT):
    for k in xrange(y // 4 + 1, y):
        n = y * (4 * k - y)
        if n >= LIMIT:
            break
        if n > 0:
            ways[n] += 1
print ways.count(1)
