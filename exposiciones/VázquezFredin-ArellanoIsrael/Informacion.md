<h1 align=center>Control de acceso a recursos para diferentes usuarios</h1>

<p align=justify>
A lo largo de la historia se ha pronunciado que uno de los sistemas operativos más usados por personas que programan y por aquellas totalmente ajenas a este mundo es Windows. Se ha observado a lo largo de la historia como es que Windows ha crecido y mantenido en el mercado, pero un factor importante además de sus funcionalidades es la manera de que protege los recursos del sistema.<br><br>
Durante el crecimiento de la computación y el desarrollo de la tecnología siempre se ha tenido otros peligros por encima de la falta de compatibilidad, precios o algún derivado de las competencias o limitaciones de las máquinas, y es la existencia de la vulnerabilidad de los equipos hacía ataques externos con el principal objetivo de dañar y robar información. <br><br>
Es por ello mismo que actualmente la seguridad de los sistemas operativos resulta esencial en el mundo construido actualmente. Si observamos desde la premisa que un sistema operativo permite a sus usuarios realizar diferentes acciones se puede comprender que en realidad estas diferentes acciones vienen derivadas del acceso de diferentes recursos que tiene el sistema. Debido a esto, resulta importante que el acceso a recursos importantes, como archivos, carpetas y configuraciones del sistema sean reguladas y tengan un control de acceso y permisos con el fin de garantizar que solo los usuarios autorizados puedan acceder a tales recursos importantes. <br><br>
De esta manera, se estará abordando la exposición actual en donde vamos explorar los mecanismos de control de acceso y permisos usados en el sistema operativo Windows, además de mostrar cómo es que estos mecanismos son utilizados para garantizar la seguridad del sistema.<br><br>
<div align="center">
<h3>¡Comencemos!</h3>
</div>
<div align="justify">
<br><br>
Para la compresión del tema, se tiene que entender la forma en que nosotros podemos interaccionar con la computadora para realizar acciones, y es que esta interacción con la computadora simplemente se está resumiendo en acceder a determinados datos, aplicaciones y recursos, además de en qué circunstancias. <br><br>
Esta forma de realizar las acciones para comunicarnos con los recursos se hace por medio del sistema operativo del dispositivo. El sistema operativo funciona como un  intermediario entre el usuario y el hardware del dispositivo (en este caso de una computadora), tal que se estará traduciendo las instrucciones del usuario en un lenguaje que el hardware pueda entender, y esto a su vez se estará haciendo por medio de controladores de dispositivo que estarán actuando como intermediarios entre el sistema operativo y los dispositivos del hardware.<br><br>
Completando la información dada por palabras del académico José Fabián Romo Zamudio (Jefe del Departamento de Tecnologías Emergentes). Un sistema operativo es finalmente un conjunto de programas con el propósito de administrar los recursos de la computadora, siendo el hardware y el software que lo compone. El sistema operativo toma el control del hardware como procesador, memoria (RAM), dispositivos de almacenamiento y periféricos. Tal que estará permitiendo observar una interfaz para interactuar con ellos desde el lado del usuario, por ende al momento que el usuario haga una acción como abrir determinado documento, modificar un lugar u otra cosa, se estarán enviando las señales pertinentes para el procesamiento de estas instrucciones (en el procesador central) y el que estará interpretando estas señales para hacerlas llegar a la computadora es el sistema operativo. Por ello mismo el sistema operativo estará residiendo en el nivel más elemental dentro de una computadora.<br><a href="https://www.youtube.com/watch?v=JJM3riqBKec">Fuente</a><br><br>
Extra: la mayoría de los sistemas operativos son denominados DOS (Disk operating system – Sistema operativo almacenado en disco). <br><br>
A partir de esta información es que podemos empezar a deducir la importancia de mantener un control en el acceso a estos recursos, es simplemente necesario mantener este control de acceso a los recursos de una computadora para proteger la información y los recursos de accesos no autorizados.
De una computadora podemos acceder a gran cantidad de información, ejemplos:<br>
<ul>
<li>Archivos</li>
<li>Carpetas programas </li>
<li>Configuraciones del sistema</li>
</ul>

