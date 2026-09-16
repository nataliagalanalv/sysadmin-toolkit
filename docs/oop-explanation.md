# POO para Inventarios de Red

A la hora de realizar un inventario buscamos que los datos estén de la manera más clara y organizada posible, no sólo para insertar nuevos datos, sino para posteriormente buscarlos y tratarlos.

En programación no estructurada se pueden realizar bases de datos para inventarios, pero siempre con el inconveniente de la **poca flexibilidad** o capacidad de gestión de ésta.

La programación orientada a objetos ofrece ese extra que permite la manipulación y gestión de bases de datos o inventarios de forma más **rápida, organizada y estructurada**. Usando de ejemplo la clase creada para este proyecto (`network_models/`), nos permite en primer lugar establecer las características de cada objeto. No habrá que ir de forma individual a cambiarlas, sino que esta programación nos permite definirlas en un solo lugar y aplicarlas a todas las entradas de ese tipo de objetos. Además de ello, podemos hacer familias: en nuestro ejemplo tenemos un objeto padre del cual surgen dos clases de objetos más, `Router` y `Server`. Cada uno hereda las mismas características, aunque podrían añadirse nuevas.

Junto con las características, la programación orientada a objetos permite establecer **comportamientos** a partir de funciones, haciendo que la gestión del inventario no sea simple añadir y lectura de datos, sino que pueda interactuar y responder a posibles cambios en el propio inventario.