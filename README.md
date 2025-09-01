Nombres del Grupo
Estudiante 1: Yury Andrea Dorado Lucas

Estudiante 2: Cristian David Rodriguez Ruiz

Estudiante 3: Jonathan David Lancheros Bello

Proceso de trabajo
Organización del grupo
Cada miembro del grupo se encargó de implementar una de las operaciones con lenguajes y sus respectivos ejercicios:

Estudiante 1 (rama-estudiante1): Unión de lenguajes - ejercicios 1 al 10

Estudiante 2 (rama-estudiante2): Intersección de lenguajes - ejercicios 1 al 10

Estudiante 3 (rama-estudiante3): Concatenación de lenguajes - ejercicios 1 al 10

Comandos Git utilizados por cada estudiante
Estudiante 1 (Yury Andrea Dorado Lucas):

git checkout -b rama-estudiante1
# Implementar función union_lenguajes y ejercicios 1-10
git add lenguajes.py
git commit -m "Implementación de unión de lenguajes y ejercicios 1-10"
git push origin rama-estudiante1

Estudiante 2 (Cristian David Rodriguez Ruiz):
git checkout -b rama-estudiante2
# Implementar función interseccion_lenguajes y ejercicios 1-10
git add lenguajes.py
git commit -m "Implementación de intersección de lenguajes y ejercicios 1-10"
git push origin rama-estudiante2

Estudiante 3 (Jonathan David Lancheros Bello):
git checkout -b rama-estudiante3
# Implementar función concatenacion_lenguajes y ejercicios 1-10
git add lenguajes.py
git commit -m "Implementación de concatenación de lenguajes y ejercicios 1-10"
git push origin rama-estudiante3

Proceso de fusión (Pull Requests)
Cada estudiante creó un Pull Request desde su rama hacia la rama main a través de GitHub:

Yury creó PR desde rama-estudiante1 a main

Cristian creó PR desde rama-estudiante2 a main

Jonathan creó PR desde rama-estudiante3 a main

Los otros miembros revisaron el código de cada PR:

Los PRs fueron revisados por los dos estudiantes no autores

Se hicieron comentarios y sugerencias de mejora cuando fue necesario

Los autores respondieron a los comentarios y realizaron los cambios requeridos

Después de la aprobación de al menos un revisor, los PRs fueron fusionados:

Se utilizó "Squash and merge" para mantener un historial limpio

Las ramas fueron eliminadas después de la fusión

El proceso se realizó en el siguiente orden:

PR de unión (rama-estudiante1)

PR de intersección (rama-estudiante2)

PR de concatenación (rama-estudiante3)

Actualización del repositorio local después de cada fusión:

git checkout main
git pull origin main


Estructura del Proyecto
lenguajes.py
Archivo principal que contiene:

Definición de los lenguajes base L1, L2, L3, L4, L5

Funciones para operaciones con lenguajes:

union_lenguajes(L, M): Calcula la unión de dos lenguajes

interseccion_lenguajes(L, M): Calcula la intersección de dos lenguajes

concatenacion_lenguajes(L, M): Calcula la concatenación de dos lenguajes

pertenece(palabra, lenguaje): Verifica si una palabra pertenece a un lenguaje

Funciones con los ejercicios resueltos:

ejercicios_union(): 10 ejercicios de unión de lenguajes

ejercicios_interseccion(): 10 ejercicios de intersección de lenguajes

ejercicios_concatenacion(): 10 ejercicios de concatenación de lenguajes

Instrucciones de uso
Clonar el repositorio:

git clone https://github.com/TathanBello/Automatas.git
cd Automatas

Ejecutar el script principal:

python lenguajes.py

El programa mostrará los resultados de todos los ejercicios de unión, intersección y concatenación.

Contribuciones
Yury Andrea Dorado Lucas: Implementó la función de unión y resolvió los ejercicios 1-10 de unión

Cristian David Rodriguez Ruiz: Implementó la función de intersección y resolvió los ejercicios 1-10 de intersección

Jonathan David Lancheros Bello: Implementó la función de concatenación y resolvió los ejercicios 1-10 de concatenación

Comandos Git adicionales útiles

# Ver estado actual de los archivos
git status

# Ver historial de commits
git log --oneline

# Ver diferencias entre commits
git diff

# Descargar cambios remotos sin fusionar
git fetch

# Crear una rama nueva basada en main actualizada
git checkout main
git pull origin main
git checkout -b nueva-rama