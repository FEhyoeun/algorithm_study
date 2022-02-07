def solution(participant, completion):
    partHash = {}
    completHash = {}
    sum = 0
    for part in participant:
        partHash[hash(part)] = part
        sum += hash(part)

    for complet in completion:
        completHash[hash(complet)] = complet
        sum -= hash(complet)

    return partHash[sum]

