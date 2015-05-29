from random import randint
def simulate_prizedoor(nsim):
    #compute here
    answer = []
    for i in range(0,nsim):
        answer.append(randint(0,2))
    return answer


def simulate_guess(nsim):
    guess = []
    for i in range(0,nsim):
        guess.append(randint(0,2))
    return guess

def goat_door(prizedoors, guesses):
    answer = []
    all_answers = [0,1,2]
    for p_g in zip(prizedoors,guesses):
        lpg = list(p_g)
        ans = list(set(all_answers) - set(lpg))
        if len(ans)>1:
            answer.append(ans[randint(0,1)])
        else:
            answer.append(ans[0])
    return answer

def switch_guess(guesses, goatdoors):
    answer = []
    all_answers = [0,1,2]
    for g_g in zip(guesses,goatdoors):
        lgg = list(g_g)
        ans = list(set(all_answers) - set(lgg))
        if len(ans)>1:
            answer.append(ans[random.randint(0,1)])
        else:
            answer.append(ans[0])
    return answer


def win_percentage(guesses, prizedoors):
    total = len(prizedoors)
    count = 0
    for i in range(0,total):
        if guesses[i] == prizedoors[i]:
            count += 1
    return round(float(count)/float(total) *100,3)

guesses = simulate_guess(10000)
prizedoors = simulate_prizedoor(10000)
goatdoors = goat_door(prizedoors, guesses)
switched_guesses = switch_guess(guesses,goatdoors)


print 'win percentage for keeping your guess is', win_percentage(guesses,prizedoors)
print 'win percentage for switching your guess is', win_percentage(switched_guesses,prizedoors)