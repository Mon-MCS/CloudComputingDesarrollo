// 9. Dada una lista de números enteros, crea un programa en C# que calcule la suma de todos los números pares de la lista.
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


string resultado = Pares(ListaNumeros);
WriteLine(resultado);

string Pares(List<int> enteros){
    int suma = 0;
    string resultado;
    foreach ( int entero in enteros){
        if ( entero % 2 == 0)
            suma += entero;
    }
    return resultado = $"La suma de los enteros pares de la lista es {suma}";
}