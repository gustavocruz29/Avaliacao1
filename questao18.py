def data(dd,mm,aa):
    if (dd>0)and(dd<31)and(mm>0)and(mm<13):
        if (mm==1):
            print(dd,'de janeiro de',aa)
        elif (mm==2):
            print(dd,'de fevereiro de',aa)
        elif (mm==3):
            print(dd,'de março de',aa)
        elif (mm==4):
            print(dd,'de abril de',aa)
        elif (mm==5):
            print(dd,'de maio de',aa)
        elif (mm==6):
            print(dd,'de junho de',aa)
        elif (mm==7):
            print(dd,'de julho de',aa)
        elif (mm==8):
            print(dd,'de agosto de',aa)
        elif (mm==9):
            print(dd,'de setembro de',aa)
        elif (mm==10):
            print(dd,'de outubro de',aa)
        elif (mm==11):
            print(dd,'de novembro de',aa)
        elif (mm==12):
            print(dd,'de dezembro de',aa)
    else:
        print('NULL')
