---
name: Introducción Teórica a la Red Lightning
goal: Descubrir la Red Lightning desde una perspectiva técnica
objectives:
  - Entender el funcionamiento de los canales de la red.
  - Familiarizarse con los términos HTLC, LNURL y UTXO.
  - Asimilar la gestión de la liquidez y las comisiones de la LNN.
  - Reconocer la Red Lightning como una red.
  - Entender los usos teóricos de la Red Lightning.
---

# Un Viaje hacia la Segunda Capa de Bitcoin 

Adéntrese en el corazón de la Lightning Network, un sistema esencial para el futuro de las transacciones de Bitcoin. LNP201 es un curso teórico que profundiza en el funcionamiento técnico de la Lightning Network. Desvela los fundamentos y mecanismos de esta red de segunda capa/nivel, diseñada para facilitar pagos Bitcoin rápidos, económicos y escalables.

Gracias a su red de canales de pago, la tecnología Lightning, posibilita transacciones rápidas y seguras, sin necesidad de registrar cada intercambio en la blockchain ("cadena de bloques") de Bitcoin. A lo largo de este curso, aprenderás a crear, gestionar y cerrar los canales de pago. También aprenderemos cómo enrutar los pagos de forma segura, a través de nodos intermedios, minimizando la necesidad de confianza en otros nodos. Además, trataremos  la gestión de la liquidez. Descubrirás la utilidad de las «transacciones de compromiso» (Commitment transactions), los HTLC, las «claves de revocación» (Revokation key), los mecanismos de penalización, el «enrutamiento cebolla» (Onion Routing) y las facturas.

Tanto si eres un principiante como si ya eres un usuario experimentado de Bitcoin, este curso te proporcionará información valiosa sobre cómo entender y utilizar la Lightning Network. Aunque cubriremos algunos de los fundamentos sobre el funcionamiento de Bitcoin en las primeras etapas, es esencial tener una comprensión sólida de la invención de Satoshi antes de profundizar en LNP201.

¡Disfruta tu viaje por la Lightning Network!

+++

# Introducción
<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>

## Visión General del Curso
<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>

¡Bienvenido al curso LNP201!

Este curso te proporcionará un amplio conocimiento técnico de la Lightning Network, que es una capa superpuesta, que facilita transacciones de Bitcoin rápidas y, a menudo, a bajo coste. A lo largo del curso, irás descubriendo los conceptos fundamentales que rigen el sistema: la apertura de canales de pago, las técnicas de enrutamiento y la gestión de la liquidez.

**Sección 1: Los Fundamentos** 
Comenzaremos con una introducción general a la Lightning Network, en la que abordaremos: los fundamentos esenciales de Bitcoin, las direcciones, los UTXOs y el funcionamiento de las transacciones. Este repaso básico es necesario para entender que, la Lightning Network se basa en sus mecanismos subyacentes en "la cadena de bloques" (blockchain) de Bitcoin para operar de forma segura.

**Sección 2: Apertura y cierre de canales** 
En esta sección, exploraremos el proceso de apertura de canales, que es la piedra angular de la Lightning Network. Aprenderás cómo se crean las transacciones de compromiso (*commitment transactions*), el papel que tienen las claves de revocación (*Revokation key*) para la seguridad y, cómo se pueden cerrar los canales de forma colaborativa o unilateral. Cada paso se explica con precisión y de forma técnica, para que puedas comprender todos los detalles.

**Sección 3: Una red de liquidez**
La Lightning Network no se limita a los canales de pago individuales, sino que es una auténtica red de pagos. Veremos cómo las transacciones pueden enrutarse/direccionarse, a través de nodos intermediarios/intermedios, utilizando los HTLC. Esta sección también aborda los retos de la gestión de la liquidez entrante y saliente en los canales de pago.

**Sección 4: Herramientas de la Lightning Network**
En esta sección se presentan las herramientas prácticas de la Lightning Network, como son:  las facturas (Invoices), las LNURL y la “clave de revocación” (Keysend). También trataremos la gestión de la liquidez de tus canales de pago, un aspecto esencial para garantizar la fluidez de los pagos y maximizar la eficiencia de tus transacciones con la tecnología Lightning.

**Sección 5: Ve más allá** 
Por último, concluiremos la formación con un repaso de los conceptos tratados y avanzaremos hacia temas más específicos para áquellos que deseen profundizar en sus conocimientos sobre la Lightning Network.

¿Listo para descubrir el funcionamiento técnico de la Lightning Network? ¡Vamos a ello!

# Los Fundamentos

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Entendiendo la Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

:::video id=62831f54-0ee7-403b-b0e3-67084c2ef6ea:::

La Lightning Network es una red de canales de pagos, construida sobre el protocolo Bitcoin, que permite transacciones rápidas y a bajo coste. Permite crear canales de pago entre participantes, en los que las transacciones pueden realizarse de forma casi instantánea y con comisiones mínimas, sin necesidad de registrar cada operación por separado en la cadena de bloques de Bitcoin (blockchain). De este modo, la Lightning Network mejora la escalabilidad de Bitcoin y lo hace apto para pagos de bajo importe.

Antes de abordar el aspecto «red» ("network"), es fundamental comprender el concepto de **canal de pago** ("payment channel") en Lightning, su funcionamiento y sus particularidades. Este es el tema de este primer capítulo.

### El Concepto de un canal de pagos

### Un canal de pago permite a dos partes, en este caso **Alice** y **Bob**, intercambiar fondos a través de la Lightning Network. Cada parte tiene un nodo, simbolizado por un círculo, y el canal de pago, entre ellos, está representado por un segmento, que los conecta.

![LNP201](assets/en/01.webp)

En nuestro ejemplo, Alice tiene 100,000 satoshis en su extremo del canal de pago y Bob tiene 30.000, por lo que el total es de 130.000 satoshis, y ésta es es la **capacidad total del canal**.

**¿Qué es un satoshi?**

El **satoshi** (o «sat») es una unidad de cuenta de Bitcoin. Al igual que un céntimo de euro, un satoshi es simplemente, una fracción de un Bitcoin. Un satoshi equivale a **0.00000001 Bitcoin**, es decir, la cienmillonésima parte de un Bitcoin. A medida que aumente el valor de Bitcoin, el uso de satoshis se volverá más práctico.

### La distribución de fondos en el canal de pagos
Volvamos al canal de pago. El concepto clave aquí es el «**extremo del canal**». Cada participante tiene fondos en su extremo/lado del canal: Alice tiene 100.000 satoshis (sats) y Bob, 30.000 satoshis (sats). Como hemos visto, la suma de estos fondos representa la capacidad total del canal; es un número fijo cuando se abre el canal de pago.

![LNP201](assets/en/02.webp)

Pongamos un ejemplo de transacción Lightning: Si Alice quiere enviar 40,000 satoshis a Bob, puede hacerlo, porque tiene fondos suficientes (100,000 satoshis). Tras esta transacción, Alice tendrá 60,000 satoshis y Bob tendrá 70,000 sats.

![LNP201](assets/en/03.webp)

La **capacidad del canal** se mantiene constante en 130,000 satoshis. Lo que cambia es la distribución de los fondos. Este sistema no permite enviar más fondos de los que se tienen. Por ejemplo, si Bob quisiera enviar 80,000 satoshis a Alice, no podrá, porque únicamente tiene 70,000.

Otra manera de imaginar la asignación de fondos es pensar en un **deslizador** que indica dónde están los fondos en el canal. Inicialmente, con 100,000 satoshis para Alice y 30,000 para Bob, el deslizador está lógicamente en el extremo de Alice. Después de la transacción de 40,000 satoshis, el deslizador se moverá ligeramente hacia el lado de Bob, quien ahora tiene 70,000 satoshis.

![LNP201](assets/en/04.webp)

Esta representación puede ser útil para visualizar la distribución de fondos de un canal de pago.

### Las reglas fundamentales de un canal de pagos

Lo primero que hay que hay que tener en cuenta es, que la capacidad del canal es fija. Es como el diámetro de una tubería: determina la cantidad máxima de dinero que puede enviarse a través del canal de pago en un momento dado.
Pongamos un ejemplo: si Alice dispone de 130.000 satoshis, solamente puede enviar 130.000 satoshis a Bob en una única transacción. Sin embargo, Bob puede devolverle una parte o la totalidad de estos fondos.

Es importante entender que la capacidad fija del canal limita el importe máximo de una única transacción, pero no el número total de transacciones posibles ni el volumen total de fondos intercambiados dentro del canal.

**¿Qué deberías extraer del contenido de este capítulo?**

- La capacidad de un canal es fija y determina la cantidad máxima que se puede enviar en una sola transacción.
- Los fondos de un canal se reparten entre los dos participantes, y cada uno únicamente puede enviar al otro los fondos de los que dispone.
De este modo, la Lightning Network permite intercambiar fondos de forma rápida y eficaz, respetando los límites impuestos por la capacidad de los canales.
Con esto concluye el primer capítulo, en el que hemos sentado las bases de la Lightning Network. En los siguientes capítulos, veremos cómo abrir un canal y profundizaremos en los conceptos aquí tratados.

## Bitcoin, Direcciones, UTXO y Transacciones

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

:::video id=e516e004-3977-45e2-8f50-aa582061b7fa:::

Este capítulo es un poco especial, porque no está dedicado directamente a la Lightning Network, sino a Bitcoin.
De hecho, la Lightning Network es una capa, que se superpone a Bitcoin. Por lo tanto, es importante comprender algunos conceptos básicos de Bitcoin, para ir entendiendo correctamente cómo funciona la Lightning Network en los siguientes capítulos. En este capítulo, repasaremos los conceptos básicos de las direcciones de recepción de Bitcoin, los UTXO y el funcionamiento de las transacciones de Bitcoin.

### Direcciones Bitcoin, claves públicas y privadas

Una dirección Bitcoin es una cadena de caracteres derivada de una **clave pública**, que ,a su vez, se calcula a partir de una **clave privada**. Como sabes, se utiliza para bloquear Bitcoins, lo que equivale a recibirlos en nuestro monedero.

La clave privada es un elemento secreto que **nunca debe compartirse**, mientras que la clave pública y la dirección pueden compartirse, sin que suponga ningún riesgo para la seguridad (su divulgación sólo representa un riesgo para tu privacidad). A continuación, se muestra una representación común, que utilizaremos a lo largo de esta formación:

- Las **claves privadas** se muestran **verticalmente**.
- Las **claves públicas** se muestran **horizontalmente**.
- Su color indica a quién pertenecen (Alice en color naranja y, Bob, en color negro).

### Transacciones de Bitcoin: Envio de dinero y Scripts

En Bitcoin, una transacción implica el envío de dinero de una dirección a otra. Tomemos el ejemplo de Alice enviando 0.002 Bitcoin a Bob. Alice utiliza la clave privada asociada a su dirección para **firmar** la transacción, lo que muestra que puede gastar esos fondos. Pero, ¿qué ocurre exactamente detrás de esta transacción? Los fondos de una dirección Bitcoin están bloqueados por un **script**, es decir, un miniprograma, que impone ciertas condiciones para el gasto de los fondos.

El script más común requiere una firma con la clave privada de la dirección. Cuando Alice firma una transacción con su clave privada, **desbloquea el script**, el cual bloquea los fondos, que ahora pueden transferirse. Transferir los fondos implica añadir un nuevo script a esos fondos, especificando que se requiere la firma de la clave privada de **Bob** para gastarlos.


![LNP201](assets/en/05.webp)

