def ascension():

    learn = 0
    work = 1
    level = 0

    promotion = input(str("My level %s is ok? YES/NOT.: " % level))
    promotion = promotion.upper()

    if promotion != "YES":
        while promotion != "YES":
            while promotion == "NOT":
                learn += 1
                work *= 2
                level += learn + work
                promotion = input(str("My level %s is ok? YES/NOT" % level))
                promotion = promotion.upper()
                if promotion == "YES":
                    print("Objetivo alcançado!")
                    break
            else:
                print("Resposta inválida. Digite novamente.")
                promotion = input(str("My level %s is ok? YES/NOT" % level))
                promotion = promotion.upper()
    else:
        print("Objetivo alcançado!")
ascension()
