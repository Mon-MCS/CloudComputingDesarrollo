// 4.Crea un programa en C# que determine si una cadena de texto es un palíndromo o no.
using static System.Console;
///using System.Text;
//using System.Text.RegularExpressions;
using System;

string? cadena;
while(true){
    Write("Introduzca una cadena de texto: ");
    cadena = ReadLine();
    string prueba = System.Text.RegularExpressions.Regex.Replace(cadena, @"\s+", String.Empty);
    if (prueba.Length ==0)
        WriteLine("Ha escrito una cadena vacía.");
    else
        break;
}


string resultado = Capicua(cadena);
WriteLine(resultado);

string Capicua(string cadena){
    string? cadenaCopia = cadena;
    cadenaCopia = System.Text.RegularExpressions.Regex.Replace(cadenaCopia.Normalize(System.Text.NormalizationForm.FormD), @"[^a-zA-z0-9 ]+", "");
    cadenaCopia = System.Text.RegularExpressions.Regex.Replace(cadenaCopia, @"\s+", String.Empty);
    cadenaCopia = cadenaCopia.ToLower();

    string cadenaInversa = "";

    for (int i=cadenaCopia.Length-1; i >= 0; i--){
        cadenaInversa += cadenaCopia[i];
    }
    string resultado;
    if (cadenaCopia == cadenaInversa)
        return resultado = $"La cadena {cadena} es palíndromo";
    else
        return resultado = $"La cadena {cadena} no es palíndromo";
}




    