# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

# check equality of two float value
def epsilon_equal(n, m, epsilon=0.00001):
    return (n - epsilon) < m and (n + epsilon > m)
