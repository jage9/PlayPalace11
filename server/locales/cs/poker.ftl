# Sdílené pokerové zprávy

poker-fold = Zahodit
poker-call = Dorovnat
poker-check = Checkovat
poker-raise = Přihodit
poker-all-in = All in
poker-enter-raise = Zadejte výši přihození

poker-check-pot = Zkontrolovat pot
poker-check-bet = Částka k dorovnání
poker-check-min-raise = Minimální přihození
poker-check-log = Historie akcí
poker-check-hand-players = Hráči v rozdání
poker-check-turn-timer = Časovač tahu
poker-check-blind-timer = Časovač blindů
poker-check-button = Kdo má button
poker-check-dealer = Kdo je dealer
poker-check-position = Vaše pozice

poker-read-hand = Přečíst ruku
poker-read-table = Přečíst karty na stole
poker-hand-value = Hodnota ruky
poker-read-card = Přečíst kartu { $index }
poker-dealt-cards = Bylo vám rozdáno { $cards }.
poker-flop = Flop: { $cards }.
poker-turn = Turn: { $card }.
poker-river = River: { $card }.

poker-pot-total = { $amount } žetonů v potu.
poker-pot-main = Hlavní pot: { $amount } žetonů.
poker-pot-side = Boční pot { $index }: { $amount } žetonů.
poker-to-call = Potřebujete { $amount } žetonů k dorovnání.
poker-min-raise = { $amount } žetonů minimální přihození.

poker-player-folds = { $player } zahazuje.
poker-player-checks = { $player } checkuje.
poker-player-calls = { $player } dorovnává { $amount } žetonů.
poker-player-raises = { $player } přihazuje { $amount } žetonů.
poker-player-all-in = { $player } jde all in za { $amount } žetonů.

poker-player-wins-pot = { $player } vyhrává { $amount } žetonů.
poker-player-wins-pot-hand = { $player } vyhrává { $amount } žetonů s { $cards } za { $hand }.
poker-player-wins-side-pot-hand = { $player } vyhrává boční pot { $index } s { $amount } žetony s { $cards } za { $hand }.
poker-players-split-pot = { $players } si dělí { $amount } žetonů s { $hand }.
poker-players-split-side-pot = { $players } si dělí boční pot { $index } s { $amount } žetony s { $hand }.
poker-player-all-in = { $player } jde all in za { $amount } žetonů.
poker-player-wins-game = { $player } vyhrává hru.

poker-showdown = Showdown.

poker-timer-disabled = Časovač tahu je vypnut.
poker-timer-remaining = Zbývá { $seconds } sekund.
poker-blind-timer-disabled = Časovač blindů je vypnut.
poker-blind-timer-remaining = { $seconds } sekund do zvýšení blindů.
poker-blind-timer-remaining-ms = { $minutes } { $minutes ->
    [one] minuta
    [few] minuty
    [many] minuty
   *[other] minut
} { $seconds } sekund do zvýšení blindů.
poker-blinds-raise-next-hand = Blindy se zvýší v příštím rozdání.

poker-button-is = Button má { $player }.
poker-dealer-is = Dealer je { $player }.
poker-position-seat = Jste { $position } místo za buttonem.
poker-position-seats = Jste { $position } { $position ->
    [one] místo
    [few] místa
    [many] místa
   *[other] míst
} za buttonem.
poker-position-button = Jste na buttonu.
poker-position-dealer = Jste dealer.
poker-position-dealer-seat = Jste { $position } místo za dealerem.
poker-position-dealer-seats = Jste { $position } { $position ->
    [one] místo
    [few] místa
    [many] místa
   *[other] míst
} za dealerem.
poker-show-hand = { $player } ukazuje { $cards } za { $hand }.
poker-blinds-players = Malý blind: { $sb }. Velký blind: { $bb }.
poker-reveal-only-showdown = Karty můžete ukázat jen na konci rozdání.

poker-reveal-both = Ukázat obě hole cards
poker-reveal-first = Ukázat první hole card
poker-reveal-second = Ukázat druhou hole card

poker-raise-cap-reached = Limit přihození byl dosažen pro toto kolo.
poker-raise-too-small = { $amount } žetonů minimální přihození.
poker-hand-players-none = Žádní hráči v rozdání.
poker-hand-players-one = { $count } hráč: { $names }.
poker-hand-players = { $count } { $count ->
    [one] hráč
    [few] hráči
    [many] hráče
   *[other] hráčů
}: { $names }.
poker-raise-too-large = Nemůžete přihodit víc než máte žetonů.

poker-log-empty = Žádné akce zatím.
poker-log-fold = { $player } zahodil
poker-log-check = { $player } checkoval
poker-log-call = { $player } dorovnal { $amount }
poker-log-raise = { $player } přihodil { $amount }
poker-log-all-in = { $player } šel all in za { $amount }

poker-table-cards = Karty na stole: { $cards }.
poker-your-hand = Vaše ruka: { $cards }.

# Popisky voleb časovače
poker-timer-5 = 5 sekund
poker-timer-10 = 10 sekund
poker-timer-15 = 15 sekund
poker-timer-20 = 20 sekund
poker-timer-30 = 30 sekund
poker-timer-45 = 45 sekund
poker-timer-60 = 60 sekund
poker-timer-90 = 90 sekund
poker-timer-unlimited = Neomezeno

poker-blind-timer-unlimited = Neomezeno
poker-blind-timer-5 = 5 minut
poker-blind-timer-10 = 10 minut
poker-blind-timer-15 = 15 minut
poker-blind-timer-20 = 20 minut
poker-blind-timer-30 = 30 minut

poker-raise-no-limit = Bez limitu
poker-raise-pot-limit = Pot limit
poker-raise-double-pot = Dvojitý pot limit
