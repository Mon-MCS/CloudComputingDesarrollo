// 2.Dado un número entero, crea un programa en C# que determine si es par o impar.
using static System.Console;

int numero;
while(true){
    Write("Introduzca un número: ");
    string? elemento = ReadLine();
    if (!int.TryParse(elemento, out numero))
        WriteLine("Ha introducido un elemento incorrecto, vuelva a introducir el número");
    else
        break;
}

if (numero % 2 == 0)
    WriteLine($"El número {numero} es par");
else
    WriteLine($"El número {numero} es impar");