### UTXOs: Unspent Transaction Outputs: "Salidas de Transacción No Gastadas" 

En Bitcoin, lo que realmente intercambiamos no son Bitcoins, sino **UTXOs** (_Unspent Transaction Outputs_), que significa literalmente, "salidas de transacciones no gastadas".

Un UTXO es una pieza de Bitcoin que puede ser de cualquier valor, por ejemplo **2,000 Bitcoins**, **8 Bitcoins**, o incluso **8,000 sats**. Cada UTXO está bloqueado por un script, y para gastarlo, debes cumplir las condiciones del script, a menudo es una firma con la clave privada, correspondiente a una dirección de destinatario determinada.

Los UTXO no pueden dividirse. Cada vez que se utilizan para gastar la cantidad de Bitcoin que representan, debe hacerse en su totalidad. Es un poco como un billete: si tienes un billete de 10€ y le debes 5€ al panadero, no puedes cortar el billete por la mitad. Tienes que darle el billete de 10€ y él te dará 5€ de cambio. Este es exactamente el mismo principio para los UTXOs en Bitcoin. Por ejemplo, si Alice desbloquea un script con su clave privada, desbloquea todo el UTXO. Si solamente quiere enviar parte de los fondos representados por este UTXO a Bob, puede «fragmentarlo» en varios más pequeños. Entonces enviará 0.0015 BTC a Bob y el resto, 0.0005 BTC, a una **"dirección de cambio"** (change address).

Este es un ejemplo de una transacción con 2 salidas: 

- Un UTXO de 0.0015 BTC para Bob, bloqueado por un script, que requiere la firma con la clave privada de Bob.
- Un UTXO de 0.0005 BTC para Alice, bloqueado por un script, que requiere su propia firma.

![LNP201](assets/en/06.webp)

### Direcciones Multi-firma

Además de las direcciones simples,que se generan a partir de una única clave pública, también es posible crear **direcciones multi-firma**, a partir de múltiples claves públicas. Un caso particularmente interesante para la Lightning Network es la **dirección multi-firma 2/2** (peer-to-peer), generada a partir de dos claves públicas:

![LNP201](assets/en/07.webp)

Para gastar los fondos asociados a esta dirección multifirma 2/2 (peer-to-peer), es necesario firmar con las dos claves privadas, asociadas a las claves públicas.

![LNP201](assets/en/08.webp)

Este tipo de dirección es la representación de los canales de pago de la Lightning Network en la blockchain ("cadena de bloques") de Bitcoin.

**¿Qué debes recordar del contenido de este capítulo?** 

- Una **dirección Bitcoin** se deriva de una clave pública, que a su vez, se deriva de una clave privada.
- Los fondos en Bitcoin están bloqueados por **scripts**, y para gastar esos fondos, debes cumplir las condiciones, que marca el script, que, normalmente, implica proporcionar una firma con la correspondiente clave privada. 
- Los **UTXOs** son piezas de Bitcoin, las cuales están bloqueadas por scripts, y cada transacción en Bitcoin consiste en desbloquear un UTXO y después, crear uno o más nuevos UTXOs a cambio.
- **2/2 direcciones multi-firma** (peer-to-peer) se requiere de la firma de dos claves privadas, para poder gastar los fondos.

Estas direcciones especiales se utilizan en el contexto de la tecnología Lightning para abrir canales de pagos.
Este capítulo sobre Bitcoin nos ha permitido repasar algunos conceptos esenciales, que nos serán útiles para lo que aprenderemos a continuación. En el próximo capítulo, veremos detalladamente cómo funciona la apertura de canales en la Lightning Network.

# Apertura y Cierre de Canales

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Apertura de un canal de pagos

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

:::video id=0dd90e82-4d29-4d27-bcdf-42988ced4b16:::

En este capítulo, veremos cómo abrir un canal de pagos en la Lightning Network y analizaremos el vínculo entre la apertura del canal de pago y el sistema subyacente de Bitcoin.

### Canales de pago en la Lightning Network de Bitcoin

Como vimos en el primer capítulo, un **canal de pago** en la Lightning Network puede compararse con una "tubería" para intercambiar fondos entre dos participantes (**Alice** y **Bob**, en nuestros ejemplos). La capacidad de este canal corresponde a la suma de los fondos disponibles de cada extremo. En nuestro ejemplo, Alice tiene **100,000 satoshis** y Bob tiene **30,000 satoshis**, lo que suma una **capacidad total** de **130,000 satoshis**.

![LNP201](assets/en/09.webp)

### Niveles de Intercambio de Información

Es crucial distinguir claramente los diferentes niveles de intercambio en la Lightning Network:

- **Comunicaciones entre pares (protocolo Lightning)**: Estos son los mensajes, que los nodos de Lightning se envían entre sí para comunicarse. En nuestros diagramas, representaremos estos mensajes con líneas negras punteadas .
- **Canales de pago (protocolo Lightning)**: vías de intercambio de fondos en la Lightning Network, que representaremos con líneas negras continuas.
- **Transacciones de Bitcoin (protocolo Bitcoin)**: son las transacciones realizadas en la cadena de bloques (blockchain) y las representaremos con líneas en color naranja.

![LNP201](assets/en/10.webp)

Cabe destacar que un nodo Lightning puede comunicarse a través del protocolo P2P (peer-to-peer), sin necesidad de abrir un canal de pago, pero para intercambiar fondos es necesario un canal de pagos.

### Pasos para abrir un canal de pagos en la Lightning Network

- **Intercambio de mensajes**: Alice quiere establecer un canal de pago con Bob. Alice le envía un mensaje con la cantidad, que quiere depositar en el canal (130.000 sats) y su clave pública. Bob responde con su propia clave pública.
  
![LNP201](assets/en/11.webp)

- **Creación de la dirección multi-firma**: Alice usa estas dos claves públicas para crear una dirección multi-firma, lo que significa que, cualquier fondo depositado en esta dirección, requiere las firmas de Alice y Bob para gastarse.

![LNP201](assets/en/12.webp)

- **Transacción de depósito**: Alice prepara una transacción de Bitcoin para depositar fondos en esta dirección multi-firma. Por ejemplo, puede decidir enviar **130,000 satoshis** a esta dirección multifirma: esta transacción está **construida, pero aún no se ha publicado** en la cadena de bloques (blockchain).

![LNP201](assets/en/13.webp)

- **Transacción de retiro de fondos**: antes de publicar la transacción de depósito, Alice crea una transacción de retiro de fondos para poder recuperarlos, en caso de que haya algún problema con Bob. De hecho, una vez que Alice publica la transacción de depósito, su sats se bloquearán en una dirección multifirma 2/2 y, únicamente, podrán desbloquearse con su firma y con la de Bob. Alice se protege contra este riesgo de pérdida, construyendo la transacción de retiro, que le permite recuperar sus fondos.
  
![LNP201](assets/en/14.webp)

- **Firma de Bob**: Alice envía la transacción de depósito a Bob como prueba y, le pide que firme la transacción de retiro de liquidez. Cuando Alice obtiene la firma de Bob en la transacción de retiro de fondos, ella ya tiene la seguridad de poder recuperar sus fondos cuando quiera, ya que ahora sólo es necesaria su propia firma para desbloquear la dirección multi-firma.

![LNP201](assets/en/15.webp)

- **Publicación de la transacción de depósito**: una vez obtenida la firma de Bob, Alice puede publicar la transacción de depósito en la cadena de bloques (blockchain) de Bitcoin, abriendo el canal de pago Lightning, entre ambos usuarios, oficialmente.
  
![LNP201](assets/en/16.webp)

### ¿Cuándo se considera que el canal está abierto?

El canal se considera abierto, cuando la transacción de depósito se registra en un bloque de la blockchain de Bitcoin y esta transacción ha acumulado el número de confirmaciones necesarias (número de bloques siguientes), para verificar la validez de la operación en el canal de pagos.

**¿Qué debo recordar de este capítulo?** 
- La apertura de un canal comienza con el intercambio de **mensajes** entre las dos partes (intercambio de importes y claves públicas).
— Un canal se crea con la creación de una dirección **multi-firma 2/2 ** y el depósito de fondos en esta dirección a través de una transacción de Bitcoin.
- La persona que abre el canal se asegura de que puede **recuperar sus fondos**, mediante una transacción de retirada firmada por la otra parte, antes de publicar la transacción de depósito.

En el próximo capítulo, exploraremos el funcionamiento técnico de una transacción Lightning dentro de un canal de pagos.

## "Transacción de Compromiso" (Commitment Transaction)

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

:::video id=ec8a9259-cf0e-4142-af74-d08a867e3842:::
 
En este capítulo, descubriremos el funcionamiento técnico de una transacción dentro de un canal de pagos en la Lightning Network, es decir, cuando los fondos se mueven de un extremo del canal al otro lado del canal de pago.

### Recordatorio: El ciclo de vida del canal de pagos

Como hemos visto anteriormente, la **apertura** de un canal de pagos en la Lightning Network comienza a través de una transacción de Bitcoin. El canal se puede **cerrar** cuando se desee. También cerramos el canal a través de una transacción de Bitcoin. Entre la apertura y el cierre del canal de pago, se pueden efectuar un número casi infinito de transacciones dentro del canal de pagos, sin tener que registrarlas en la blockchain de Bitcoin. Veamos qué es lo que ocurre durante una transacción en un canal de pagos.

![LNP201](assets/en/17.webp)

### El estado inicial del canal de pago

En el momento de abrir el canal, Alice depositó **130,000 satoshis** en la dirección de multi-firma del canal. Así, en el estado inicial, todos los fondos están del lado de Alice. Antes de abrir el canal, Alice también hizo que Bob firmara una **transacción de retiro**, lo que permitiría a Alice recuperar sus fondos, en el caso de que si quisiera cerrar el canal.

![LNP201](assets/en/18.webp)

### Transacciones no publicadas: Las Transacciones de Compromiso (Commitment Transactions)

Cuando Alice realiza una transacción en el canal de pago para enviar fondos a Bob, se crea una nueva transacción de Bitcoin, la cual refleja este cambio en la distribución de fondos. Esta transacción, llamada transacción de compromiso, no se publica en la blockchain, pero representa el nuevo estado del canal, tras la transacción Lightning.

Tomemos un ejemplo en el que Alice envía 30,000 satoshis a Bob:

- **Inicialmente**: Alice tiene 130,000 satoshis.
- **Después de la transacción**: Alice tiene 100,000 satoshis y Bob tiene 30,000 satoshis.

Para validar esta transferencia, Alice y Bob crean una nueva **transacción Bitcoin no publicada**, por la que se envían **100,000 satoshis a Alice** y **30,000 satoshis a Bob** , desde la dirección multi-firma. Ambas partes construyen esta transacción de forma independiente, pero con los mismos datos (cantidades y direcciones). Una vez creada, cada parte firma la transacción e intercambia su firma con la otra parte. Esto permite a cualquiera de los dos, publicar la transacción en cualquier momento, para así reclamar su parte de los fondos del canal, en la blockchain principal de Bitcoin.

  ![LNP201](assets/en/19.webp)

### El proceso de transferencia: la factura

Cuando Bob quiere recibir dinero, envía a Alice una **factura_** por 30,000 satoshis. Alice paga esta factura, lo que inicia la transferencia dentro del canal. Como hemos visto, este proceso se basa en la creación y firma de una nueva **transacción de compromiso**.
Cada transacción de compromiso representa la distribución de fondos en el canal de pagos tras la transferencia. En este ejemplo, después de la transacción, Bob tiene 30,000 satoshis y Alice tiene 100,000 satoshis. Si uno de los dos participantes decide publicar esta transacción de compromiso en la cadena de bloques (blockchain), el canal se cerrará y los fondos se distribuirán, según la distribución final.

