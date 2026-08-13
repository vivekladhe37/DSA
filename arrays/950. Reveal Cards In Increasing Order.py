class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        pq = deque()

        for i in range(len(deck)):
            if not pq:
                pq.append(deck[i])
                continue

            bottom = pq.pop()
            pq.appendleft(bottom)
            pq.appendleft(deck[i])

        return list(pq)
        