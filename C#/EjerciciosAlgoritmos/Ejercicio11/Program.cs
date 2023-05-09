// 11. Dada una lista de números enteros, crea un programa en C# que calcule la media de la lista.

using static System.Console;

List<int> ListaNumeros = new List<int>();

while(true) {
    Write("Entre el numero, si desea finalizar escriba FIN: ");
    string? elemento = ReadLine();
    int numero;
    if (elemento == "FIN")
    break;
    else if (!int.TryParse(elemento, out numero)){
        WriteLine("Elemento no válido, vuelva a introducir el número");
        continue;
    }
    else {
        ListaNumeros.Add(numero);
    }
}

string resultado = Media(ListaNumeros);
WriteLine(resultado);

string Media(List<int> ListaEnteros){
    int suma = 0;
    string resultado;
    foreach ( int entero in ListaEnteros)
        suma += entero;
    decimal media = (decimal) suma / (ListaEnteros.Count);
    
    return resultado = $"La media de la lista de enteros es {Math.Round(media,2)}";
}