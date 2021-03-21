#!/usr/bin/env python3
import math
import collections

def half(length):
    return math.sqrt(2 - math.sqrt(4-length*length))

def double(length):
    return math.sqrt(length*length*(4-length*length))

def sum_(table, alpha, beta):
    sup_alpha = math.sqrt(4-table[alpha]**2)
    sup_beta = math.sqrt(4-table[beta]**2)
    return (table[alpha] * sup_beta + table[beta] * sup_alpha)/2

def sub_(table, alpha, beta):
    sup_alpha = math.sqrt(4-(table[alpha]**2))
    sup_beta = math.sqrt(4-(table[beta]**2))
    return (table[alpha] * sup_beta - table[beta] * sup_alpha)/2

def triple(table, theta):
    return 3*table[theta] - table[theta]**3

def onethird(table, theta):
    delta = (table[theta]**2)/4 + math.pow(((-3)/3.0), 3)
    print(theta/3.0, theta, delta);
    """
    a = math.sqrt((table[theta]**2)/4 + a0)
    b = -(table[theta]/2)
    print(b+a)
    print(b-a)
    print(math.pow(-3, 1.0/3.0))
    print("hello")
    c = math.pow(b+a, 1.0/3.0)
    d = math.pow(b-a, 1.0/3.0)
    print(d)
    return c+d
    """

def get36():
    return 0.5*(math.sqrt(5)-1)

def build_chord_table():
    chord_table = collections.OrderedDict()
    crd36 = get36()
    Q = collections.deque([(0.0, 0.0), (60.0, 1.0), (180.0, 2.0), (36.0, crd36), (0.5, .00872)])
    #Q = collections.deque([(0.0, 0.0), (60.0, 1.0), (180.0, 2.0)])

    while (Q):
        (theta, chord) = Q.popleft()
        chord_table[theta] = chord
        h = theta / 2.0
        if (h >= 0.5 and h % 0.5 == 0 and h not in chord_table):
            Q.append((h, half(chord)))
        d = theta * 2
        if (d < 180.0 and d not in chord_table):
            Q.append((d, double(chord)))

        for k, v in chord_table.items():
            s = theta + k
            #if s < 180.0 and s not in chord_table:
            #    Q.append((s, sum_(chord_table, theta, k)))
            s = theta - k
            if s > 0.0 and s not in chord_table:
                Q.append((s, sub_(chord_table, theta, k)))
            s = k - theta
            if s > 0.0 and s not in chord_table:
                Q.append((s, sub_(chord_table, k, theta)))
            s = 3 * theta
            if s < 180.0 and s not in chord_table:
                Q.append((s, triple(chord_table, theta)))
            """
            h = theta/3.0
            if (h % 0.5 == 0):
                if (h > 0.5 and h not in chord_table):
                    onethird(chord_table, theta)
                    Q.append((h, onethird(chord_table, theta)))
            """

    return chord_table

def print_chord_table(table):
    i = 0
    for k, v in sorted(table.items()):
        if i % 4 == 0:
            print("")
        sin = 2 * math.sin(math.radians(k/2))
        R = round(v, 6) == round(sin, 6)
        if R == False:
            print("False: ", k, round(v, 6), round(sin, 6))
        #print("{}, {}, {} {} | ".format(k, round(v, 6), round(sin, 6), R), end="")
        print("{}, {}, ".format(k, round(v, 6)), end="")
        i += 1
    print("\ntotal: {}".format(i))

def main():
    chords = build_chord_table()
    print_chord_table(chords)

if __name__ == "__main__":
    main()
