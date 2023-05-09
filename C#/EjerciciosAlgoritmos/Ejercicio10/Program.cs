// 10. Crea un programa en C# que determine si un número es positivo, negativo o cero.

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

string resultado = TipoNumero(numero);
WriteLine(resultado);

string TipoNumero (int numero){
    string resultado;
    if (numero > 0)
        return resultado = $"El número {numero} es positivo";
    else if (numero < 0)
        return resultado = $"El número {numero} es negativo";
    else 
        return resultado = $"El número {numero} es cero";
}