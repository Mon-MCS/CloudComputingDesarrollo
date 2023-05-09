// 1. Crear un progrma en C#, que dada una lista de números enteros, 
// determina cuál es el mayor y cuál es el menor.

using static System.Console;

void MayorMenor(){

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

    ListaNumeros.Sort();
    WriteLine($"El menor elemento de la lista es {ListaNumeros[0]}");
    WriteLine($"El mayor elemento de la lista es {ListaNumeros[ListaNumeros.Count -1]}");
}

MayorMenor();