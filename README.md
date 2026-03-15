# Sistema Básico de Gestión de Garaje

## Descripción
Este proyecto corresponde a la tarea de la **Semana 13** de la materia de **Programación Orientada a Objetos**.  
La aplicación fue desarrollada en **Python** utilizando **Tkinter** para la interfaz gráfica.

El sistema permite registrar vehículos dentro de un garaje, mostrando la información ingresada en una lista dentro de la ventana principal.

## Funcionalidades
- Registrar vehículos en el sistema.
- Ingresar los datos de:
  - Placa
  - Marca
  - Propietario
- Visualizar los vehículos registrados en una lista.
- Limpiar los campos del formulario.
- Validar campos vacíos.
- Evitar registrar placas repetidas.

## Estructura del proyecto
El proyecto está organizado de acuerdo con la arquitectura solicitada en la tarea:

```text
garaje_app/
├── main.py
├── modelos/
│   ├── __init__.py
│   └── vehiculo.py
├── servicios/
│   ├── __init__.py
│   └── garaje_servicio.py
└── ui/
    ├── __init__.py
    └── app_tkinter.py
