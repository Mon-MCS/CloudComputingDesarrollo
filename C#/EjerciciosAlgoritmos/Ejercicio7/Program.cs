// 7.Dado un número entero, crea un programa en C# que determine si es primo o no.
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

string resultado = Primo(numero);
WriteLine(resultado);

string Primo(int numero){
    bool primo = true;
    int posibleDivisor = numero - 1;
    while (posibleDivisor >= 2){
        if (numero % posibleDivisor == 0){
            primo = false;
            break;
        }
        else 
            posibleDivisor -= 1;
    }
    if (primo == true)
        return $"El número {numero} es primo";
    else
        return $"El número {numero} no es primo, pues {posibleDivisor} es un divisor del mismo";
}
