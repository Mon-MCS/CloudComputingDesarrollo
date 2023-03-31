salarioBase = float(input("Introduzca el salario base: "))
pagasExtras = float(input("Introduzca las pagas extras: "))
complementos = float(input("Introduzca los complementos: "))
otrosConceptosRetributibos = float(input("Introduzca los otros conceptos retributibos: "))
IRP = float(input("Introduzca el IRPF: "))
SeguridadSocial = float(input("Introduzca la Seguridad Social: "))

salarioBruto = salarioBase + pagasExtras + complementos + otrosConceptosRetributibos
salarioNeto = salarioBruto - (IRP +SeguridadSocial)

print(f"EL salario bruto es {salarioBruto} y el salario neto es {salarioNeto}")