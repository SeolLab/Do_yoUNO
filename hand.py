class Hand:
    def __init__(self, screen, deck):
        self.screen = screen
        self.deck = deck
        self.cards = []
        for _ in range(5):
            card = self.deck.pop()
            if card:
                self.cards.append(card)

    def count(self):
        return len(self.cards)

    def is_empty(self):
        return len(self.cards) == 0
    
