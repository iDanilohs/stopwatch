from time import sleep


def show(hours, minutes, seconds):
    print(f'{hours}h : {minutes}m : {seconds}s')


def run():
    status = int(input(
        "Hola ¿Cómo estas? Presiona 1: para iniciar el cronometro. Presiona 2: Para detenerlo."))

    seconds = 0
    minutes = 0 
    hours = 0

    while status == 1 or hours <= 60:
        seconds += 1
        show(hours, minutes, seconds)
        sleep(1)

        if seconds == 60:
            minutes += 1
            seconds = 0
            show(hours, minutes, seconds)
            sleep(1)
        elif minutes == 60:
            hours += 1
            minutes = 0
            show(hours, minutes, seconds)
            sleep(1)
        elif hours == 60:
            print("60 horas es el maximo de tiempo")
            break
        

if __name__ == '__main__':
    run()