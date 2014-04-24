# Presentacion tecnica LeTSAS 4

!SLIDE portada

# LeTSAS 4.0

!SLIDE antecedentes

#¿Porqué LETSAS 4.0?

 - LeTSAS 3.x es muy estable, pero nota ya el paso del tiempo, necesita actualizar su software.
 - No existía conocimiento en la organización sobre el proyecto. Se comienza desde un mero pendrive y documentación técnica pero no referente a la construcción de la distribución.
 - Renovación tecnológica, apuesta de futuro y ahorro de costes con los terminales que ya tenemos desplegados.

!SLIDE encontramos

# ¿Qué nos encontramos?
LeTSAS es un proyecto con buena base, pero muy fragmentado:
- 13 Kernels diferentes para los 13 tipos de hardware actual existente.
- Idem para los filesystem de las diferentes máquinas.
- Proceso de recreación de la imagen no muy claro.
- La actualización de la imagen hay que hacerla completa (lo que imposibilta so actualización masiva vía red).

!SLIDE objetivos
#¿Qué objetivos nos marcamos para LeTSAS 4?

!SLIDE objetivos
# Unificar la distribución ...
Un solo filesystem y un sólo kernel para toda la base de hardware existente.

!SLIDE unificar
Para la unificación de la distribución nos hemos basado en las siguientes herramientas:
- Personalización completa del kernel: escogiendo y optimizando opción por opción (Incluyendo todo el hardware de toda la base instalada)
@@@ bash
-rw-r--r-- 1 root root 2.3M Apr  9 20:55 bzImage
@@@

!SLIDE unificar
- Personalización completa del stack de compilación, escogiendo las opciones necesarias para GCC (aquí nos tenemos que conformar con el mínimo común denominador)
@@@ bash

@@@ 

!SLIDE objetivos
# ... permitiendo la personalización
Trabajar en un sistema eficaz y controlado en el que cada organización pueda incorporar los cambios que crea convenientes en la distribución (incluyendo autoria y distribución del desarrollo si queremos).


!SLIDE objetivos
# Proceso sencillo para la generación de la distribución:
Un sólo comando genera la distribución desde 0:
@@@ bash
lgi4 scripts # ./target.sh
Creating target directories
Writting /etc/init.d/rcS ...
Addind +x to rcS ...
Writting /etc/inittab ...
Touching /etc/fstab ...
Writting /etc/mtab ...
Touching /var/log/lastlog ...
Touching /var/log/wtmp ...
Touching /etc/resolv.conf ...
Setting boot environment ...
Copying kernel configuration ...
Purging gentoo news ...
Setting Glibc timezone info ...
Emerging base system ...
@@@

!SLIDE objectivos
# Rolling updates
Conseguir una distribución que podamos actualizar poco a poco, y que ademas nos permita hacer betatesting sin nada más que colocar una etiqueta en el repositorio de la distribución.


!SLIDE html5
# Objetivo: Incorporar navegador con soporte HTML5 a LeTSAS.
De esta forma podremos usar las diferentes aplicaciones corporativas y departamentales que ya se están sirviendo vía web sin pasar por la capa citrix.
Problema: Las máquinas más pequeñas sólo tienen 128MB de RAM, El más ligero de los motores HTML5 que hemos probado incorpora una carga de RAM de más de 200MB 

!SLIDE sabores
# Sabores de LeTSAS
La distribución "estandar" incorpora el siguiente software:
- Acceso remoto por ssh (dropbear)
- Servidor VNC.
- Cliente Altiris.
- Cliente ICA.
- Terminal X.
- Navegador web SAS (basado en webkit).
- Cliente RDP.
- Demonio de impresión LPRNG.

!SLIDE sabores
# Sabores de LeTSAS
Adicionalmente tenemos una versión de la distribución que supera los 128MB de disco y que contiene el siguiente software adicional:
- Java.
- Libreoffice.

- Ligero: 
Framebuffer.
BTRFS.
GIT para actualizaciones.
Compresion de RAM (ZRAM).
