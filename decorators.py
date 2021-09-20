from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Han pasado " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    n = 1000000
    for i in range(1,n):
        pass
    return print("\n"+ str(n) + " ciclos completados")

@execution_time
def suma (a: int,b: int) -> float:
    return print("\nla suma es : " + str((a + b)))

@execution_time
def saludo(nombre=str) -> str:
    print("\nHola :" + nombre)

random_func()
suma(2,2)
saludo(" Juanelo")