Por ende, al tener esta información en mano no autorizadas se tiene directamente el riesgo de divulgación de información confidencial o alteración de la misma. Como puede llegar a ser borrar accidentalmente archivos o hacer cambios en la configuración del sistema.
Esta es la clave del control de acceso, nos va asegurar (en lo mayor posible) que solo los usuarios autorizados tengan acceso a ciertos recursos, protegiéndolos de usuarios no autorizados, garantizando la integridad y su disponibilidad. <br>
Ahora, podemos comenzar…
<br><hr><br>
<h2>¿Qué es el control de acceso?</h2>
Es un elemento que va a determinar quién tiene permiso para acceder a determinados datos, aplicaciones y recursos. De forma que las directivas de control de acceso van a depender de técnicas, las cuales son:<br>
<ul>
<li>Autenticación </li>
<li>Autorización</li>
</ul>
<br><hr>
Directiva de control de acceso: conjunto de reglas que definen los permisos de acceso a los recursos, estas reglan determinan quiénes tienen acceso a qué recursos y cómo se les concede ese acceso. 
<hr><br>
Dichas técnicas van a permitir a las organizaciones verificar el nivel adecuado de acceso a los elementos a los usuarios.
<br><br>
<h3>Valor del control de acceso</h3><br>
En esta instancia podemos presentar que el objetivo del control de acceso es evitar que la información confidencial caiga en manos de infiltrados, los ataques a estos tipos de datos generan consecuencias severas como la filtración de propiedad intelectual. Llegando a exponer información personal de clientes, empleados o perder fondos corporativos.
<br><br>
Tal vez en este punto vale la pena mencionar lo que posiblemente sucede con las filtraciones que hacen de diferentes aplicaciones como las que ocurren con videojuegos.
Será por esto que se reconoce la necesidad de gobernar cómo y cuándo se tiene acceso a los datos.<br><br>
En funcionamiento del control de acceso implica la identificación de un usuario basándose en sus credenciales y luego autorizar el nivel de acceso apropiado. Las credenciales de usuario lo podemos entender a primera instancia como un nombre de usuario y la contraseña que lo acompaña, o cualquier forma de método de autenticación para acceder a un recurso del equipo, y de forma redundante tiene como función de gestionar el acceso a recursos. <br><br>
Pongamos como ejemplo lo siguiente:<br>
Las contraseñas, Los PIN o tokens de seguridad son precisamente credenciales para identificar y autenticar a un usuario. Para que una vez autenticado el usuario se les conceda permisos, y esto lo hacen las directivas de control.<br><br><hr>
Identificar vs autenticar: (poner diferencias)
<hr><br>

