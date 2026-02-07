# Light Turret - České zprávy hry

# Název hry
game-name-lightturret = Světelná věž

# Úvod
lightturret-intro = Light Turret začala! Každý hráč má věž s { $power } silou. Střílej do věže pro získání světla a mincí, ale pokud tvé světlo překročí tvou sílu, jsi vyřazen! Kupuj vylepšení za mince pro zvýšení své síly. Hráč s nejvíce světlem na konci vyhrává!

# Akce
lightturret-shoot = Střelit do věže
lightturret-upgrade = Koupit vylepšení (10 mincí)
lightturret-check-stats = Zkontrolovat statistiky

# Výsledky akcí
lightturret-shoot-result = { $player } střílí do věže a získává { $gain } světla! Věž má teď { $light } světla.
lightturret-coins-gained = { $player } získává { $coins } { $coins ->
    [one] minci
    [few] mince
    [many] mince
   *[other] mincí
}! { $player } má nyní { $total } { $total ->
    [one] minci
    [few] mince
    [many] mince
   *[other] mincí
}.
lightturret-buys-upgrade = { $player } kupuje vylepšení síly!
lightturret-power-gained = { $player } získává { $gain } síly! { $player } má nyní { $power } síly.
lightturret-upgrade-accident = Vylepšení bylo náhodně prolnuto s věží! Věž má nyní { $light } světla.
lightturret-not-enough-coins = Nemáte dost mincí! Potřebujete { $need } { $need ->
    [one] minci
    [few] mince
    [many] mince
   *[other] mincí
}, ale máte jen { $have }.

# Vyřazení
lightturret-eliminated = Světlo je příliš silné pro duši hráče { $player }! { $player } je vyřazen!

# Statistiky
lightturret-stats-alive = { $player }: { $power } síly, { $light } světla, { $coins } mincí.
lightturret-stats-eliminated = { $player }: vyřazen s { $light } světlem.

# Konec hry
lightturret-game-over = Konec hry!
lightturret-final-alive = { $player } skončil se { $light } světlem.
lightturret-final-eliminated = { $player } byl vyřazen se { $light } světlem.
lightturret-winner = { $player } vyhrává s { $light } světlem!
lightturret-tie = Remíza na { $light } světle!

# Možnosti
lightturret-set-starting-power = Počáteční síla: { $power }
lightturret-enter-starting-power = Zadejte počáteční sílu:
lightturret-option-changed-power = Počáteční síla nastavena na { $power }.
lightturret-set-max-rounds = Maximum kol: { $rounds }
lightturret-enter-max-rounds = Zadejte maximum kol:
lightturret-option-changed-rounds = Maximum kol nastaveno na { $rounds }.

# Důvody zakázaných akcí
lightturret-you-are-eliminated = Byli jste vyřazeni.
