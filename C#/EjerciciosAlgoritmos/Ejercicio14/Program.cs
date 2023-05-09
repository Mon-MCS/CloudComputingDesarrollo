// 14. Dada una lista de números enteros, crea un programa en C# que elimine los números duplicados de la lista.
using static System.Console;

List<int> ListaNumeros = new List<int>();
List<int> ListaNumerosSinDuplicados = new List<int>();
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
ListaNumerosSinDuplicados.Add(ListaNumeros[0]);
for (int i=0; i < ListaNumeros.Count; i++){
    bool noEstaEnLista = true;
    for (int j=0; j < ListaNumerosSinDuplicados.Count;j++){
        if (ListaNumeros[i] == ListaNumerosSinDuplicados[j]){
            noEstaEnLista = false;
            j = ListaNumerosSinDuplicados.Count-1;
        }
    }    
    if (noEstaEnLista == true)
        ListaNumerosSinDuplicados.Add(ListaNumeros[i]);
}
Write($"La lista sin duplicados de la lista [");
foreach ( int numero in ListaNumeros){
    Write(numero);
}
Write("] es [");
foreach ( int numero in ListaNumerosSinDuplicados){
    Write(numero);
}
Write("]");