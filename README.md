Utilize una matriz de 12 filas por 3 columnas, implementada mediante la librería NumPy para optimizar el rendimiento y las operaciones matriciales. La estructura se define como:

Filas: Representan los 12 meses del año (índices 0-11)
Columnas: Representan los 3 departamentos (índices 0-2)
Valores: Almacenan los montos de ventas en formato float64

Métodos Principales
1. Método para Insertar Ventas
El método insertar_venta(mes, departamento, monto) recibe como parámetros el mes, el departamento y el monto de la venta. El proceso de inserción se realiza de la siguiente manera:

Validación de índices: Primero valida que el mes (0-11) y el departamento (0-2) existan dentro de la estructura
Validación de datos: Verifica que el monto sea un valor numérico positivo
Acceso directo: Obtiene la posición exacta dentro de la matriz usando los índices correspondientes: matriz[mes][departamento]
Almacenamiento: Almacena el monto en esa celda, sumándolo al valor existente si ya hay datos previos

Este acceso directo por índices garantiza una complejidad temporal de O(1), haciendo la operación extremadamente eficiente.
2. Método de Búsqueda
El método buscar_por_mes_departamento(mes, departamento) permite consultar una venta específica indicando el mes y el departamento. Al igual que en el método para insertar, se utilizan los índices de fila y columna para acceder directamente al valor almacenado en la matriz, lo que hace la búsqueda rápida y eficiente.
El proceso es:

Validación de los parámetros de entrada
Acceso directo a la posición matriz[mes][departamento]
Retorno del valor almacenado

Adicionalmente, se implementaron métodos de búsqueda avanzada:

buscar_por_monto(min, max): Búsqueda por rango de valores
buscar_multiples_criterios(): Permite filtrar por múltiples condiciones simultáneamente

3. Método para Eliminar Ventas
El método eliminar_venta(mes, departamento, monto) es fundamental para mantener la integridad estructural. No modifica el tamaño de la matriz, sino que restablece el valor de la venta a cero en la posición indicada. Esto simula la eliminación de una venta manteniendo la estructura del arreglo intacta.
Características importantes:

Permite dos modos de eliminación:

Total: Resetea la celda a 0.00
Parcial: Resta un monto específico del total existente


Preserva la dimensionalidad de la matriz (siempre 12×3)
Valida que no se generen valores negativos

4. Método para Mostrar la Matriz
El método mostrar_matriz() recorre la matriz y presenta los datos de forma ordenada, mostrando los meses como filas y los departamentos como columnas. El algoritmo implementado:

Itera sobre cada fila (mes) de la matriz
Para cada fila, accede a las tres columnas (departamentos)
Formatea los valores monetarios con separadores de miles
Calcula totales por fila (mes) y por columna (departamento)
Presenta la información en formato tabular legible

Optimizaciones Implementadas

Uso de NumPy: Operaciones vectorizadas para cálculos de totales
Enumeraciones: Índices legibles mediante IntEnum (ej: Mes.ENERO, Departamento.DEPORTES)
Validación centralizada: Método _validar_indices() reutilizable
Type hints: Facilita el mantenimiento y detección de errores
Persistencia eficiente: Serialización JSON para guardado/carga de datos

Por ultimo el sistema implementa dos mecanismos de persistencia:

Guardado interno: Archivo JSON (ventas_data.json) con carga automática al iniciar
Exportación externa: Archivos CSV compatibles con hojas de cálculo
