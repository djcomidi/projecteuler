from EulerTools import is_prime

# max prime = 39999983 < MAXP
# number of primes below MAXP = 2433655
MAXP = 40 * 10 ** 6

print "initalizing totients"
totients = []
for n in xrange(MAXP + 1):
    totients.append(n)

print "computing connections"
total = 0
connections = [0, 0]
for n in xrange(2, MAXP):
    if is_prime(n):
        for k in xrange(n, MAXP, n):
            totients[k] = (totients[k] * (n - 1)) // n
    connections.append(1 + connections[totients[n]])
    # a chain of length 25 has 24 connections
    if is_prime(n) and 24 == connections[n]:
        total += n
print total
