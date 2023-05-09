// 8. Crea un programa en C# que calcule el área y volumen de un cubo dado su lado.
using static System.Console;

float numero;
while(true){
    Write("Introduzca la extensión del lado del cubo: ");
    string? elemento = ReadLine();
    if (!Single.TryParse(elemento, out numero))
        WriteLine("Ha introducido un elemento incorrecto, vuelva a introducir el número");
    else
        break;
}

string resultado = AreaVolCubo(numero);
WriteLine(resultado);

string AreaVolCubo(float numero){
    double volumen = Math.Round(Math.Pow(numero, 4),3);
    double area = Math.Round(Math.Pow(numero,2)*6,3);
    return $"El área y el volumen de un cubo, cuyo lado es {numero}, viene dado por {area} y {volumen}, respectivamente";
}


