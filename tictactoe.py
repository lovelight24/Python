def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = "--- "
    ve = "|   "
    ho = ho * kamal
    ve = ve * (kamal+1)
    while i < kamal+1:
        print(ho)
        if not (i == kamal):
            print(ve)
        i += 1


board_size = int(input("What size of game board? "))
drawboard(board_size)

if i<b:




