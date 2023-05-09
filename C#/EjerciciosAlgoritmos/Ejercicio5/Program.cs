// 5.Dada una lista de nombres, crea un programa en C# que ordene la lista alfabéticamente.
using static System.Console;

List<string> ListaNombres = new List<string>();

while(true) {
    Write("Entre el nombre, si desea finalizar escriba FIN: ");
    string? elemento = ReadLine();
    if (elemento == "FIN")
    break;
    else {
        ListaNombres.Add(elemento);
    }
}

ListaNombres.Sort();
Write("La lista ordenada alfabéticamente es: ");
foreach ( string nombre in ListaNombres)
    Write($"{nombre} ");
