## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pytest.

## Objetivo
Agregar una mejora a la mini-aplicación web Trivia de cultura general:
1. El endpoint GET /api/preguntas debe aceptar el parámetro opcional de consulta `cantidad` (entero entre 1 y 5).
2. Si se especifica `cantidad`, devuelve solo esa cantidad de preguntas.
3. Si no se envía el parámetro `cantidad`, devuelve 5 preguntas por defecto.
4. Si `cantidad` es menor que 1 o mayor que 5, responde con código de estado 422.
5. Actualiza la página principal (HTML/JS) para incluir un control donde el usuario pueda elegir cuántas preguntas jugar (de 1 a 5).
6. Crea una prueba automatizada en tests/test_mejora.py que verifique este parámetro y el código de estado 422.

## Contexto
Lee AGENTS.md, app/main.py, app/servicios.py y app/templates/index.html.

## Restricciones
No modifiques ni borres tests/test_aceptacion.py.
Usa solo las dependencias existentes en requirements.txt.
Mantén la lógica en app/servicios.py y las rutas en app/main.py.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a modificar/crear y espera mi aprobación.

## Ejemplo
GET /api/preguntas?cantidad=2 devuelve una lista con exactamente 2 preguntas.
GET /api/preguntas?cantidad=10 devuelve código de estado 422.

## Criterio de éxito
python -m pytest -v ejecuta y aprueba todas las pruebas (incluyendo tests/test_mejora.py) y ruff check . no reporta errores. Si después de 3 intentos las pruebas no pasan, detente y explica el problema.