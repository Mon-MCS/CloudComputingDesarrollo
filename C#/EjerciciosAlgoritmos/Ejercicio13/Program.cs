// 13. Crea un programa en C# que determine si una cadena de texto es un anagrama de otra cadena de texto.
using static System.Console;

string? cadena;
string? anagrama;
Write("Introduzca una cadena: ");
cadena = ReadLine();
Write("Introduzca el anagrama de la cadena: ");
anagrama = ReadLine();

string resultado = Anagrama(cadena,anagrama);
WriteLine(resultado);

string Anagrama(string cadena, string anagrama){
    char[] letrasCadena = cadena.ToLower().ToCharArray();
    Array.Sort(letrasCadena);
    char[] letrasAnagrama = anagrama.ToLower().ToCharArray();
    Array.Sort(letrasAnagrama);
    if (letrasCadena == letrasAnagrama)
        return $"{anagrama} es un anagrama de {cadena}";
    else
        return $"{anagrama} no es un anagrama de {cadena}";
}