![LNP201](assets/en/20.webp)

### Nuevo estado después de una segunda transacción

Tomemos otro ejemplo: después de la primera transacción en la que Alice envió 30,000 satoshis a Bob, éste decide enviar **10,000 satoshis a Alice de vuelta**. Esto crea un nuevo estado del canal de pagos. La nueva transacción de compromiso reflejará así la distribución actualizada: 

- **Alice** tiene **110,000 satoshis** ahora.
- **Bob** tiene **20,000 satoshis**.
  
![LNP201](assets/en/21.webp)

Esta transacción no se publica en la blockchain, pero puede publicarse en cualquier momento, si se cierra el canal.
En resumen, cuando se transfieren fondos dentro de un canal de pago Lightning:

- Alice y Bob crean una nueva **transacción de compromiso** que refleja la nueva distribución de fondos.
- Esta transacción Bitcoin es **firmada** por ambas partes, pero **no publicada** en la blockchain de Bitcoin, mientras el canal permanezca abierto.
- Las transacciones de compromiso garantizan que cada participante pueda recuperar sus fondos en cualquier momento, publicando la última transacción firmada en la blockchain de Bitcoin.

Sin embargo, este sistema tiene una falla potencial, que abordaremos en el próximo capítulo. Veremos cómo cada participante puede protegerse de un intento de estafa que venga de la otra parte.

## Revocation Key ("llave de revocación")

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
:::video id=387747fe-bcda-499d-b247-d5c82bb6dcd7:::
En este capítulo, exploraremos en profundidad el funcionamiento de las transacciones en la Lightning Network y describiremos los mecanismos de protección contra estafas y de garantía de cumplimiento de las reglas por parte de todos los participantes en un canal de pago.  

### Recordatorio: Transacciones de compromiso (Commitment Transactions)
Las transacciones en Lightning se basan en **transacciones de compromiso** no publicadas. Estas transacciones de compromiso reflejan la distribución de fondos en el canal. Cuando se realiza una nueva transacción en la Lightning Network, se crea una nueva transacción de compromiso (Commitment Transaction), que es firmada por ambas partes,y que refleja el nuevo estado del canal.
Pongamos un ejemplo sencillo: 
- **Estado inicial**: Alice tiene **100,000 satoshis**, Bob tiene **30,000 satoshis**.
- Después de una transacción, en la que Alice envía **40,000 satoshis** a Bob, la nueva transacción de compromiso refleja la distribución de los fondos de la siguiente manera:
- Alicia: **60,000 satoshis**
- Bob: **70,000 satoshis**.
  
![LNP201](assets/en/22.webp)

En cualquier momento, ambas partes pueden publicar la **última transacción de compromiso firmada** para cerrar el canal y recuperar sus fondos.

### La falla en el proceso: Estafar a la contraparte, publicando una transacción antigua.

Si una de las partes decide **estafar**, publicando una transacción de compromiso antigua, surge un potencial problema.  Por ejemplo, Alice podría publicar una transacción de compromiso antigua con una posición de balance más favorable con **100.000 satoshis**, cuando, en realidad, sólo tiene **60.000** satoshis. Así, podría robar **40.000 satoshis** a Bob. 

![LNP201](assets/en/23.webp)

Peor aún, Alice podría publicar la primera transacción de retirada, la anterior a la apertura del canal, en la que tenía **130,000 satoshis**, y estafar, así, la totalidad de fondos del canal a Bob. 

![LNP201](assets/en/24.webp)

### Solución: Clave de revocación (Revokation Key) y Timelock (“candado de tiempo”)
Para evitar este tipo de trampas por parte de Alice, la Lightning Network añade **mecanismos de seguridad** a las transacciones de compromiso:

- **Timelock**: Cada transacción de compromiso contiene un timelock ("candado de tiempo") para los fondos de Alice. El timelock es una característica de los contratos inteligentes, que establece una condición temporal a cumplir, para que una transacción se incluya en un bloque. Esto significa que, si Alice publica una de las transacciones de compromiso, no podrá recuperar sus fondos, hasta que hayan transcurrido un número de bloques determinado. Este tiempo de espera comienza cuando se confirma la transacción de compromiso. Su duración suele ser proporcional al tamaño del canal, aunque este tiempo de espera también puede configurarse manualmente.
  
- **Clave de revocación** (Revocation Key):
El dinero de Alice también puede ser gastado directamente por Bob, si éste dispone de la clave de revocación. Esta clave está compuesta por un secreto, que guarda Alice y, otro, que tiene Bob. Tenga en cuenta que, para cada transacción de compromiso, este secreto es diferente.
Gracias a estos dos mecanismos combinados, Bob tiene tiempo de detectar el intento de engaño de Alice y de penalizarla, recuperando su salida con la clave de revocación, lo que para Bob significa recuperar todos los fondos del canal de pagos. Esta es la representación de la nueva transacción de compromiso:

![LNP201](assets/en/25.webp)

Veamos el funcionamiento de este mecanismo en su conjunto.

### Proceso de actualización de transacciones

Cuando Alice y Bob actualizan el estado del canal con una nueva transacción Lightning, ya han intercambiado por adelantado sus respectivos **secretos** para la transacción de compromiso anterior (que quedará obsoleta y podría servir para estafar al otro). Por eso, en el nuevo estado del canal:
- Alice y Bob tienen una nueva transacción de compromiso, donde se ha registrado la distribución actual de los fondos, tras la transacción Lightning.
- Cada uno de ellos tiene el secreto del otro para la transacción anterior, lo que les permite usar la clave de revocación, si uno de ellos intenta estafar fondos, publicando una transacción del estado anterior en los mempools del nodo Bitcoin. De hecho, para penalizar a la otra parte ("penalty transaction" o "justice transaction"), es necesario tener los dos secretos y la transacción de compromiso del otro participante, que incluye la entrada firmada. Sin esta transacción, la clave de revocación por sí sola es inútil. La única forma de obtener esta transacción es recuperándola de los mempools (en transacciones pendientes de registrar en la "blockchain" de Bitcoin) o de transacciones confirmadas en la blockchain de Bitcoin durante el timelock. Así, demostraríamos que la otra parte está intentando llevar a cabo un ataque malicioso, ya sea intencionadamente o no.

Para entender bien este proceso, pongamos un ejemplo:

- **Estado inicial**: Alice tiene **100,000 satoshis** y Bob, **30,000 sathosis**.

![LNP201](assets/en/26.webp)

- Bob quiere recibir 40,000 satoshis de Alice, a través de su canal de pago Lightning. Para ello:
   - Bob envía una factura a Alice, junto con su clave secreta de revocación para su transacción de compromiso anterior.
- En respuesta, Alice proporciona su firma para la nueva transacción de compromiso de Bob, así como su clave secreta de revocación, para su transacción anterior.
- Por último, Bob envía su firma para la nueva transacción de compromiso de Alice.
   - Estos intercambios permiten a Alice enviar **40,000 satoshis** a Bob, a través de su canal de pago Lightning, y las nuevas transacciones de compromiso reflejan esta distribución actualizada de fondos.

![LNP201](assets/en/27.webp)

- Si Alice intenta publicar la transacción antigua, en la que todavía tenía **100,000 sathosis**, Bob puede recuperar los fondos inmediatamente, usando la clave de revocación. Mientras tanto, Alice está bloqueada por el timelock (bloqueo temporal).

![LNP201](assets/en/28.webp)

En este caso, Bob no tiene motivaciones económicas para intentar estafar a Alice, pero si fuera así, Alice también se beneficiaría de esta protección simétrica, que ofrece las mismas garantías a Alice que a Bob.

**¿Qué debes extraer del contenido de este capítulo?**

Las **transacciones de compromiso** ("Commitments Transactions") de la Lightning Network incorporan mecanismos de seguridad que mitigan el riesgo de estafa y minimizan el incentivo para llevarlas a cabo. Antes de firmar una nueva transacción de compromiso, Alice y Bob intercambian los **secretos** de las transacciones de compromiso anteriores. En el caso hipotético, en el que Alice intente publicar una transacción de compromiso antigua, Bob podría utilizar la **clave de revocación** (Revokation Key) para recuperar la totalidad de los fondos, antes de que Alice complete la operación, lo que resultaría en una penalización por parte de Bob hacia Alice por intentar realizar una operación fraudulenta. 

Este sistema de seguridad garantiza que los participantes cumplan con las normas de la Lightning Network y que no puedan beneficiarse de la publicación de "transacciones de compromiso" antiguas. 
Ya hemos aprendido cómo las "transacciones de compromiso" de la Lightning Network incorporan mecanismos de seguridad que mitigan el riesgo de estafa y el incentivo para llevarlas a cabo. En el contexto de las transacciones de compromiso, se establece un intercambio de secretos entre Alice y Bob, antes de proceder con una nueva transacción. 

En este punto, se espera que el alumno haya desarrollado la capacidad de comprender el proceso de apertura de los canales de pago en la Lightning Network y el funcionamiento de las transacciones, que tienen lugar en dichos canales de pago. En el siguiente capítulo, se abordarán las diversas técnicas para cerrar un canal de pagos y recuperar los Bitcoins en la blockchain.

## Cierre de un canal de pago

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

:::video id=e3bfae93-85f5-4996-9dbc-5185ff0b4d0f:::

En este capítulo, discutiremos **cerrar un canal** en la Lightning Network, lo cual se hace a través de una transacción de Bitcoin, justo como al abrir un canal. Después de ver cómo funcionan las transacciones dentro de un canal, ahora es momento de ver cómo cerrar un canal y recuperar los fondos en la blockchain de Bitcoin.

## Recordatorio: El ciclo de vida de un canal de pagos
El **ciclo de vida de un canal** comienza con su **apertura**, mediante una transacción de Bitcoin. A continuación, se realizan otras transacciones Lightning en este canal de pagos. Cuando los participantes desean recuperar sus fondos, el canal de pagos **se cierra**, mediante una segunda transacción Bitcoin. Las transacciones realizadas en la Lightning Network están representadas por **transacciones de compromiso no publicadas**.

![LNP201](assets/en/29.webp)

### Los tres tipos de cierre del canal de pagos

Hay tres modos principales para cerrar el canal de pagos.
Estos tres modos los podemos llamar **El Bueno, El Bruto y El Ausente** (inspirado en el libro "Mastering the Lightning Network" de Andreas Antonopoulos).

- **El Bueno** (The Good): **cierre coperativo**, en el que Alice y Bob acuerdan el cierre del canal.
- **El Bruto** (The Bad): **cierre forzado**, en el que uno de los participantes decide cerrar el canal honestamente, pero sin que la contraparte esté de acuerdo con ello.
- **El Ausente**: *- **cierre con estafa**, en el que una de las dos partes intenta robar fondos, publicando unna transacción de compromiso antigua, en lugar de la última transacción realizada, (que es la que refleja la distribución real y justa de sus fondos), si no otra, (que, normalmente, tiene más liquidez, que la última transacción).
Por ejemplo,

- Supongamos que Alice posee **100.000 satoshis** y Bob posee **30.000 satoshis**.
- Esta distribución de fondos se refleja en dos transacciones de compromiso (una por usuario), que no se publican, pero que podrían publicarse en caso de cierre del canal.

![LNP201](assets/en/30.webp)

### El Bueno: el cierre cooperativo

