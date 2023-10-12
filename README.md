# SOBRE LA APP

API que funciona principalmente como crud para almacenar usuarios en un archivo json, cuenta con varias funcionalidades:

# ENDPOINTS

Contamos con endpoints publicos y privados:

PUBLICOS:

- <span style="color:blue">POST</span> /register : Creacion de usuario regular, require mail, username y password.

- <span style="color:blue">POST</span> /login : Login de usuario, retorna token JWT de autenticacion, requiere username y password.

PRIVADOS:

- <span style="color:green">GET</span> /users : Retorna los username de todos los usuarios almacenados en el archivo json.

- <span style="color:green">GET</span> /puedopasar?user=<xxxx> : Valida si el token es valida y si corresponde al username pasado por query params.

# requisitos para iniciar el proyecto de manera local:

- Necesitas tener instalado python y por consecuente sus gestor de paquetes pip (podes descargarlo desde **https://www.python.org/downloads/**).

PASOS PARA INSTALAR EL PROYECTO:

1 - Realizar un git clone de este repositorio.

2 - Crear un entorno virtual y activarlo en la raiz del proyecto clonado:
mac -> python3 -m virtualenv venv, luego : source venv/bin/activate  
win -> python -m venv venv, luego : venv\Scripts\activate

3 - Debemos completar las variables de entorno, renombraremos .env.example a .env y setearemos un valor para las variables correspondientes.

4 - Una vez en el venv instalaremos invoke de la siguiente manera: **pip install invoke**
"esto nos permitira facilitara el uso de la api sin importar que sistema operativo utilicemos. "
(https://www.pyinvoke.org/)

5 - Digitaremos el siguiente comando : **invoke init**
"este comando inicializara el proyecto y nos instalara todas las dependencias necesarias en nuestro venv"

PODEMOS HACER USO DE LA API TANTO DESDE **invoke init** COMO USANDO EL COMANDO **flask run**.
