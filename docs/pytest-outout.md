# Resultado de pytest

Test ejecutado: `test_parse_failed_ips_counts_correctly`

Este test verifica que la función `parse_failed_ips` cuenta correctamente los intentos de login SSH fallidos por dirección IP, distingue entre intentos fallidos y exitosos, y construye correctamente el conjunto de IPs únicas.

Para ello, se genera un archivo de log temporal con contenido de prueba conocido (2 fallos para una IP, 1 fallo para otra, y un login exitoso de una tercera IP que no debe contarse como fallo), y se comprueba que el resultado de la función coincide exactamente con lo esperado.

## Salida obtenida

========================================================== test session starts ==========================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\natal\Documents\8. CORNER ESTUDIOS\sysadmin-toolkit
plugins: Faker-40.39.0
collected 1 item

test_toolkit.py::test_parse_failed_ips_counts_correctly PASSED                                                                     [100%]

=========================================================== 1 passed in 0.09s ===========================================================
