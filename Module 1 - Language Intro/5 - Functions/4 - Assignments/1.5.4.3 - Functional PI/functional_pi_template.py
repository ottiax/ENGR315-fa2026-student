import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    # Initial values for the Gauss-Legendre algorithm
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 1.0 / 4.0
    p = 1.0

    # Start with an estimate that is guaranteed to be outside the target
    # and continue until the desired accuracy is reached
    pi_estimate = 0
    error = float("inf")

    while error >= target_error:
        # Save old value of a
        old_a = a

        # Update the variables
        a = (a + b) / 2
        b = math.sqrt(old_a * b)
        t = t - p * (old_a - a) ** 2
        p = 2 * p

        # Calculate current estimate of pi
        pi_estimate = ((a + b) ** 2) / (4 * t)

        # Calculate error
        error = abs(math.pi - pi_estimate)

    return pi_estimate
    # change this so an actual value is returned
    return 0




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
