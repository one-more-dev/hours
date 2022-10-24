
import datetime as dt

calInicio = dt.date(2022,10,16)
calFim = dt.date(2023,12,31)

print("Welcome user!\n\nThis application goal is counting hours. Inserting a initial date, a ending date and hours\
(minutes) per day, the app will calculate the total time from one to the other.\n\nFollow the instructions to\
proper use it!")

print("Insert dates as YEAR,MONTH,DAY(2000,1,31, for example, and don't forget the commas'\n")

def inserindoData(question,inicial=None):
    while True:
        thisDate = input(question)
        a,b,c = map(int, thisDate.split(","))
        thisDate = dt.date(a,b,c)
        if inicial==None or thisDate > inicial:
            return thisDate
            break
        else:
            print("Please, do it again.")


def periodoDeContagem(*tx):
    dataInicial = inserindoData(tx[0])
    dataFinal = inserindoData(tx[1],dataInicial)
    return dataFinal-dataInicial, dataInicial


periodo = periodoDeContagem("Starting date: ","Ending date: ")
tempo = int(input("Time per day (in minutes): "))


def calculaDias(d=None):
    if(d == None):
        return periodo[0].days
    else:
        return periodo[0].days - d


print("\nNow, considering the weekdays as follow: Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4,\
Saturday = 5 and Sunday = 6.\nWould you like to exclude some weekday(s) or period from your counting?\n\n")

def excluirDias():
    print("Empty insertings will be the same as not excluding dates\n")
    excluirS = input("Exclude some week from the counting (if more than one, use commas): ")
    if excluirS != "":
        diasTotais = 0
        excluirS = excluirS.split(",")
        p = periodo[1]
        for dias in range(periodo[0].days):
            p += dt.timedelta(days=1)
            if (str(p.weekday()) in excluirS):
                diasTotais += 1
        return diasTotais
    else:
        return 0
        


def excluirPeriodo():
    print("If you wish to exclude a full period, press Y/y to continue.")
    prosseguir = input("")
    if(prosseguir == 'Y' or prosseguir == 'y'):
        excluirP = periodoDeContagem("Insert it's start: ","And it's end: ")
        return excluirP[0].days
    else:
        return 0


e1 = excluirDias()
e2 = excluirPeriodo()
p = periodo[0].days

horasTotais = (p-(e1+e2))*(tempo/60)
print(f"\nThe total amount of hours is {horasTotais}")

#   ERROR TREATMENT
#   CHANGING SPECIFIC DAY TIMES
#   DOCUMENT GENERATOR
#   GRAPHIC INTERFACE














