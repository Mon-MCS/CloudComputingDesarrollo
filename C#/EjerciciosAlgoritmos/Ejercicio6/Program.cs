// 6. Crea un programa en C# que calcule el factorial de un número entero.
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

string resultado = Factorial(numero);
WriteLine(resultado);
string Factorial(int numero){
    int factorial = 1;
    for (int i=numero; i>=1; i--){
        factorial *= i;
    }
    return $"El factorial de {numero} es {factorial}";
}
