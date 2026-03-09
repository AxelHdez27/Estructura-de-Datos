Forma 1.- En la forma en que se pidio en el Aula que el codigo, si pide eliminar un elemento que no esta este se agruegue y elimine y que a su vez si quiero eliminar un elemento abajo del tope se borre todo hasta llegar a ese elemento y que los valores anteriores se restauren:
¿Con cuántos elementos quedó la pila?
La pila terminó con 5 elementos: X, Y, V, W y R.

¿Hubo algún caso de error (desbordamiento o subdesbordamiento)?
No hubo ningún error. El desbordamiento no ocurrió porque en ningún momento se intentaron guardar más de 8 elementos, que es el límite de la pila. El subdesbordamiento tampoco sucedió, ya que nunca se quiso eliminar un elemento cuando la pila estaba vacía. Las operaciones de eliminación simplemente no hicieron nada porque los valores que se pidió sacar (Z, T, U y p) se agregaron y eliminaron automaticamente por como esta hecho el codigo, así que todo se mantuvo dentro del funcionamiento normal.

Forma 2.- En esta versión, cuando se pide eliminar un valor que no existe, lo que realmente hace es eliminar el último elemento que se insertó (el tope actual), sin importar qué valor se haya pedido.
¿Con cuántos elementos quedó la pila?
La pila terminó con 2 elementos: V y R.

¿Hubo algún caso de error?
Sí, ocurrió subdesbordamiento en el paso e, cuando se intentó eliminar U pero la pila ya estaba vacía. Eso es un error porque no se puede eliminar de una pila vacía.
