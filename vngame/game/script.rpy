init:
    $layout.ARE_YOU_SURE = "Czy na pewno?"
    $layout.DELETE_SAVE = "Czy na pewno chcesz usunąć ten stan gry?"
    $layout.OVERWRITE_SAVE = "Czy na penwo chcesz nadpisać ten stan gry?"
    $layout.LOADING = "Ładowanie spowoduje utracenie obecnego stanu gry, czy na pewno załadować?"
    $layout.QUIT = "Czy na pewno chcesz wyjść?"
    $layout.MAIN_MENU = "Czy na pewno chcesz powrócić do głównego menu? Spowoduje to utracenie obecnego stanu gry."
   
define nel = Character('Nel', color="#c8ffc8")

image bg test1 = "graphics/scene_001_test.png"
image nel normal = "graphics/person_001_test.png"

# The game starts here.
label start:

    nel "Załadujmy tło!"
    show bg test1

    nel "Teraz załadujmy mnie!"
    show nel normal

    nel "IT WERKS (ale nie do końca jak widać) - sie poprawi."
    return

