import sys


try:
    superpower = input('Please input the heroes\' powers: ')
    superpower = list(filter(None, superpower.split(' ')))
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()

try:
    for i in range(len(superpower)):
        superpower[i] = int(superpower[i])
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()

try:
    nb_of_switches = int(input('Please input the number of power flips: '))
    if nb_of_switches < 0:
        raise ValueError
    if nb_of_switches > len(superpower):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()

print()

# Find the negative power and positive power in superpower[].
# Store negative and positive power in negative_pw[] and positive_pw[], respectively.
negative_pw = []
positive_pw = []
for i in range(len(superpower)):
    if superpower[i] < 0:
        negative_pw.append(superpower[i])
    else:
        positive_pw.append(superpower[i])
negative_pw = sorted(negative_pw)
positive_pw = sorted(positive_pw)

# A given hero's power can be switched an arbitrary number of times.
def get_max_power1(positive_pw, negative_pw, nb_of_switches):

    final_power = []
    max_power = 0

    # If nb_of_switches is less than the number of negative power, then
    # we switch the least nb_of_switches negative power.
    if nb_of_switches < len(negative_pw):
        for i in range(len(negative_pw)):
            if i < nb_of_switches:
                final_power.append(- negative_pw[i])
            else:
                final_power.append(negative_pw[i])
        final_power += positive_pw
        max_power = sum(final_power)

    # If nb_of_switches is greater than or equal to the number of negative
    # power, we firstly switch all the negative power. Then, if the number of
    # left switches is even, the sum of all current power is the maximal power.
    # If the number of left switch is odd, we switch the minimal power.
    else:
        for i in range(len(negative_pw)):
            final_power.append(- negative_pw[i])
        final_power += positive_pw
        final_power = sorted(final_power)
        left_switches = nb_of_switches - len(negative_pw)
        if left_switches % 2 == 1:
            final_power[0] *= -1
        max_power = sum(final_power)

    return max_power

# A given hero's power can be switched at most once.
def get_max_power2(positive_pw, negative_pw, nb_of_switches):

    final_power = []
    max_power = 0
    
    # If nb_of_switches is less than the number of negative power, then
    # we switch the least nb_of_switches negative power.
    if nb_of_switches < len(negative_pw):
        for i in range(len(negative_pw)):
            if i < nb_of_switches:
                final_power.append(- negative_pw[i])
            else:
                final_power.append(negative_pw[i])
        final_power += positive_pw
        max_power = sum(final_power)

    # If nb_of_switches is greater than or equal to the number of negative
    # power, we firstly switch all the negative power and than switch the
    # minimal positive power.
    else:
        for i in range(len(negative_pw)):
            final_power.append(- negative_pw[i])
        for i in range(nb_of_switches - len(negative_pw)):
            positive_pw[i] *= -1
        final_power += positive_pw
        max_power = sum(final_power)
      
    return max_power

# Flipping the power of nb_of_flips many consecutive heroes.
# Enumerate all the possibilities and find the greatest one.
def get_max_power3(superpower, nb_of_switches):

    max_power = 0
    find_max_power = []
    static_power = tuple(superpower)

    for i in range(len(superpower)):
        if i + nb_of_switches > len(superpower):
            break
        else:
            cur_power = list(static_power) 
            for j in range(i, i + nb_of_switches):
                cur_power[j] *= -1
            find_max_power.append(sum(cur_power))
    max_power = max(find_max_power)

    return max_power

# Flipping the power of arbitrarily many consecutive heroes
# Enumerate all the possibilities and find the greatest one.
def get_max_power4(superpower):

    find_max_power = [sum(superpower)]
    static_power = tuple(superpower)

    for i in range(len(superpower)):
        cur_power = list(static_power)
        for j in range(i, len(superpower)):
            cur_power[j] *= -1
            find_max_power.append(sum(cur_power))
    max_power = max(find_max_power)

    return max_power

max_power1 = get_max_power1(positive_pw, negative_pw, nb_of_switches)
max_power2 = get_max_power2(positive_pw, negative_pw, nb_of_switches)
max_power3 = get_max_power3(superpower, nb_of_switches)
max_power4 = get_max_power4(superpower)

print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {max_power1}.')
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {max_power2}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {max_power3}.')
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {max_power4}.')

