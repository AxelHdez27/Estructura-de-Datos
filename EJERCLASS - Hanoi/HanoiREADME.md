El programa maneja 5 funciones:
hanoi(n, origen, auxiliar, destino): Genera todos los movimientos necesarios para resolver el problema. Usa una pila iterativa en lugar de recursión para evitar el RecursionError de Python con valores grandes de n.
dibujar(): Borra y redibuja el canvas completo con el estado actual de las tres torres y sus discos en cada frame de la animación.
animar(): Extrae un movimiento de la lista, mueve el disco correspondiente entre torres, actualiza los contadores de movimientos y tiempo en pantalla, y se vuelve a llamar a sí misma usando ventana.after(200, animar).
iniciar() : Lee el número de discos ingresado por el usuario, valida que esté entre 1 y 64, inicializa las torres, genera todos los movimientos llamando a hanoi() y arranca la animación.
ventana.mainloop(): Mantiene la ventana de tkinter activa y procesa todos los eventos de la interfaz gráfica.

2. Tiempos de ejecución
Se midió el tiempo que tarda la función hanoi() en generar la lista completa de movimientos. Los valores de n=5 y n=10 fueron medidos directamente. Los de n=30 y n=64 son calculados, ya que n=30 agota la memoria RAM al intentar guardar más de mil millones de movimientos, y n=64 es físicamente imposible de ejecutar.
Con 5 discos se generan 31 movimientos en 0.000021 segundos. Animados a 200ms por movimiento, la solución se ve completa en unos 6.12 segundos.
Con 10 discos se generan 1,023 movimientos en 0.000314 segundos. La animación completa tomo unos 209.22 segundos .
Con 30 discos se generarían 1,073,741,823 movimientos. Solo calcularlos tomaría unos 95 segundos y consumiría varios gigabytes de RAM. Animarlos a 200ms cada uno tomaría aproximadamente 68 años.
Con 64 discos el número de movimientos es 18,446,744,073,709,551,615. Guardar esa lista requeriría más de 130,000 petabytes de RAM, lo cual es imposible. Si de alguna forma pudiera ejecutarse, la animación tardaría unos 585,000 millones de años, más de 40,000 veces la edad actual del universo.

3.- Conclusiones 
El crecimiento exponencial es real y brutal. Entre n=5 y n=10 el tiempo de cálculo se multiplicó por 15, lo que es consistente con que los movimientos crecieron de 31 a 1,023. Cada disco que se agrega duplica exactamente el trabajo total, sin excepción.
Con n=30 el problema no es la velocidad del algoritmo sino la memoria. Python necesita guardar más de mil millones de tuplas en una lista antes de empezar a animar, lo que colapsa la RAM de una computadora común antes de que termine el cálculo.
El límite de 64 discos en el programa es teórico. Está ahí para demostrar que el código acepta ese rango, no porque sea posible ejecutarlo. Ninguna computadora existente ni futura podría resolverlo paso a paso.
Cambiar la recursión por una versión iterativa no hace el algoritmo más rápido, sigue siendo O(2^n), pero sí lo hace correcto. La versión recursiva original fallaría con RecursionError antes de llegar a n=1000 en Python, haciendo que el límite de 64 fuera inútil.
La lección más importante es que un algoritmo puede estar perfectamente implementado, ser el más eficiente posible para ese problema, y aun así ser completamente impracticable para entradas medianas. La complejidad exponencial no es un problema de código, es una barrera matemática.
