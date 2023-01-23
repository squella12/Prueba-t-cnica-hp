# PokeApi App

Una aplicación web construida con Django como backend y React como frontend. Utiliza la PokeAPI para obtener información sobre los Pokemon y ofrece diferentes opciones de filtrado.

## Requerimientos
- Python 3.6+
- Node.js
- npm (viene con Node.js)

## Instalación
1. Clona este repositorio en tu computadora.
``` git clone https://github.com/squella12/Prueba-tecnica-hp.git ```
2. Crea un nuevo entorno virtual en Python con el comando 
``` python -m venv nombre_del_entorno_virtual ```
3. Activa el entorno virtual con el comando 
``` source nombre_del_entorno_virtual/bin/activate ```
(en Windows, usa `nombre_del_entorno_virtual\Scripts\activate.bat`)
4. Instala las dependencias de Python con el comando 
``` pip install -r requirements.txt ```
5. Entra en la carpeta `frontend` con el comando 
``` cd frontend ```
6. Instala las dependencias de Node.js con el comando 
``` npm install ```

## Uso
1. Inicia el servidor de Django con el comando en la carpeta raíz del proyecto.
``` python manage.py runserver ```

2. Inicia el servidor de React con el comando en la carpeta `frontend`.
``` npm start ```

3. Abre tu navegador en `http://localhost:3000` para ver la aplicación.

## Funciones
- Ver todos los Pokemon que pesen más de 30 y menos de 80: Al presionar el botón "Weight Filter" en la barra de navegación se filtrarán los Pokemon que cumplan con este criterio.
- Ver todos los Pokemon tipo “grass”: Al presionar el botón "Type Grass Filter" en la barra de navegación se filtrarán los Pokemon que sean de tipo "grass".
- Ver todos los Pokemon tipo “flying” que midan más de 10: Al presionar el botón "Flying and Height Filter" en la barra de nave
- Ver todos los nombres de los Pokemon invertidos, porejemplo, “bulbasaur” → “ruasablub”: Al presionar el botón "Reversed Name" en la barra de navegación se mostrarán los nombres de los Pokemon invertidos.

## Adicionalmente
- Tambien puedes ver todos los pokemones en la página principal al presionar el botón "All Pokemons" en la barra de navegación.
- Tambien puedes borrar todos los pokemones de la base de datos dirigiendote a  `http://127.0.0.1:8000/api/deletepokemon/`

## Tecnologías Utilizadas
- [Django](https://www.djangoproject.com/) como framework para el backend.
- [Django REST framework](https://www.django-rest-framework.org/) para construir la API.
- [React](https://reactjs.org/) como framework para el frontend.
- [Tailwind](https://tailwindcss.com/) como librería de estilos.
- [PokeAPI](https://pokeapi.co/) como fuente de datos sobre los Pokemon.