En un **cierre cooperativo**, Alice y Bob acuerdan cerrar el canal. A continuación se explica detalladamente el proceso:

- Alice ha propuesto a Bob cerrar el canal, a través del protocolo de comunicación Lightning.
- Bob está de acuerdo, y las dos partes proceden a concluir sus transacciones en el canal.
  
![LNP201](assets/en/31.webp)

- Alice y Bob negocian juntos las comisiones de la **transacción de cierre**. Estas comisiones se calculan, generalmente, en base al mercado de comisiones de Bitcoin en el momento del cierre. Es importante tener en cuenta que **el individuo que inició la transacción** (en nuestro ejemplo, Alice) es responsable de las comisiones de cierre.
- Se construye una nueva **transacción de cierre**. Esta transacción se asemeja a una transacción de compromiso, sin embargo, carece de la inclusión de timelocks o mecanismos de revocación, debido a la naturaleza colaborativa de ambas partes y a la ausencia de cualquier riesgo de actividad fraudulenta. Esta transacción de cierre cooperativo es, por tanto, distinta de las transacciones de compromiso.
   Por ejemplo, si Alice posee **100,000 satoshis** y Bob posee **30,000 satoshis**, la transacción de cierre enviará **100,000 satoshis** a la dirección de Alice y, **30,000 satoshis** a la dirección de Bob, sin límite de tiempo. Una vez que esta transacción es firmada por ambas partes, es publicada por Alice. Una vez confirmada la transacción en la blockchain de Bitcoin, el canal de pago Lightning se cierra oficialmente.
  
   ![LNP201](assets/en/32.webp)

El **cierre cooperativo** es el método preferido de cierre porque es rápido (sin bloqueo de tiempo) (Timelock) y las tarifas de transacción se ajustan, de acuerdo con las condiciones actuales del mercado Bitcoin. Este enfoque garantiza que el importe del pago se ajuste adecuadamente al valor de la transacción, mitigando así el riesgo de rechazo de transacciones dentro de los mempools. Además, evita que se produzcan pérdidas financieras excesivas para todas las partes implicadas.

### El Malo: el cierre forzoso
Entre las desventajas del sistema está el cierre forzado.
Si el nodo de Alice envía un mensaje al nodo de Bob, solicitando un cierre cooperativo y éste no responde (por ejemplo, debido a un corte de Internet o a un problema técnico), Alice puede proceder a un cierre forzado, publicando la última transacción de compromiso firmada.
En este caso, Alice simplemente publicará la última transacción de compromiso, que refleja el estado del canal en el momento en que tuvo lugar la última transacción Lightning con la distribución correcta de los fondos.

![LNP201](assets/en/33.webp)

Esta transacción incluye un **timelock** para los fondos de Alice, lo que provocará un cierre más lento.

![LNP201](assets/en/34.webp)

Tenga en cuenta que las comisiones asociadas a la operación de compromiso pueden no ser adecuadas en el momento del cierre, ya que se determinan en el momento de la creación de la operación, que puede ser varios meses antes. Es práctica común entre los clientes de Lightning sobrestimar las comisiones con vistas a evitar problemas futuros, pero esto puede dar lugar a comisiones excesivas o, por el contrario, demasiado bajas.

En resumen, la opción del **cierre forzoso** es un último recurso cuando el compañero ya no responde. En general, se considera que un cierre cooperativo es más rápido y más económico. Por lo tanto, es aconsejable evitar el cierre forzoso en la medida de lo posible.

### La Estafa: el engaño

El acto de **estafar**  implica que una de las partes intenta publicar una vieja transacción de compromiso, a menudo en la que poseía más fondos de los que debería. Por ejemplo, Alice podría publicar una transacción antigua en la que poseía **120,000 satoshis**, pero en realidad solo posee **100,000 satoshis** en la actualidad.
![LNP201](assets/en/35.webp)

Para prevenir cualquier caso de engaño, Bob es responsable de monitorizar la cadena de bloques de Bitcoin (blockchain) y su mempool. Así, se asegura que Alice no publique una transacción antigua. En caso de detectar un intento de engaño, Bob puede utilizar la **clave de revocación** (Revocation Key) para recuperar los fondos del canal de pago de Alice. Como Alice está bloqueada por el timelock en su salida de fondos, Bob tiene tiempo de gastar los fondos (Bob no está bloqueado por el timelock) para recuperar toda la suma en una dirección de su propiedad.

![LNP201](assets/en/36.webp)

Si Bob no actúa dentro del tiempo permitido por el bloqueo de tiempo en la salida de Alice, el engaño podría funcionar. En este caso, la salida de Alice está desbloqueada, por lo que puede usarla para crear una nueva salida hacia una dirección que ella controle.

**¿Qué es lo más importante de este capítulo?

Hay tres maneras de cerrar un canal.
- **Cierre cooperativo**: es rápido y barato, y ambas partes acuerdan cerrar el canal de pago y publicar una transacción especial de cierre.
- **Cierre forzado**: no es un cierre óptimo, ya que hay que publicar una transacción de compromiso (Commitment Transaction), que puede tener comisiones inadecuadas y un bloqueo temporal. Esto puede ralentizar el cierre.
- **Cierre engañoso**: si alguien intenta robar fondos, publicando una transacción antigua, la otra parte puede utilizar la clave de revocación (Revokation Key) para impedirlo.
  En los próximos capítulos estudiaremos la Lightning Network más detalladamente, centrándonos en la forma de operar de esta red.

# Una Red de Liquidez

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Red Lightning (Lightning Network)

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

:::video id=52ad2fd7-0459-4635-8785-793fc5fff28e:::

En este capítulo, exploraremos cómo los pagos en la Lightning Network pueden llegar a un destinatario, incluso, si no están conectados directamente por un canal de pago. Lightning es, de hecho, una **red de canales de pago**, que permite enviar fondos a un nodo distante, a través de los canales de pago de otros participantes intermedios. Descubriremos cómo se enrutan los pagos a través de la red, cómo se mueve la liquidez entre canales y cómo se calculan las tarifas de transacción.

### La red de canales de pagos

En la Lightning Network, una transacción consiste en transferir fondos entre dos nodos. Como se ha visto en capítulos anteriores, para realizar transacciones Lightning es necesario abrir un canal de pago con alguien. Este canal permite realizar un número casi infinito de transacciones fuera de la cadena antes de que se cierre para reestablecer el saldo en la cadena. Sin embargo, este método tiene el inconveniente de que requiere un canal directo con la otra persona para recibir o enviar fondos, lo que implica una transacción de apertura y otra de cierre para cada canal. Si tengo previsto realizar un gran número de pagos con este participante, abrir y cerrar un canal resulta costoso. Por el contrario, si solo necesito realizar unas pocas transacciones Lightning, abrir un canal directo no es ventajoso, ya que me costaría dos transacciones en la cadena por un número limitado de transacciones fuera de ella. Este podría ser el caso, por ejemplo, si se quiere utilizar Lightning para pagar a un comerciante, sin tener previsto volver al comercio.

Para resolver este problema, la Lightning Network permite enrutar un pago, a través de múltiples canales y nodos intermedios, lo que permite realizar una transacción sin un canal directo con el otro participante.

Imagina, por ejemplo:

- **Alice** (en naranja) tiene un canal con **Suzie** (en gris) con **100,000 satoshis** en su lado y **30,000 satoshis** en el lado de Suzie.
- **Suzie** tiene un canal con Bob en el que ella tiene **250,000 satoshis** y Bob, no tiene satoshis.

![LNP201](assets/en/37.webp)

Si Alicia quiere enviar dinero a Bob sin abrir un canal de pago directo con él, tendrá que pasar por Suzie y, cada canal de pago tendrá que ajustar la liquidez en cada extremo. **Los satoshis enviados permanecen dentro de sus respectivos canales**; en realidad, no «cruzan» los canales, sino que la transferencia se realiza ajustando la liquidez interna de cada canal.
Supongamos que Alicia desea enviar **50.000 satoshis** a Bob:
- **Alice** envía 50.000 satoshis a **Suzie** en su canal compartido.
- Suzie replica esta transferencia enviando 50,000 satoshis al canal de **Bob** .
  
![LNP201](assets/en/38.webp)

El pago se dirige hacia Bob, a través de un movimiento de liquidez en cada canal. Al final de la operación, Alice dispone de 50,000 sats. En realidad, ha transferido 50 000 sats, ya que empezó con 100 000. Bob, por su parte, acaba con 50,000 sats más.
Para Suzie (el nodo intermedio), esta operación es neutra: empezó con 30,000 sats en su canal con Alice y,  250,000 sats en su canal con Bob, lo que suma un total de 280,000 sats. Tras la transacción, Suzie tiene 80,000 sats en su canal con Alice, y 200,000 sats en su canal con Bob, que son las mismas cifras que al principio.

Por tanto, esta transferencia está limitada por la **liquidez disponible** en el momento de la transferencia.

### Direccionamiento de rutas y límites de liquidez

Tomemos un ejemplo teórico de otra red en la que hay:

- **130,000 satoshis** del lado de Alice (en color naranja) en su canal con **Suzie** (en color gris).
- **90,000 satoshis** en el extremo de **Suzie** y **200,000 satoshis** en el extremo de **Carol** (en color rosa).
- **150,000 satoshis** en el extremo de **Carol** y **100,000 satoshis** en el extremo de **Bob**.

![LNP201](assets/en/39.webp)

Con esta configuración, el máximo que Alice puede enviar a Bob  es **90,000 satoshis**, ya que está limitada por la cantidad de liquidez mínima disponible en el canal de **Suzie a Carol**. En la dirección opuesta (de Bob a Alice), no es posible ningún pago, porque el extremo de **Suzie**, en el canal de pago que le une con **Alice**, no hay satoshis. Por lo tanto, no existe una **ruta** en condiciones operativas para una transacción a esta dirección.
Alice envía **40,000 satoshis** a Bob a través de estos canales de pago:

- Alice transfiere 40,000 satoshis a su canal común con Suzie.
- Suzie transfiere 40,000 satoshis a Carol en su canal compartido.
- Por último, Carol transfiere 40,000 satoshis a Bob.

![LNP201](assets/en/40.webp)

Los **satoshis enviados** hacia cada canal de pago **permanecen en el canal**, por lo que los satoshis enviados por Carol a Bob no son los mismos, que los enviados por Alice a Suzie. La transferencia se realiza ajustando la liquidez dentro de cada canal. Además, la capacidad total de los canales de pago permanece sin cambios.

![LNP201](assets/en/41.webp)

Como en el ejemplo anterior, después de la transacción, el nodo origen/fuente (Alice) tiene 40,000 satoshis menos. Los nodos intermedios (Suzie y Carol) retienen la misma cantidad total, haciendo la operación neutral para ellas. Finalmente, el nodo destino (Bob) recibe 40,000 satoshis adicionales.

El papel de los nodos intermedios es, por tanto, muy importante en el funcionamiento de la Lightning Network. Los nodos intermedios facilitan las transferencias, ofreciendo múltiples rutas para los pagos. Para incentivar a estos nodos a proporcionar su liquidez y participar en la tarea del enrutamiento de pagos, se les abona **honorarios por enrutamiento**.

### Comisiones por enrutamiento

Los nodos intermedios aplican comisiones para permitir que los pagos pasen a través de sus canales. Estas comisiones son fijadas por **cada nodo para cada canal**. Las comisiones consisten en 2 elementos:

