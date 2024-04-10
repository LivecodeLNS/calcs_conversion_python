# Conversor de notación de cálculos

## ÍNDICE
- [Descripción](#descripción)
- [Finalidad](#finalidad)
- [Cómo Instalar](#cómo-instalar)
- [Cómo Usar](#cómo-usar)
- [Errores Conocidos](#errores-conocidos)
- [Solicitud de Implementación](#solicitud-de-implementación)
- [Contacto](#contacto)

## Descripción:
Una aplicación CLI para convertir notaciones de cálculo entre prefijos, infijos y postfijos/sufijos.

###### [(Volver al índice)](#índice)
## Finalidad
El propósito o finalidad de este repositorio es mostrar mi forma de codificar y organizar/redactar documentación.

La intención es que cuente como un proyecto de portafolio.

###### [(Volver al índice)](#índice)
## Cómo Instalar
Actualmente para instalarlo, sigue estos pasos.
> REQUERIDO:
> - Git o GitHub CLI
> - Python 3.7+

1. Clonar el repositorio.
```sh
$> git clone https://github.com/livecodelns/calcs_conversion_python.git 
```
2. Entrar al directorio.
```sh
$> cd calcs_conversion_python 
```
3. Ejecutar [(Ver Cómo usar)](#cómo-usar)

###### [(Volver al índice)](#índice)
## Cómo Usar
Actualmente sólo se puede ejecutar por medio de python 3.7+.

> Necesitamos:
> - El cálculo o expresión inicial
> - La notación que deseamos obtener

Usamos el flag `--initial-calculation` (Abreviado: `-ic`) para especificar el cálculo y el flag `--target-notation` (Abreviado: `-tn`) para especificar la notación que deseamos obtener de regreso.

> Valores admitidos para *-tn*:

    1 (PREFIX)
    2 (INFIX)
    3 (POSTFIX/SUFFIX)

> Ejemplos:
```sh
$> py main.py -ic '((3*4)+5^6-7)/8' -tn 1
```
```sh
$> py main.py -ic '((2^3)/4+5-6)*7' -tn 3
```

###### [(Volver al índice)](#índice)
## Errores Conocidos
Aún se encuentra en desarrollo la conversion de las notaciones, si se intenta, causa error.
- Prefijo => Infija
- Prefijo => Postfija
- Postfija => Infija
- Postfija => Prefijo

###### [(Volver al índice)](#índice)
## Solicitud de Implementación
Ante cualquier solicitud se pueden realizar `Issues`.

###### [(Volver al índice)](#índice)
## Contacto
Puedes contactarte conmigo para enviar comentarios, donaciones, propuestas de proyectos, ideas, clases personalizadas, etc.

*NOTA*: En caso de donaciones, por favor consultar con antelación para orientar y facilitar el proceso.

Todo es bienvenido y suma, lo agradezco.

* WhatsApp: +54 9 11 3845 3811
* Mail: _livecodelns@gmail.com_
* YouTube: [Canal de *_YouTube_*](https://YouTube.com/@livecodelns)
* Twitch: [Canal de *_Twitch_*](https://Twitch.tv/LiveCodeLNS)
* Instagram: [Perfil de *_Instagram_*](https://www.instagram.com/livecodelns)

###### [(Volver al índice)](#índice)