Lo anterior nos ayudará a poder continuar con la exploración del control de acceso, retomando una palabra que nos interesa y fue mencionada hace un momento… ¡Que lo vamos comentar de forma inmediata!<br><br>
Para este punto ya se entendió que el control de acceso es el proceso de autorización de usuarios para acceder a recursos en la red o de la computadora. Ahora, ya enfocándonos en Windows se va abarcar que los equipos con una versión compatible de Windows pueden controlar el uso de los recursos del sistema y de la red y esto mismo lo hará por medio de los mecanismos:<br>
<ul>
<li>Autenticación </li>
<li>Autorización</li>
</ul>
Windows lo que hace es utilizar tecnologías de control de acceso y autorización integradas para determinar si un usuario autenticado tiene los permisos correctos para acceder a un recurso. <br><br>
<h2>Autenticación</h2>
La autenticación es el proceso por el que sistema podrá validar la información de un usuario.
Se hará esto de la siguiente manera, el nombre de y la contraseña de un usuario se van a comparar con una lista autorizada y existe coincidencia se va a conceder el acceso en la medida que la lista de permisos lo específica para ese usuario.<br><br>
<ul>
<li>Tecnologías de autenticación que usa Microsoft</li>
<li>Autenticación de LSA</li>
<li>Administración de credenciales</li>
<li>Autenticación de tarjeta inteligente </li>
<li>Proveedor de red</li>
<li>Interfaz del proveedor de soporte técnico de seguridad</li>
</ul>
Estas mismas son para uso de por parte de desarrolladores de aplicaciones basadas en el servidor de Windows para autenticar a los clientes.<br><br>
<hr>
Lista autorizada: (poner información)
<hr><br>
Ahora, adentrándonos a esto veremos más acerca de la autenticación y será en diferentes puntos.
<br><br>
<h3>Administración de credenciales (como nombres de usuario y contraseñas).</h3>
Windows tiene diferentes funciones para la administración de credenciales, entre ellas está la API credentials Management o las funciones de interfaz de usuario de administración de credenciales. <br><br>
Objetivo de estas funciones: solicitar información de la cuenta que se usará en lugar de las credenciales al iniciar sesión.
En este caso vamos a explorar credentials Management API, este va a permitir a los usuarios almacenar credenciales relevantes para otros sistemas y sitios web. Y este va a funcionar con dos tipos de credenciales:<br>
<ul>
<li>Credenciales de dominio</li>
<li>Credenciales genéricas</li>
</ul><br>
<h3>Credenciales del dominio</h3>
El sistema operativo usa estas credenciales para autenticar la autoridad de seguridad local (LSA). Estas credenciales establecen para un usuario cuando un paquete de seguridad autentica los datos de inicio de sesión dado por el usuario, se almacena en caché estas credenciales tal que nos dará la facilidad que un único inicio sesión proporcione al usuario acceso a muchos recursos diferentes. <br><br>
Entonces, la administración de credenciales genera un mecanismo para que aplicaciones pidan a un usuario las credenciales de dominio, y esto va a suceder hasta después de que el usuario inicie sesión y el sistema operativo pueda autenticar la información proporcionada por el usuario.<br><br>
Es importante mencionar que la contraseña en estas credenciales, está protegida por el sistema operativo. Será únicamente el código que se ejecuta en proceso con LSA puede leer y escribir.<br><br>
<h3>Credenciales genéricas</h3>
Estas se definen y autentican mediante aplicaciones que administran la autorización y la seguridad directamente en lugar de delegar estas tareas en el sistema operativo.
Las aplicaciones lo que harán es usar funciones de administración de credenciales para solicitar a los usuarios información de credenciales, genéricas y definidas por la aplicación. Tal que la información especificada por el usuario se devuelve a la aplicación para la autenticación.<br><br>
Una vez cubierto la administración de credenciales, vamos a explorar sobre la autenticación que ocurre sobre la autoridad de seguridad local.
<br><br>
<h3>Autenticación LSA</h3>
Puede sonar un poco raro esta definición, pero simplemente podemos entenderlo como partes que las aplicaciones pueden usar para autenticar e iniciar sesión de los usuarios en el sistema local. Lo que hará es crear y llamar paquetes de autenticación y de seguridad.<br><br>
Ahora, los paquetes de autenticación implementan protocolos de seguridad, un paquete lo que hará es analizar los datos de inicio de sesión siguiendo las reglas y procedimientos establecidos en un protocolo de seguridad.<br><br>

<h2>Fuentes consultadas</h2>
<ol>
<li>Li, L., Li, Y., Liu, C., & Chen, X. (2015). Research on computer access control technology based on role and rights management. Advances in Intelligent Systems Research, 83, 110-113. DOI: 10.2991/iccsee-15.2015.27</li>
<li>https://www.youtube.com/watch?v=JJM3riqBKec</li>
<li>https://learn.microsoft.com/es-es/windows/win32/secauthn/about-authentication</li>
<li>https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/access-control</li>
<li>https://learn.microsoft.com/es-es/windows-server/identity/ad-fs/ad-fs-overview</li>
<li>https://www.microsoft.com/es-mx/security/business/security-101/what-is-access-control</li>
<li>https://www.profesionalreview.com/2018/11/23/credenciales-windows-10/#:~:text=acerca%20de%20estas-,Que%20son%20las%20credenciales%20Windows%2010,aplicaci%C3%B3n%20o%20una%20p%C3%A1gina%20web.</li>
<li>https://learn.microsoft.com/es-es/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication</li>
</ol>
</div>
</p>