- "**Tarifa de base**": una cantidad fija por canal, normalmente es **1 sat** por defecto, pero esta tarifa de base es personalizable.
- "**Tarifa variable**": un porcentaje del monto transferido, calculado en **partes por millón (ppm)**. Por defecto, es **1 ppm** (1 sat por millón de satoshis transferidos), pero también puede ajustarse.
   Las tarifas por transferencia realizada varían dependiendo de la dirección a la que se realice la transferencia. Por ejemplo, para una transferencia de Alice a Suzie, se aplican las tarifas de Alice. Inversamente, de Suzie a Alice, se fijan las tarifas de Suzie.

Por ejemplo, para un canal entre Alice y Suzie, podríamos tener:

- **Alice**: tarifa de base de 1 sat y 1 ppm por las tarifas variables.
- **Suzie**: tarifa de base de 0.5 sat y 10 ppm por las tarifas variables.

![LNP201](assets/en/42.webp)

Para entender mejor cómo funcionan las tarifas, analicemos la misma Lightning Network que antes, pero ahora con las siguientes honorarios de enrutamiento:

- Canal **Alice - Suzie**: tarifa base de 1 satoshi y 1 ppm (partes por millón) para Alice.
- Canal **Suzie - Carol**: tarifa base de 0 satoshi y 200 ppm para Suzie.
- Canal **Carol - Bob**: tarifa base de 1 satoshi y 1 ppm para Suzie 2.
  ![LNP201](assets/en/43.webp)

Para el mismo pago de **40,000 satoshis** a Bob, Alice tendrá que enviar un poco más, ya que cada nodo intermediario deducirá sus tarifas:

