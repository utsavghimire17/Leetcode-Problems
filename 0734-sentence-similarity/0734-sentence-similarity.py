class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairs = {}
        for pair in similarPairs:
            if pair[0] not in pairs:
                pairs[pair[0]] = [pair[1]]
            else:
                pairs[pair[0]].append(pair[1])
            if pair[1] not in pairs:
                pairs[pair[1]] = [pair[0]]
            else:
                pairs[pair[1]].append(pair[0])
        for i in range(len(sentence1)):
            if sentence1[i] not in pairs or sentence2[i] not in pairs:
                if sentence1[i] != sentence2[i]:
                    return False
            else:
                if sentence1[i] != sentence2[i]:
                    if sentence1[i] not in pairs[sentence2[i]]:
                        return False
        return True