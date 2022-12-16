def on_forever():
    min2 = 500
    # Minimum interval v milisekundách
    max2 = 5000
    # Maximum interval v milisekundách 
    # Vygeneruj náhodný interval
    interval = Math.random() * (max2 - min2) + min2
    # Pískni tón na Microbitu po dobu intervalu
    music.play_tone(Note.C, music.beat(BeatFraction.WHOLE))
    # Spusť stopky a začni počítat čas
    start = control.millis()
    # Počkej, dokud uživatel nedrží stisknuté tlačítko
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        pass
    # Nic nedělej, dokud není stisknuté tlačítko
    # Zastav stopky a zjisti, kolik času uplynulo
    end = control.millis()
    elapsed = end - start
    # Porovnej skutečný interval s ideálním intervale
    diff = abs(interval - elapsed)
    # Vypiš výsledek na Microbit
    if diff < 100:
        basic.show_string("Gratuluju")
    elif diff < 101:
        basic.show_string("Skoro")
basic.forever(on_forever)
