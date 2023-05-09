// 11. Crea un programa en C# que determine si un número es capicúa o no.
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

string resultado = Capicua(numero);
WriteLine(resultado);

string Capicua(int numero){
    string numeroString = numero.ToString();
    string capicua = "";
        for (int i=numeroString.Length-1; i >= 0; i--){
        capicua += numeroString[i];
    }
    string resultado;
    if (capicua == numeroString)
        return resultado = $"El número {numeroString} es capicúa";
    else
        return resultado = $"El número {numeroString} no es capicúa";

}
