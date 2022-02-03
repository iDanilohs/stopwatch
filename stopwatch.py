def run():
    status = int(input(
        "Hola ¿Cómo estas? Presiona 1: para iniciar el cronometro. Presiona 2: Para detenerlo."))

    while status == 1:

        seconds = 0
        minutes = 0 
        hours = 0

        for seconds in range(62):
            print(f'{hours} : {minutes} : {seconds}')
            if seconds > 60:
                minutes += 1
                if minutes > 60



if __name__ == '__main__':
    run()