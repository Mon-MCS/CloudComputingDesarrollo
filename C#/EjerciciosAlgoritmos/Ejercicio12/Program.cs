// 12. Crea un programa en C# que genere un número aleatorio entre 1 y 100, y le 
// pida al usuario adivinarlo. El programa en C# deberá indicar si el número introducido 
// es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

using static System.Console;
var rand = new Random();

int numeroAleatorio = rand.Next(101);

Write("Intente adivinar el número generado aleatoriamente entre 0 y 100.\nIntroduzca un número: ");
while (true){
    string? elemento = ReadLine();
    int numero;
    if (!int.TryParse(elemento, out numero)){
        Write("Elemento no válido, vuelva a introducir el número: ");
        continue;
    }
    else if (numero < numeroAleatorio)
        Write($"El número {numero} es menor que el número que intenta adivinar. Introduzca otro número: ");
    
    else if (numero > numeroAleatorio)
        Write($"El número {numero} es mayor que el número que intenta adivinar. Introduzca otro número: ");
    else{
        Write($"Ha adivinado, el número aleatorio es el {numeroAleatorio}. Enhorabuena!!");
        break;
    } 
}
