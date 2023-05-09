// 3.Crea un programa en C# que determine si un año es bisiesto o no.
using static System.Console;

int año;
while(true){
    Write("Introduzca un número: ");
    string? elemento = ReadLine();
    if (!int.TryParse(elemento, out año))
        WriteLine("Ha introducido un elemento incorrecto, vuelva a introducir el año");
    else
        break;
}

string resultado = Bisiesto(año);
WriteLine(resultado);
string Bisiesto( int año){
    string resultado;
    if (((año % 4 == 0) && (año % 100 != 0)) || (año % 400 == 0))
        return resultado = $"El año {año} es bisiesto";
    else 
        return resultado = $"El año {año} no es bisiesto";
}