- **Carol** descuenta 1.04 satoshis en el canal con Bob:
  $$ f*{\text{Carol-Bob}} = \text{tarifa base} + \left(\frac{\text{ppm} \times \text{monto}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** deduce 8 satoshis como honorarios en el canal con Carol:
  $$ f*{\text{Suzie-Carol}} = \text{tarifa base} + \left(\frac{\text{ppm} \times \text{monto}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Las comisiones totales para este pago en esascienden a **9.04 satoshis**. Así, Alice debe enviar **40,009.04 satoshis**, para que Bob reciba exactamente **40,000 satoshis**.

![LNP201](assets/en/44.webp)

por lo tanto, la liquidez queda actualizada de la siguiente manera:

![LNP201](assets/en/45.webp)

### Enrutamiento Cebolla (Onion Routing)

Para enrutar un pago del emisor al receptor, la Lightning Network utiliza un método llamado "**enrutamiento cebolla**" (onion Routing), a diferencia del enrutamiento de datos clásicos, en el que cada enrutador decide la dirección de los datos, basándose en su destino. El enrutamiento cebolla funciona de un modo distinto:

- **El nodo emisor calcula toda la ruta**: Alice, por ejemplo, determina que su pago debe pasar por Suzie y Carol antes de llegar a Bob.
- **Cada nodo intermedio solamente conoce a su vecino inmediato**: Suzie sólo sabe que recibió fondos de Alice y que ella debe transferírselos a Carol. Sin embargo, Suzie no sabe si Alice es el nodo fuente o un nodo intermedio, y tampoco sabe si Carol es el nodo receptor o es, simplemente, otro nodo intermedio (mediador). Este principio también se aplica a Carol y a todos los demás nodos de la ruta. El enrutamiento cebolla (Onion Routing) preserva el anonimato de las transacciones, al enmascarar la identidad del remitente y del receptor final. Asegurar que el nodo transmisor pueda calcular una ruta completa hasta el receptor final en el Onion Routing, el nodo transmisor debe mantener un **gráfico de red** para saber la topología de la red y, así determinar las posibles rutas.
  **¿Qué debes recordar del contenido de este capítulo?**

- En la Lightning Network, los pagos pueden enrutarse entre nodos conectados indirectamente, a través de canales intermedios. Cada uno de estos nodos intermedios facilita la transmisión de liquidez.
- Los nodos intermedios son remunerados con una comisión por su actividad, consistente en tarifas fijas y tarifas variables.
- El Onion Routing permite al nodo transmisor calcular el itinerario de la ruta completa, sin que los nodos intermedios distingan la fuente/origen o el receptor final en la ruta.

En este capítulo, hemos explorado el enrutamiento de pagos en la Lightning Network y surge una pregunta: ¿qué obstáculos encuentran los nodos intermedios acepten un pago entrante, sin reenviarlo al siguiente destino; con el objetivo de interceptar la transacción? Éste es, precisamente, el papel de los HTLCs que estudiaremos en el siguiente capítulo.

## HTLC – Hashed Time Locked Contract ("Contrato bloqueado por tiempo y por una función hash")

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

:::video id=4e2361e0-e859-4459-bef5-79b2fbb03574:::

En este capítulo, descubriremos cómo Lightning permite el tránsito de los pagos a través de nodos intermedios, sin necesidad de depositar ciega confianza en ellos, gracias a los **HTLC** (_Hashed Time-Locked Contracts_ o Contratos bloqueados por tiempo y por una función hash). Estos contratos inteligentes aseguran que cada nodo intermedio únicamente reciba los fondos en su canal de pago, si cumple la condición de reenvíar el pago al destinatario final. De lo contrario, el pago no será validado.

El problema que surge para el enrutamiento de pagos es, por tanto, depositar la confianza necesaria en los nodos intermedios, y que los propios nodos intermedios confíen también entre ellos. Para ilustrar esto, revisemos nuestro ejemplo de la Lightning Network con 3 nodos y 2 canales:

- Alice tiene un canal con Suzie.
- Suzie tiene un canal con Bob.

Alice quiere enviar 40,000 sats a Bob, pero no existe un canal directo con Bob, y Alice no quiere abrir un canal de pagos. Alice busca una ruta y decide que la transacción se lleve por la vía que pasa por el nodo de Suzie.

![LNP201](assets/en/46.webp)

Si Alice envía ingenuamente 40,000 satoshis a Suzie, esperando que Suzie transfiera esta suma a Bob, Suzie podría quedarse con los fondos y no reenviárselos a Bob.

![LNP201](assets/en/47.webp)
Para evitar esta situación, en Lightning Network, usamos HTLCs (Contratos bloqueados por tiempo y por una función hash), que hacen el pago al nodo intermediario condicional, esto es, Suzie debe cumplir ciertas condiciones y requisitos para acceder a los fondos de Alice y para transferírselos a Bob.

### Cómo Funcionan los HTLCs

Un HTLC es un contrato inteligente basado en dos principios:

- **Condición de acceso**: El destinatario debe revelar un secreto para desbloquear el pago que le corresponde.
- **Expiración/ Caducidad del contrato**: Si el pago no se completa en su totalidad dentro de un período definido, el pago se cancela y los fondos regresan al remitente.

Así es como funciona este proceso en nuestro ejemplo con Alice, Suzie y Bob:

![LNP201](assets/en/48.webp)
**Creación del secreto**: Bob genera un secreto aleatorio nombrado como _s_ (imagen previa), y calcula su función hash nombrado como _r_ con la función hash nombrada como _h_. El resultado es:

$$
r = h(s)
$$

Usando una función hash se hace imposible encontrar _s_ conociendo solo _h(s)_, pero si sabemos _s_, es fácil despejar el valor de la funciónhash _h(s)_ en el secreto.

![LNP201](assets/en/49.webp)

**Enviando la solicitud de pago**: Bob envía una **factura** a Alice solicitando un pago. Esta factura incluye la función hash _r_, en particular.

![LNP201](assets/en/50.webp)

**Enviando el pago sujeto a condición**: Alice envía un HTLC de 40,000 satoshis a Suzie. La condición para que Suzie reciba estos fondos es que ella proporcione a Alice un secreto nombrado _s'_ que resuelva la siguiente ecuación:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Traspasar el HTLC al destinatario final**: Suzie, para obtener los 40,000 satoshis de Alice, debe traspasar un HTLC semejante de 40,000 satoshis a Bob, quien tiene la misma condición, esto es, que debe revelar el secreto (nombrado _s'_) a Suzie y que éste satisfaga la ecuación a continuación:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Validación del pago mediante el valor del secreto, que llamamos _s_**: Bob proporciona el valor de la función hash _s_ a Suzie para recibir los 40,000 satoshis que garantiza el HTLC. Con este secreto, Suzie puede entonces desbloquear el HTLC de Alice y obtener los 40,000 satoshis de Alice. En ese momento, el pago es enrutado correctamente hasta Bob.

![LNP201](assets/en/53.webp)
Este proceso evita que Suzie se quede con los fondos de Alice sin completar la transferencia a Bob. Ya que Suzie debe enviar el pago a Bob para obtener el secreto _s_ y así desbloquear el HTLC de Alice. La operación permanece igual que antes, incluso si la ruta incluye varios nodos intermedios: simplemente, es cuestión de repetir los pasos que ha seguido Suzie para cada nodo intermedio. Cada nodo está protegido por las condiciones que requieren los HTLCs, porque desbloquear el último HTLC por el destinatario pone automáticamente en funcionamiento el desbloqueo en cascada de todos los demás HTCL.

### Caducidad de los contratos HTCL y la gestión de problemas:
Si durante el proceso de pago, uno de los nodos intermedios, o el nodo del destinatario, deja de responder, (especialmente en caso de un corte de Internet o de energía), entonces el pago no puede completarse, porque el secreto necesario para desbloquear los HTLCs no se llega a transmitir. Tomando nuestro ejemplo de Alice, Suzie y Bob, este problema ocurre si, por ejemplo, Bob no transmite el secreto _s_ a Suzie. En este caso, todos los HTLCs de la ruta están bloqueados, y los fondos que aseguran los HTCL, también.

![LNP201](assets/en/54.webp)

Para evitar esto, los HTLCs en Lightning Network tienen una caducidad, la cual permite la expiración del HTLC si la operación no se completa después de determinado tiempo. La caducidad del HTCL sigue un orden específico, ya que empieza por el HTLC más cercano al nodo destinatario, y luego se mueve, progresivamente, hacia la entidad emisora de la transacción. En nuestro ejemplo, si Bob nunca entrega el secreto _s_ a Suzie, esto provocaría la expiración del HTLC de Suzie a Bob.

![LNP201](assets/en/55.webp)

El HTLC de Alice hasta Suzie:
![LNP201](assets/en/56.webp)
Si el orden de expiración se invirtiera, Alice recuperaría su pago antes de que Suzie pudiera protegerse de un posible engaño. De hecho, si Bob regresa para reclamar su HTLC, mientras que el de Alice ya ha expirado, Suzie estaría en desventaja. El orden de expiración en cascada de los HTCLs securiza los nodos intermedios para que no sufran pérdidas injustas.

### Representación de HTLCs en las "transacciones de compromiso" (Commitment Transactions)

Las transacciones de compromiso representan los HTLCs de tal modo que, éstos imponen sus mismas condiciones, que se imponen en la Lightning Network. Estas condiciones a cumplir pueden ser transferidas a la tecnología Bitcoin durante la vida útil de un HTLC, en el caso de un cierre forzado del canal. Como recordatorio, las transacciones de compromiso indican el estado actual del canal de pagos entre los dos usuarios y permiten un cierre forzado unilateral en caso de problemas. Con cada nuevo estado del canal, se crean 2 transacciones de compromiso: una transacción para cada parte. Revisemos nuestro ejemplo de Alice, Suzie y Bob, pero examinemos más de cerca qué sucede en el canal entre Alice y Suzie en el momento de creación de un HTLC.

![LNP201](assets/en/57.webp)

Antes del inicio del pago de 40,000 sats entre Alice y Bob, Alice tiene 100,000 sats en su canal de pagos con Suzie, mientras que Suzie tiene 30,000 sats. Sus transacciones de compromiso serían las siguientes:

![LNP201](assets/en/58.webp)

Alice acaba de recibir la factura de Bob, que indica específicamente _r_, la función hash del secreto. De este modo, Alice puede crear un HTLC de 40,000 satoshis con Suzie. Este HTLC está representado en las últimas transacciones de compromiso como una salida con nombre: "**_HTLC Out_**" en el extremo de Alice, mientras que los fondos que salen, entran en el extremo de Suzie, y llevan el nombre: "**_HTLC In_**".

![LNP201](assets/en/59.webp)

Estas salidas asociadas con el HTLC comparten exactamente las mismas condiciones a cumplir:
- Si Suzie puede proporcionar el valor _s_ del secreto, podrá desbloquear de inmediato la salida, y transferirla a su propia dirección bajo su control.
- Si Suzie no tiene en su poder el valor _s_ del secreto, no puede desbloquear la salida y, Alice podrá desbloquearla después de transcurrido el tiempo fijado por el timelock para, a continuación, enviarla a su propia dirección. De esta manera, el timelock (“candado de tiempo”) concede a Suzie un tiempo de reacción, si ésta obtiene el valor _s_.

Estas condiciones aplican solamente si el canal se cierra (es decir, cuando una transacción de compromiso haya sido publicada en la “cadena de bloques”), mientras el HTLC sigue activo todavía en la Lightning Network. Esto significa que el pago entre Alice y Bob aún no se ha completado, y los HTLCs no han expirado aún. Gracias a estas condiciones, Suzie puede recuperar los 40,000 satoshis del HTLC que se le deben por por haber aportado la información del valor _s_. Alice recupera los fondos después de la expiración del timelock, porque si Suzie no conoce _s_, significa que no ha transferido los 40,000 satoshis a Bob, y, por lo tanto, los fondos de Alice no le son debidos.

Además, si el canal de pagos se cierra mientras que varios HTLCs están pendientes, en el canal de pago habrá tantas salidas adicionales como número de HTLCs haya en curso.
Si el canal de pago no está cerrado, a continuación de que el pago haya expirado o cuando el pago se haya completado correctamente en la Lightning Network, se crearán nuevas transacciones de compromiso para el registro del nuevo estado del canal de pago: En su estado no habrá ningún HTLC pendiente. Es decir, el canal de pagos es estable en este momento. Por tanto, las salidas relacionadas con los HTLCs pueden ser eliminadas, de las transacciones de compromiso. 

![LNP201](assets/en/60.webp)

Para terminar, en el caso de un cierre cooperativo del canal de pagos, mientras un HTLC está activo, Alice y Suzie cortan la admisión de nuevos pagos y esperan la solución o expiración/vencimiento de los HTLCs en curso. Esto les permite a Alice y Suzie publicar una transacción de cierre a velocidad del rayo, sin tener que publicar las salidas relacionadas con los HTLCs. Así consiguen reducir el importe de las comisiones y evitan la posible espera ocasionada por un "bloqueo de tiempo" (timelock).

**¿Qué debes recordar de este capítulo?**

Los HTLCs permiten el enrutamiento de pagos, a través de múltiples nodos seguros. Éstos son los puntos clave a recordar:

- Los HTLCs securizan los pagos mediante un secreto (imagen previa) y un tiempo límite de expiración.
- La expiración de los contratos inteligentes HTLCs sigue un orden específico: este orden empieza en el destino y va en dirección al origen, para proteger a cada nodo intermedio.
- Los HTCLs que no hayan sido resueltos ni tampoco áquellos cuyo tiempo no haya expirado todavía, se guardan como salidas con las últimas transacciones de compromiso.

En el próximo capítulo, descubriremos cómo un nodo emisor, que inicia una transacción en la Lightning Network puede encontrar y seleccionar rutas/vías para que su transacción de pago llegue al nodo receptor.

## Encuentra la ruta más eficiente y rápida para el enrutamiento de un pago.

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

:::video id=e84ce4ec-d766-42dc-a58b-277af115b0e2:::

En los capítulos anteriores,entendimos el método para aprovechar los canales de pagos de otros nodos para el enrutamiento de pagos y poder alcanzar otro nodo sin estar conectado directamente a él a través de un canal de pagos. Anteriormente, también abordamos cómo garantizar la seguridad de la transferencia, sin que sea necesario confiar en los nodos intermedios. En este capítulo, nos centraremos en encontrar la ruta más eficiente y rápida disponible para llegar un nodo objetivo (destino).

### El desafío del enrutamiento en la Lightning Network (Decisiones de enrutamiento)

Como hemos visto, en Lightning Network, el nodo que envía el pago es el que debe calcular la ruta completa hasta el destinatario final, porque utilizamos un sistema de enrutamiento tipo cebolla (Onion Routing). Los nodos intermediarios no conocen ni el punto de origen, ni tampoco el destino final. Solamente conocen de qué nodo viene el pago y a qué nodo deben transferirlo a continuación. Esto significa que, el nodo emisor del pago se encarga de mantener la topología local dinámica de la red: los nodos Lightning existentes y los canales entre cada uno y debe tener en cuenta la apertura y cierre de pagos, así como las actualizaciones periódicas de la información del estado de los canales de pago. Buscará la ruta  óptima a través de la Lightning Network.

![LNP201](assets/en/61.webp)
En la topología de la Lightning Network hay un dato esencial para el enrutamiento, que es inaccesible para el nodo emisor. Este dato es la distribución exacta de liquidez/ distribución del saldo en los canales de pago. Cada canal de pago únicamente muestra su **capacidad total**, pero solamente los dos nodos participantes tienen conocimiento de la distribución de los fondos. Esto plantea el reto de conseguir un enrutamiento con eficiencia energética, ya que el éxito del pago depende, sobre todo, de si el importe es inferior a la liquidez más baja de la ruta/vía elegida. Sin embargo, el monto de todos los fondos son desconocidos para el nodo emisor/origen.
![LNP201](assets/en/62.webp)

### Actualización del mapa de red de la Lightning Network

Para mantener el mapa de red actualizado, los nodos de enrutado en la Lightning Network intercambian información en mensajes frecuentes. Para que esta actualización funcione, se utiliza un algoritmo llamado “cotilleo” (“gossip”). “Gossip” es un algoritmo distribuido, utilizado para transmitir la información como lo haría una epidemia o una plaga: es decir, transmite la información entre los nodos (enlaces) de la red de forma simultánea, lo que permite el tránsito de comunicaciones y sincronización del estado global actual a través de los canales. Este intercambio de mensajes entre los nodos se consigue en unos pocos ciclos de comunicaciones. Cada nodo intercambia el mensaje a uno o más nodos vecinos elegidos al azar o no. Éstos, a su vez, transmiten esta información  a otros nodos vecinos y, así sucesivamente, hasta que se alcanza un estado sincronizado entre todos los nodos, a nivel global.

Los 2 mensajes principales que se intercambian entre los nodos de la Lightning Network son:

- "**Notificaciones de canales**": son mensajes que nos anuncian e indican la apertura de un nuevo canal.
- "**Actualizaciones  de los canales**": son mensajes que indican una actualización del estado de un canal. Informan, especialmente, acerca de la evolución de las comisiones, pero no facilitan datos de la distribución de la liquidez. Los nodos de la Lightning Network también monitorizan la blockchain de Bitcoin para encontrar transacciones de cierre de canal. El canal cerrado se elimina del mapa, dado que éste ya no puede utilizarse para el enrutamiento de los pagos.
  
### Enrutamiento de un pago

Tomemos el ejemplo de una pequeña Lightning Network con 7 nodos enlazados: Alice, Bob, 1, 2, 3, 4 y 5. Imagina que Alice quiere enviar una transacción de pago a Bob, pero ésta tiene que transmitirse a través de nodos que intermedian en la transacción de pago.

![LNP201](assets/en/63.webp)

Ésta es la distribución de fondos actual en los canales de pago anteriores:

Esta es la distribución de fondos actual en los canales de pago anteriores:
- **Canal entre Alice y 1**: 250,000 satoshis en el extremo de Alice y 80,000 satoshis en el extremo de 1 (con una capacidad total de 330,000 satoshis).
- ** Canal entre 1 y 2**: 300,000 satoshis en el extremo de 1 y, 200,000 satoshis  en el extremo de 2 (con una capacidad de liquidez total de 500,000 satoshis).
- **Canal entre 2 y 3**: 50,000 satoshis en el extremo de 2 y 60,000 en el extremo de 3 (con una capacidad de liquidez total de 110,000 satoshis).
- **Canal entre 2 y 5**: 90,000 satoshis en el extremo de 2 y 160,000 satoshis en el extremo de 5 (con una capacidad total de 250,000 satoshis).
- ** Canal entre 2 y 4**: 180,000 satoshis en el extremo de 2 y 110,000 satoshis en el extremo de 4 (con una capacidad total de 290,000 satoshis).
- ** Canal entre 4 y 5**: 200,000 satoshis en el extremo de 4 y 10,000 satoshis en el extremo de 5 (capacidad de liquidez total de 210,000 satoshis).
- **Canal entre 3 y Bob**: 50,000 sats en el extremo de 3 y 250,000 satoshis en el extremo de Bob (con una capacidad total de 300,000 satoshis).
- **Channel between 5 and Bob**: 260,000 satoshis en el extremo de 5 y 100,000 satoshis en el extremo de Bob (capacidad de liquidez total de 360,000 satoshis).

![LNP201](assets/en/64.webp)

Para realizar un pago de 100,000 satoshis de Alice hasta Bob, las opciones de enrutamientos del pago en la Lightning Network están limitadas por la liquidez disponible en cada canal de pago. La ruta idónea para Alice, se basa en las distribuciones de liquidez conocidas en esos canales. La secuencia puede ser representada de la siguiente forma:

![LNP201](assets/en/65.webp)

Dado que Alice no es conocedora la posición de balance de la liquidez en cada canal, Alice tiene que estimar la ruta idónea de manera probabilística, teniendo en cuenta los criterios de enrutamiento que vienen a continuación:

- **Probabilidad de éxito del pago**: Un canal de pagos con una posición de balance de liquidez tiene más probabilidades de contener suficiente liquidez. Por ejemplo, el canal entre el nodo 2 y el nodo 3 tiene una posición de balance de 110.000 satoshis, por lo que es improbable encontrar 100.000 satoshis o más, del lado opuesto (nodo 2), aunque sigue siendo viable.
- **Comisiones por el servicio de enrutamiento en cada transacción**: Para elegir la mejor ruta, el nodo emisor también tiene en cuenta las comisiones por enrutamiento, que aplican a cada nodo intermedio (enrutador) y busca minimizar al máximo los costes globales, que conlleva el enrutamiento.
- **Finalización de la vigencia de los HTLCs**:  para prevenir los pagos bloqueados, hay un parámetro que también se tiene que contemplar y éste es el tiempo de expiración de los HTCLs.
- **Número de nodos enrutadores intermediarios**: De manera más general, el nodo emisor busca encontrar una ruta con el menor número posible de nodos para reducir el riesgo de fallo y delimitar las comisiones de enrutamiento por transacción realizada en la Lightning Network. 
  Analizando estos criterios, el nodo emisor puede poner a prueba las rutas más probables para intentar optimizar al máximo la ruta del pago. En nuestro ejemplo, Alice podría clasificar las rutas más efectivas de la siguiente manera:

- `Alice → 1 → 2 → 5 → Bob`, porque es la ruta más corta con la mayor capacidad de liquidez.
- `Alice → 1 → 2 → 4 → 5 → Bob`, porque esta ruta ofrece buena capacidad de liquidez, aunque es una ruta más larga que la primera. 
- `Alice → 1 → 2 → 3 → Bob`, porque esta ruta incluye el canal de transmisión de liquidez `2 → 3`, el cual tiene una capacidad muy limitada. No obstante, es un canal de pago potencialmente utilizable. 

### Realizar un pago a través de la Lightning Network de Bitcoin

Alice decide probar su primera ruta (`Alice → 1 → 2 → 4 → 5 → Bob`), por lo tanto, envía un HTCL de 100.000 satoshis al nodo 1. Este nodo revisa que tiene suficiente liquidez con el nodo 2 y continúa la transmisión. El nodo 2 recibe el HTCL del nodo 1, pero éste se da cuenta de que no tiene fondos suficientes en su canal de pago con el nodo 5 para enrutar un pago de 100.000 satoshis. A continuación, el nodo 2 envía un mensaje de error, contestando al nodo 1. El nodo 1 transmite este mensaje a Alice. Esta opción de ruta ha fallado.

![LNP201](assets/en/66.webp)

Alice trata de utilizar su segunda ruta para realizar el pago: (`Alice → 1 → 2 → 4 → 5 → Bob`). Alice envía un HTCL de 100,000 satoshis al nodo 1, el cual lo transmite al nodo 2, luego pasa al nodo 4, después al nodo 5 y, por último, llega a Bob. En esta ocasión, hay suficiente liquidez, la ruta funciona. Cada nodo desbloquea en cascada su HTCL, usando la imagen proporcionada por Bob, la cual es el secreto _s₎ este último proceso es lo que permite completar con éxito el pago de Alice a Bob. 

![LNP201](assets/en/67.webp)

La lógica de enrutamiento de pagos, que es la búsqueda de una ruta óptima se lleva a cabo como sigue: el nodo emisor comienza por identificar las mejores rutas de direccionamiento, a continuación y después intenta hacer los pagos de manera sucesiva, hasta que encuentra una ruta operativa.

Cabe señalar que Bob puede proporcionar información a Alice en la factura para facilitar el enrutamiento de la transacción. Por ejemplo, el nodo emisor puede precisar, especificar los canales de pago ubicados cerca de él con suficiente capacidad de liquidez o revelar la existencia de canales privados. Estos indicios permiten evitar rutas con menos probabilidades de éxito, e intentar, en primer lugar, las rutas recomendadas por Bob.

**¿Qué debes recordar del contenido de este capítulo?**

- Los nodos mantienen un mapa topológico de la Lightning Network, a través de avisos y el monitoreo del cierre de canales en la blockchain de Bitcoin.
- La búsqueda de una ruta óptima (lógica de enrutamiento de pagos) para un pago es probabilística y depende de muchos criterios.
- Bob puede sugerir información adicional en la factura para ayudar a Alice a optimizar la ruta de pago y ahorrarle el tiempo probando otras rutas con bajas probabilidades de éxito de pago.

En el próximo capítulo, estudiaremos el uso y propósito de las facturas, es decir, aprenderemos cómo atender un pago, además de otras herramientas, utilizadas en la Lightning Network.

# Las herramientas de la Lightning Network

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Factura, LNURL y Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
:::video id=b4707c4e-6b63-496e-9ac8-e748a8c3be94:::
En este capítulo, vamos a examinar más de cerca cómo funcionan las facturas en la Lightning Network, es decir, cómo las solicitudes de pago enviadas por el nodo receptor se transmiten hasta el nodo emisor. El objetivo es entender cómo pagar y recibir pagos en la Lightning Network. También discutiremos 2 alternativas a las facturas típicas, que son: LNURL y Keysend.
![LNP201](assets/en/68.webp)

### Estructura de las facturas en la Lightning Network

Como explicamos en el capítulo que trata de los HTCL´s , el proceso de pago comienza con la creación de una factura por parte del receptor. Para iniciar el pago el beneficiario transmite una factura al pagador por medio de un QR o copiando y pegando. Podemos dividir la factura en 2 partes:

- Primero, encontramos la **parte legible por el ser humano**: para mejorar la experiencia de usuario, esta parte contiene metadatos claramente visible para el usuario.
- La parte del **Payload**: esta sección incluye información para la realización de un pago, es la carga útil. Es la parte esencial de datos que se transmiten dentro de la transmisión del pago. Esta parte va destinada a las máquinas, que procesan el pago.

La típica estructura de una factura comienza con un identificador `ln` que significa “Lightning”, sigue de `bc` para Bitcoin, y, a continuación, se indica el importe de la factura. Un separador `1` distingue la parte legible por seres humanos de la otra parte de datos (payload).

La siguiente factura ilustra un ejemplo de la estructura típica de una factura Lightning:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Podemos dividirla en 2 secciones diferenciadas. Primero, está la parte legible por humanos:

```invoice
lnbc100u
```

Luego encontramos la sección diseñada para el payload (que es el conjunto de datos transmitidos útiles, que se obtienen de excluir cabeceras, metadatos, información de control y otros datos que son enviados para facilitar la entrega del mensaje): 

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Las 2 partes están separadas por un 1. Para facilitar la tarea de copiar y pegar toda la factura haciendo doble click, se ha elegido un separador (1), en lugar de un caracter especial.

En la primera parte, podemos ver que:

- `ln` indica que se trata de una transacción Lightning.
- `bc` señala que la Lightning Network se encuentra en la blockchain de Bitcoin ( y no en la “testnet” o en “Litecoin”)
- `100u` indica el importe a facturar y se expresa en **microbitcoins** (`u` significa "micro"), que equivale  a 10,000 satoshis.

El importe a pagar en los micropagos se expresa en subunidades de Bitcoin:

- **Millibitcoin (indicado como `m`):** Representa una milésima parte de un bitcoin.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Microbitcoin (indicado como `u`):** También llamado "bit", representa una millonésima parte de un bitcoin.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (indicado como `n`):** Representa una milmillonésima parte de un bitcoin.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Picobitcoin (indicado como `p`):** Representa una billonésima parte de un bitcoin. 
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### Cuerpo de una factura Lightning

El “payload” incluye los datos necesarios para transmitir el pago, es la carga útil de datos:

- **El timestamp (la marca de tiempo)**: El “timestamp” es la primera parte del “payload” (parte de datos). El timestamp es el momento de la creación de la factura, expresado en Timestamp Unix (el número de segundos que han transcurrido desde el 1 de enero de 1970).
- **Hashing/Revisando el secreto**: Como vimos en la sección de  HTCL, el nodo receptor tiene que proporcionar el hash de un número (que llamamos “preimage”) y computar su hash para  transmitirlo al nodo emisor.  Esto se utiliza en HTCLs para securizar la transacción. Nos referimos a ello como "_r_". 
- **El secreto en el pago**: El receptor crea otro secreto, pero ahora se transmite al nodo emisor. Se utiliza en el “enrutamiento cebolla” (Onion routing) para evitar que los nodos enrutadores intermedios adivinen si el siguiente nodo es el destinatario final o no. Cada nodo solamente puede ver la información del nodo anterior o del siguiente. Los nodos intermedios no son capaces de identificar la ruta completa o el receptor final que va a recibir el pago. Son rutas ciegas que esconden información para los participantes de la transacción. De este modo, se mantine una forma de privacidad  para el destinatario sin revelar su identidad, respecto al último nodo intermedio de la ruta. Se esconde la parte final del recorrido de una transacción.
- **La clave pública del destinatario**: Indicar al pagador el identificador de la persona a ser pagada.
- **Duración del tiempo de vencimiento**: Es el tiempo máximo para pagar la factura (se ha establecido una hora por defecto).
- **Routing Hints/Indicaciones para el enrutamiento a través de la red**: Es la información adicional facilitada por el destinatario final para yudar al remitente a optimizar la ruta de pago.
- **The Recipient's Public Key** (“clave pública del receptor”): garantiza la integridad de la factura, verificando toda la información. La firma se verifica, usando la clave pública, la cual se facilita en la factura.
- **Firma**:  Garantiza la integridad de la factura al verificar toda la información. La firma se verifica, usando la clave pública, la cual se facilita en la factura.
A continuación, las facturas se codifican en **bech32** que tiene el mismo formato que las direcciones SegWit de Bitcoin (formato que empieza con `bc1`).

### LNURL: Retiro de liquidez 

En una transacción tradicional, como una compra en una tienda, la factura refleja el importe total a pagar. Una vez que se presenta la factura (en forma de QR o cadena de caracteres), el cliente puede escanear el QR y completar la transacción. El pago sigue el proceso tradicional que estudiamos en la sección anterior. Sin embargo, este proceso puede resultar engorroso para el usuario, ya que debe el receptor debe enviarle la información en la factura al emisor.
Para ciertas situaciones, como retirar bitcoins de un servicio online, el proceso tradicional es demasiado engorroso. Por eso, en tales casos, la solución de retiro de bitcoins **LNURL** simplifica este proceso al mostrar un código QR en el display que se escanea en la billetera del destinatario, con el objetivo de crear la factura automáticamente. Después, el servicio online pagará la factura y el usuario simplemente ve un retiro instantáneo.

![LNP201](assets/en/69.webp)

LNURL es un protocolo de comunicación que especifica un conjunto de funcionalidades diseñadas para simplificar las interacciones entre nodos Lightning y clientes, así como con aplicaciones de terceros. Un LNURL es un procedimiento estándar para las interacciones entre un pagador y un beneficiario Lightning. El retiro de liquidez LNURL es, únicamente, un ejemplo entre otras funcionalidades.
Este protocolo se basa en HTTP y permite crear links para varias operaciones, como: una solicitud de pago, un solicitud de retiro de liquidez, junto con otras características, las cuales mejoran la experiencia de usuario. Cada LNURL es una URL codificada en bech32 con el prefijo lnurl , que, una vez es escaneada, desencadena una serie de acciones automáticas en el monedero electrónico (Lightning wallet).
El uso más común de LNURL es iniciar una retirada de liquidez o crear links que contienen el estado de los pagos.
Por ejemplo, la característica LNURL-withdraw (LUD-03) permite retirar fondos de un servicio, escaneando un QR, sin la necesidad de generar una factura manualmente. LNURL-auth (LUD-04) te permite iniciar sesión en servicios online, usando la clave privada del monedero electrónico (wallet), en lugar de usar una contraseña.

### Envío de un pago Lightning sin crear una factura: Keysend 

Keysend es una función característica dentro de la Lightning Network que permite a los usuarios mandar pagos a la clave pública de otro nodo directamente, sin requerir una factura.
Es interesante es la transferencia de fondos , sin haber recibido una factura previamente y es lo que conocemos como “Keysend”. Este protocolo permite enviar fondos, añadiendo una PREIMAGE en los datos de pago cifrado, accesible solamente por el destinatario de los fondos. Esta PREIMAGE desbloquea el HTCL del destinatario, recuperando así los fondos, sin haber generado una factura de antemano.

Para simplificar, en este protocolo, es el emisor, quien genera el secreto utilizado en los HTCL´s, en lugar del destinatario. En la práctica, esto permite al remitente efectuar el pago sin haber tenido que interactuar prácticamente con el destinatario final previamente. 

![LNP201](assets/en/70.webp)

**¿Qué debes recordar de este capítulo?**

- Una factura Lightning es una solicitud de pago, que consta de una parte legible por el ser humano y una parte de datos (información) dirigidos a la máquina.
- La factura está codificada en **bech32**, con un separador `1` para facilitar su copia y, otra parte de datos, que contiene toda la información necesaria para el proceso del pago.
- Existen otros procesos de pago en Lightning, en particular, **LNURL-Withdraw** para facilitar el retiro de fondos, y también para el **Keysend**, usado para las transferencias directas sin factura.

En el siguiente capítulo, analizaremos cómo un operador de nodos puede gestionar la liquidez en sus canales, y no ser bloqueado y poder enviar y recibir pagos a través de la Lightning Network.

## Gestión o manejo de liquidez

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

:::video id=a2ee69ae-e1e9-46f5-b95a-91e8c1a0aee6:::

En este capítulo, exploraremos estrategias para gestionar efectivamente la liquidez en la Red Lightning. La gestión de la liquidez varía dependiendo del tipo de usuario y contexto. Veremos los principios principales y las técnicas existentes para entender mejor cómo optimizar esta gestión.

### Necesidades de Liquidez

Existen tres perfiles principales de usuarios en Lightning, cada uno con necesidades específicas de liquidez:

- **El Pagador**: Es quien realiza pagos. Necesitan liquidez saliente para poder transferir fondos a otros usuarios. Por ejemplo, esto podría ser un consumidor.
- **El Vendedor (o Beneficiario)**: Es quien recibe pagos. Necesitan liquidez entrante para poder aceptar pagos en su nodo. Por ejemplo, esto podría ser un negocio o una tienda en línea.
- **El Enrutador**: Un nodo intermediario, a menudo especializado en el enrutamiento de pagos, que debe optimizar su liquidez en cada canal para enrutador tantos pagos como sea posible y ganar comisiones.

Estos perfiles obviamente no son fijos; un usuario puede cambiar entre pagador y beneficiario dependiendo de las transacciones. Por ejemplo, Bob podría recibir su salario en Lightning de su empleador, colocándolo en la posición de un "vendedor" que requiere liquidez entrante. Posteriormente, si quiere usar su salario para comprar comida, se convierte en un "pagador" y debe entonces tener liquidez saliente.

Para entender mejor, tomemos el ejemplo de una red simple compuesta por tres nodos: el comprador (Alice), el enrutador (Suzie) y el vendedor (Bob).

![LNP201](assets/en/71.webp)

Imagina que el comprador quiere enviar 30,000 sats al vendedor y que el pago pasa por el nodo del enrutador. Cada parte debe entonces tener una cantidad mínima de liquidez en la dirección del pago:

- El pagador debe tener al menos 30,000 satoshis de su lado del canal con el enrutador.
- El vendedor debe tener un canal donde 30,000 satoshis estén del lado opuesto para poder recibirlos.
- El enrutador debe tener 30,000 satoshis del lado del pagador en su canal, y también 30,000 satoshis de su lado en el canal con el vendedor, para poder enrutador el pago.

![LNP201](assets/en/72.webp)

### Estrategias de Gestión de Liquidez

Los pagadores deben asegurarse de mantener suficiente liquidez de su lado de los canales para garantizar la liquidez saliente. Esto resulta ser relativamente simple, ya que es suficiente abrir nuevos canales Lightning para tener esta liquidez. De hecho, los fondos iniciales bloqueados en el multisig on-chain están completamente del lado del pagador en el canal Lightning al inicio. La capacidad de pago está así asegurada mientras se abran canales con fondos suficientes. Cuando la liquidez saliente se agota, es suficiente abrir nuevos canales.
Por otro lado, para el vendedor, la tarea es más compleja. Para poder recibir pagos, deben tener liquidez del lado opuesto de sus canales. Por lo tanto, abrir un canal no es suficiente: también deben realizar un pago en este canal para mover la liquidez al otro lado antes de que puedan recibir pagos ellos mismos. Para ciertos perfiles de usuarios de Lightning, como los comerciantes, existe una clara desproporción entre lo que su nodo envía y lo que recibe, ya que el objetivo de un negocio es principalmente recaudar más de lo que gasta, con el fin de generar una ganancia. Afortunadamente, para estos usuarios con necesidades específicas de liquidez entrante, existen varias soluciones:

- **Atraer canales**: El comerciante se beneficia de una ventaja debido al volumen de pagos entrantes esperados en su nodo. Teniendo esto en cuenta, pueden intentar atraer a nodos enrutadores que buscan ingresos de las comisiones por transacción y que podrían abrir canales hacia ellos, esperando enrutador sus pagos y cobrar las comisiones asociadas.
- **Movimiento de liquidez**: El vendedor también puede abrir un canal y transferir parte de los fondos al lado opuesto realizando pagos ficticios a otro nodo, el cual devolverá el dinero de otra manera. Veremos en la próxima parte cómo llevar a cabo esta operación.
- **Apertura triangular**: Existen plataformas para nodos que desean abrir canales de manera colaborativa, permitiendo a cada uno beneficiarse de liquidez entrante y saliente inmediata. Por ejemplo, [LightningNetwork+](https://lightningnetwork.plus/) ofrece este servicio. Si Alice, Bob y Suzie quieren abrir un canal con 100,000 sats, pueden acordarlo en esta plataforma para que Alice abra un canal hacia Bob, Bob hacia Suzie y Suzie hacia Alice. De esta manera, cada uno tiene 100,000 sats de liquidez saliente y 100,000 sats de liquidez entrante, habiendo bloqueado solo 100,000 sats.

![LNP201](assets/en/73.webp)

- **Comprar canales**: También existen servicios para alquilar canales de Lightning para obtener liquidez entrante, como [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) o [Lightning Labs Pool](https://lightning.engineering/pool/). Por ejemplo, Alice puede comprar un canal de un millón de satoshis hacia su nodo para poder recibir pagos.

![LNP201](assets/en/74.webp)

Finalmente, para los routers, cuyo objetivo es maximizar el número de pagos procesados y las comisiones recogidas, deben:

- Abrir canales bien financiados con nodos estratégicos.
- Ajustar regularmente la distribución de fondos en los canales según las necesidades de la red.

### El Servicio Loop Out

El servicio [Loop Out](https://lightning.engineering/loop/), ofrecido por Lightning Labs, permite mover la liquidez al lado opuesto del canal mientras se recuperan los fondos en la blockchain de Bitcoin. Por ejemplo, Alice envía 1 millón de satoshis a través de Lightning a un nodo loop, el cual luego le devuelve esos fondos en bitcoins en cadena. Esto equilibra su canal con 1 millón de satoshis en cada lado, optimizando su capacidad para recibir pagos.

![LNP201](assets/en/75.webp)

Por lo tanto, este servicio permite la liquidez entrante mientras se recuperan los bitcoins en cadena, lo que ayuda a limitar la inmovilización de efectivo necesaria para aceptar pagos con Lightning.

**¿Qué debes recordar de este capítulo?**

- Para enviar pagos en Lightning, debes tener suficiente liquidez de tu lado en tus canales. Para aumentar esta capacidad de envío, simplemente abre nuevos canales.
- Para recibir pagos, necesitas tener liquidez del lado opuesto en tus canales. Aumentar esta capacidad de recepción es más complejo, ya que requiere que otros abran canales hacia ti, o hacer pagos (ficticios o reales) para mover la liquidez al otro lado.
- Mantener la liquidez donde se desea puede ser aún más desafiante dependiendo del uso de los canales. Por eso existen herramientas y servicios para ayudar a equilibrar los canales según se desee.

En el próximo capítulo, propongo revisar los conceptos más importantes de esta formación.

# Ir Más Allá

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Resumen de la formación


<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

:::video id=102fd1db-1730-4f18-8f16-4c31b4431ba0:::
En este capítulo final que marca el fin del entrenamiento LNP201, propongo revisar los conceptos importantes que hemos cubierto juntos.
El objetivo de este entrenamiento era proporcionarte una comprensión comprensiva y técnica de la Red Lightning. Descubrimos cómo la Red Lightning depende de la blockchain de Bitcoin para realizar transacciones fuera de la cadena, mientras retiene las características fundamentales de Bitcoin, notablemente la ausencia de la necesidad de confiar en otros nodos.

### Canales de Pago

En los capítulos iniciales, exploramos cómo dos partes, al abrir un canal de pago, pueden realizar transacciones fuera de la blockchain de Bitcoin. Aquí están los pasos cubiertos:

- **Apertura del Canal**: La creación del canal se realiza a través de una transacción de Bitcoin que bloquea los fondos en una dirección multisignatura 2/2. Este depósito representa el canal Lightning en la blockchain.

![LNP201](assets/en/76.webp) 2. **Transacciones en el Canal**: En este canal, entonces es posible llevar a cabo numerosas transacciones sin tener que publicarlas en la blockchain. Cada transacción Lightning crea un nuevo estado del canal reflejado en una transacción de compromiso.
![LNP201](assets/en/77.webp)

- **Aseguramiento y Cierre**: Los participantes se comprometen con el nuevo estado del canal intercambiando llaves de revocación para asegurar los fondos y prevenir cualquier engaño. Ambas partes pueden cerrar el canal cooperativamente haciendo una nueva transacción en la blockchain de Bitcoin, o como último recurso a través de un cierre forzado. Esta última opción, aunque menos eficiente porque es más larga y a veces mal evaluada en términos de comisiones, aún permite la recuperación de fondos. En caso de engaño, la víctima puede castigar al tramposo recuperando todos los fondos del canal en la blockchain.

![LNP201](assets/en/78.webp)

### La Red de Canales

Después de estudiar canales aislados, extendimos nuestro análisis a la red de canales:

- **Enrutamiento**: Cuando dos partes no están conectadas directamente por un canal, la red permite el enrutamiento a través de nodos intermediarios. Los pagos entonces transitan de un nodo a otro.

![LNP201](assets/en/79.webp)

- **HTLCs**: Los pagos que transitan a través de nodos intermediarios están asegurados por "_Hash Time-Locked Contracts_" (HTLC), que permiten que los fondos estén bloqueados hasta que el pago se complete de extremo a extremo.

![LNP201](assets/en/80.webp)

- **Enrutamiento Onion**: Para asegurar la confidencialidad del pago, el enrutamiento onion enmascara el destino final a los nodos intermediarios. El nodo emisor debe, por lo tanto, calcular toda la ruta, pero en ausencia de información completa sobre la liquidez de los canales, procede a través de pruebas sucesivas para enrutamiento del pago.

![LNP201](assets/en/81.webp)

### Gestión de Liquidez

Hemos visto que la gestión de liquidez es un desafío en Lightning para asegurar el flujo suave de pagos. Enviar pagos es relativamente simple: solo requiere abrir un canal. Sin embargo, recibir pagos requiere tener liquidez en el lado opuesto de los canales propios. Aquí algunas estrategias discutidas:

- **Atraer Canales**: Alentando a otros nodos a abrir canales hacia uno mismo, un usuario obtiene liquidez entrante.

- **Mover Liquidez**: Enviando pagos a otros canales, la liquidez se mueve al lado opuesto.

![LNP201](assets/en/82.webp)

- **Usar Servicios como Loop y Pool**: Estos servicios permiten reequilibrar o comprar canales con liquidez en el lado opuesto.
  ![LNP201](assets/en/83.webp)
- **Aperturas Colaborativas**: También hay plataformas disponibles para conectarse para realizar aperturas triangulares y tener liquidez entrante.

![LNP201](assets/en/84.webp)

# Sección final

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Reseñas & Valoraciones

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusión

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
<isCourseConclusion>true</isCourseConclusion>
