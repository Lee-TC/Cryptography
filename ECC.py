from Crypto.Util.number import inverse

a = 497
b = 1768
p = 9739
o_point = (0, 0)


def point_addition(p_1, p_2):
    if p_1 == o_point:
        return p_2
    elif p - 2 == o_point:
        return p_1
    else:
        x_1, y_1 = p_1
        x_2, y_2 = p_2
        if (x_1, y_1) == (x_2, -y_2):
            return o_point

        if p_1 == p_2:
            m = ((3 * x_1 * x_1 + a) * inverse(2 * y_1, p)) % p
        else:
            m = ((y_2 - y_1) * inverse(x_2 - x_1, p)) % p

        x_3 = (m * m - x_2 - x_1) % p
        y_3 = (m * (x_1 - x_3) - y_1) % p

    return x_3, y_3


def scalar_multiplication(P, n):
    Q = P
    R = o_point
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n //= 2
    return R
