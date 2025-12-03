from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


CARTEL_DATA = [
    {"titulo": "titulo", "imagen": "Imagen1.png"},
    {"titulo": "titulo", "imagen": "Imagen2.jpg"},
    {"titulo": "titulo", "imagen": "imagen3.jpg"},
    {"titulo": "titulo", "imagen": "imagen4.png"},
    {"titulo": "titulo", "imagen": "imagen5.jpg"},
    {"titulo": "titulo", "imagen": "imagen6.png"},
    {"titulo": "titulo", "imagen": "imagen7.jpg"},
    {"titulo": "titulo", "imagen": "imagen8.jpg"},
    {"titulo": "titulo", "imagen": "imagen9.jpg"},
    {"titulo": "titulo", "imagen": "imagen10.jpg"},
    {"titulo": "titulo", "imagen": "imagen11.jpg"},
    {"titulo": "titulo", "imagen": "imagen13.jpg"},
    {"titulo": "titulo", "imagen": "imagen14.jpg"},
    {"titulo": "titulo", "imagen": "imagen15.jpg"},
    {"titulo": "titulo", "imagen": "imagen16.png"},
    {"titulo": "titulo", "imagen": "imagen17.jpg"},
    {"titulo": "titulo", "imagen": "imagen18.jpg"},
    {"titulo": "titulo", "imagen": "imagen19.jpg"},
    {"titulo": "titulo", "imagen": "imagen20.png"},
    {"titulo": "titulo", "imagen": "imagen21.jpg"},
    {"titulo": "titulo", "imagen": "imagen22.png"},
    {"titulo": "titulo", "imagen": "imagen23.jpg"},
    {"titulo": "titulo", "imagen": "imagen24.jpg"},
    {"titulo": "titulo", "imagen": "imagen25.jpg"},
    {"titulo": "titulo", "imagen": "imagen26.jpg"},
    {"titulo": "titulo", "imagen": "imagen27.jpg"},
    {"titulo": "titulo", "imagen": "imagen28.jpg"},
    {"titulo": "titulo", "imagen": "imagen29.jpg"},
    {"titulo": "titulo", "imagen": "imagen30.jpg"},
    {"titulo": "titulo", "imagen": "imagen31.jpg"},
    {"titulo": "titulo", "imagen": "imagen32.jpg"},
    {"titulo": "titulo", "imagen": "imagen33.jpg"},
    {"titulo": "titulo", "imagen": "imagen34.jpg"},
    {"titulo": "titulo", "imagen": "imagen35.png"},
    {"titulo": "titulo", "imagen": "imagen36.jpg"},
    {"titulo": "titulo", "imagen": "imagen37.jpg"},
    {"titulo": "titulo", "imagen": "imagen38.jpg"},
    {"titulo": "titulo", "imagen": "imagen39.png"},
    {"titulo": "titulo", "imagen": "imagen40.jpg"},
    {"titulo": "titulo", "imagen": "imagen41.jpg"},
    {"titulo": "titulo", "imagen": "imagen42.jpg"},
    {"titulo": "titulo", "imagen": "imagen43.jpg"},
    {"titulo": "titulo", "imagen": "imagen44.jpg"},
    {"titulo": "titulo", "imagen": "imagen45.jpg"},
    {"titulo": "titulo", "imagen": "imagen46.jpg"},
    {"titulo": "titulo", "imagen": "imagen47.jpg"},
    {"titulo": "titulo", "imagen": "imagen48.png"},
    {"titulo": "titulo", "imagen": "imagen49.jpg"},
    {"titulo": "titulo", "imagen": "imagen50.png"},
    {"titulo": "titulo", "imagen": "imagen51.jpg"},
    {"titulo": "titulo", "imagen": "imagen52.png"},
    {"titulo": "titulo", "imagen": "imagen53.jpg"},
    {"titulo": "titulo", "imagen": "imagen54.jpg"},
    {"titulo": "titulo", "imagen": "imagen55.jpg"},
    {"titulo": "titulo", "imagen": "imagen56.jpg"},
    {"titulo": "titulo", "imagen": "imagen57.jpg"},
    {"titulo": "titulo", "imagen": "imagen58.jpg"},
    {"titulo": "titulo", "imagen": "imagen59.png"},
    {"titulo": "titulo", "imagen": "imagen60.jpg"},
    {"titulo": "titulo", "imagen": "imagen61.jpg"},
]

PODCASTS = [
    {"titulo": "Entrevista 1",     "duracion": "02:44", "fecha": "01 diciembre 2025", "archivo": "Audio1.mp3"},
    {"titulo": "Entrevista 2",     "duracion": "01:25", "fecha": "01 diciembre 2025", "archivo": "Audio3.mp3"},
    {"titulo": "Entrevista 3",     "duracion": "01:21", "fecha": "01 diciembre 2025", "archivo": "Audio4.mp3"},
    {"titulo": "Entrevista 4",     "duracion": "01:35", "fecha": "01 diciembre 2025", "archivo": "Audio5.mp3"},
    {"titulo": "Entrevista 5",     "duracion": "01:02", "fecha": "01 diciembre 2025", "archivo": "Audio6.mp3"},
    {"titulo": "Entrevista 6",     "duracion": "02:14", "fecha": "01 diciembre 2025", "archivo": "Audio7.mp3"},
    {"titulo": "Entrevista 7",     "duracion": "02:09", "fecha": "01 diciembre 2025", "archivo": "Audio8.mp3"},
    {"titulo": "Entrevista 8",     "duracion": "01:12", "fecha": "01 diciembre 2025", "archivo": "Audio9.mp3"}
]

ENFERMEDADES = [
    {
        "nombre": "ESQUIZOFRENIA",
        "descripcion": "La esquizofrenia es un trastorno mental grave que afecta la forma en que una persona piensa, siente y se comporta, haciendo que sea difícil diferenciar la realidad de las percepciones distorsionadas",
        "sintomas": "Pensamientos delirantes (ideas erróneas fijas) y alucinaciones (oír o ver cosas que no existen), junto con habla y pensamiento desorganizados",
        
    },
    {
        "nombre": "Trastorno de Ansiedad Generalizada (TAG)",
        "descripcion": "El Trastorno de Ansiedad Generalizada (TAG) es un trastorno mental que se caracteriza por preocupación o ansiedad excesiva y persistente sobre diversas situaciones cotidianas, que resulta difícil de controlar. Los síntomas incluyen tensión muscular, fatiga, irritabilidad, dificultad para concentrarse y problemas para dormir, además de manifestaciones físicas como sudoración o problemas estomacales. El tratamiento más común es una combinación de terapia conversacional (psicoterapia) y medicación, aunque también se puede mejorar con el uso de otros tipos de terapia. ",
        "sintomas": "Preocupación excesiva por problemas cotidianos como la salud, el dinero o el trabajo,Dificultad para controlar los sentimientos de nerviosismo o preocupación,Inquietud o sensación de estar al límite,Irritabilidad,Fatiga,Dificultad para concentrarse o tener la mente en blanco,Problemas para conciliar el sueño o permanecer dormido,Tensión muscular, dolores de cabeza o problemas estomacales,Temblores, sudoración o dificultad para respirar."
    },
    {
        "nombre": "Trastorno de Pánico",
        "descripcion": "El trastorno de pánico es un trastorno de ansiedad caracterizado por ataques de pánico recurrentes e inesperados. Estos ataques son episodios de miedo intenso y repentino que pueden incluir síntomas físicos como taquicardia, temblores, sudoración, y sensación de asfixia o peligro de muerte. A menudo, estos ataques ocurren sin una amenaza real y pueden llevar a las personas a evitar lugares o situaciones temiendo que vuelvan a suceder.  ",
        "sintomas": "Ataques de pánico, Miedo a futuros ataques",
    },
    {
        "nombre": "Fobia Social",
        "descripcion": "La fobia social, o trastorno de ansiedad social, es un miedo intenso y persistente a ser juzgado o evaluado negativamente en situaciones sociales. Se caracteriza por la ansiedad extrema en eventos sociales, lo que lleva a evitar estas situaciones e impacta significativamente la vida diaria, el trabajo y las relaciones. Los síntomas incluyen miedo al ridículo, vergüenza, enrojecimiento, sudoración, temblores y náuseas, y se trata con psicoterapia (como la TCC) y/o medicamentos. ",
        "sintomas": "Ansiedad y pánico en situaciones sociales, Síntomas físicos, Síntomas conductuales, Pensamientos negativos",
    },
    {
        "nombre": "Trastorno de Adaptación",
        "descripcion": "Un trastorno de adaptación es una reacción emocional o de comportamiento exagerada y no saludable ante un evento o cambio estresante en la vida, como una mudanza, un divorcio o la pérdida de un trabajo. Los síntomas, que pueden incluir ansiedad, tristeza, problemas de comportamiento o síntomas físicos, aparecen generalmente dentro de los tres meses posteriores al evento estresante y son más intensos de lo que se esperaría para esa situación. El tratamiento más común es la psicoterapia, como la terapia cognitivo-conductual, y en algunos casos se pueden usar medicamentos para aliviar los síntomas.",
        "sintomas": "Con ansiedad, Con estado de ánimo depresivo, Mixto, Con trastorno del comportam, Con alteraciones mixtas, No especificado",
    },
    {
        "nombre": "Trastorno de Somatización",
        "descripcion": "El trastorno de somatización, también conocido como trastorno de síntomas somáticos, se caracteriza por la presencia de uno o más síntomas físicos que causan gran angustia y/o problemas en la vida diaria, los cuales pueden o no tener una causa médica. El tratamiento principal es la terapia psicológica, a menudo acompañada de una estrecha colaboración entre un médico general y un profesional de la salud mental. Se recomienda un abordaje que incluya psicoeducación, atención médica empática y manejo de la ansiedad y depresión subyacentes.",
        "sintomas": "Síntomas físicos, Preocupación excesiva, Angustia significativa",
    },
    {
        "nombre": "Trastorno de Conversión",
        "descripcion": "El trastorno de conversión es una afección en la que los conflictos o el estrés psicológico se manifiestan como síntomas físicos reales, como parálisis, debilidad, convulsiones o problemas sensoriales, que no tienen una causa neurológica que los explique. El diagnóstico se basa en la exclusión de otras condiciones médicas y la presencia de un factor desencadenante emocional, y el tratamiento incluye terapia psicológica, orientación y educación para ayudar a abordar las causas subyacentes. ",
        "sintomas": "Síntomas motores, Síntomas sensoriales, Convulsiones o desmayos",
    },
    {
        "nombre": "Trastorno de Dolor Crónico",
        "descripcion": "El dolor crónico es un dolor que dura más de tres meses y que puede persistir incluso después de que una lesión se haya curado. No funciona como un sistema de alarma, sino que se convierte en una enfermedad en sí misma, afectando la calidad de vida física y mental de las personas. Puede ser causado por una condición subyacente como la artritis o el cáncer, o puede surgir sin una causa clara. ",
        "sintomas": "Lesiones o enfermedades persistentes, Condiciones médica, Factores psicológicos, Disfunción del sistema nervioso",
    },
    {
        "nombre": "Trastorno de Insomnio",
        "descripcion": "El trastorno de insomnio es un problema común del sueño que dificulta conciliar o mantener el sueño, resultando en un sueño de mala calidad y en sentirse cansado durante el día. Para ser considerado crónico, el problema debe ocurrir al menos tres noches por semana durante tres meses o más",
        "sintomas": "Dificultad para dormir, Sueño no reparador, Impacto durante el día",
    },
    {
        "nombre": "Trastorno de la Personalidad Evitativa",
        "descripcion": "El trastorno de la personalidad por evitación (TPE) es un patrón de inhibición social causado por el miedo al rechazo, la crítica o la humillación. Las personas con este trastorno evitan situaciones sociales e interpersonales, tienen baja autoestima y se sienten inadecuadas o incompetentes. El tratamiento generalmente consiste en psicoterapia (como la terapia cognitivo-conductual), que ayuda a desarrollar estrategias de afrontamiento, y, en algunos casos, medicamentos como ansiolíticos o antidepresivos. ",
        "sintomas": "Miedo al rechazo, Evitación social, Baja autoestima, Aislamiento, Inhibición",
    },
    {
        "nombre": "Trastorno de Hipersomnia",
        "descripcion": "El trastorno de hipersomnia es una condición que provoca somnolencia diurna excesiva, donde la persona se siente constantemente somnolienta y tiene dificultad para mantenerse despierta durante el día, incluso si ha dormido lo suficiente. Se clasifica en hipersomnia primaria (idiopática) o secundaria, y sus síntomas incluyen siestas que no alivian el cansancio, dificultad para despertarse y periodos de confusión o desorientación al despertar. El tratamiento depende de la causa subyacente e puede incluir estimulantes, cambios en el estilo de vida y abordar el trastorno principal.  ",
        "sintomas": "Somnolencia diurna excesiva e irresistible. Dificultad para mantenerse despierto y alerta en situaciones cotidianas. Siestas que no son reparadoras y no alivian la somnolencia. Dificultad para despertarse por la mañana o al final de un largo período de sueño. Confusión, desorientación o falta de coordinación al despertar. Aumento del tiempo de sueño, que puede llegar a las 11-14 horas al día. "
    },
    {
        "nombre": "Trastorno de la Personalidad Narcisista",
        "descripcion": "El trastorno narcisista de la personalidad (TNP) es un trastorno mental caracterizado por un patrón de grandiosidad, necesidad de admiración y falta de empatía. Las personas con TNP tienen un sentido exagerado de autoimportancia, exageran sus logros y talentos, creen ser especiales, necesitan admiración constante, tienen un sentido de derecho y se aprovechan de los demás para sus propios fines. ",
        "sintomas": "•	Sentido de superioridad, •	Fantasías de éxito ilimitado, •	Creen ser únicos, •	Necesidad de admiración, •	Sentido de derecho, •	Explotación interpersonal,•	Falta de empatía, •	Envidia, •	Comportamientos arrogantes y altivos, •	Sensibilidad a la crítica",
    },
    {
        "nombre": "Trastorno de la Personalidad Antisocial",
        "descripcion": "El trastorno antisocial de la personalidad (TAP) es una afección mental caracterizada por un patrón de desprecio y violación de los derechos de los demás, que comienza en la adolescencia o a los 15 años y persiste en la adultez. Las personas con TAP suelen ser manipuladoras, impulsivas, irritables y tienen una marcada falta de remordimiento o culpa. Este comportamiento a menudo resulta en problemas legales, laborales y sociales. ",
        "sintomas": "•	Desprecio por la ley y normas sociales, •	Engaño y manipulación, •	Impulsividad, •	Irritabilidad y agresividad, •	Desprecio imprudente por la seguridad, •	Irresponsabilidad, •	Falta de remordimiento",
    },
    {
        "nombre": "Trastorno de la Personalidad Dependiente",
        "descripcion": "El trastorno de personalidad dependiente es un tipo de trastorno de la personalidad ansioso donde la persona tiene una necesidad excesiva y generalizada de ser cuidada, lo que genera comportamientos sumisos y aferrados. Las personas con este trastorno suelen tener miedo de separarse, les cuesta tomar decisiones, no confían en su propia capacidad y pueden tolerar abusos para mantener una relación. El tratamiento principal es la psicoterapia, que puede complementarse con medicamentos para tratar síntomas de ansiedad o depresión asociados. ",
        "sintomas": "•	Necesidad de cuidado, •	Miedo al abandono, •	Incapacidad para la independencia, •	Sumisión y aferramiento, •	Dificultad para disentir, •	Baja autoconfianza",
    },
    {
        "nombre": "Trastorno de la Personalidad Histriónico",
        "descripcion": "El trastorno histriónico de la personalidad es un trastorno mental que se caracteriza por una búsqueda excesiva de atención y un patrón de comportamiento dramático, emocional y seductor. Las personas con este trastorno necesitan ser el centro de atención, son fácilmente influenciables, tienen emociones que cambian rápidamente y a menudo se preocupan en exceso por su apariencia física. El diagnóstico se basa en criterios clínicos específicos, y la psicoterapia es el tratamiento principal.  ",
        "sintomas": "•	Necesidad de atención, •	Comportamiento seductor o provocativo, •	Expresión emocional exagerada, •	Emociones rápidamente cambiantes, •	Influenciable, •	Preocupación por la apariencia, •	Percepción exagerada de la intimidad, •	Discurso impresionista, •	Baja tolerancia a la frustración",
    },
    {
        "nombre": "Trastorno de la Personalidad Obsesivo-Compulsiva",
        "descripcion": "El trastorno obsesivo-compulsivo de la personalidad (TOCP) se caracteriza por una preocupación excesiva por el orden, el perfeccionismo y el control, a diferencia del trastorno obsesivo-compulsivo (TOC) que se define por pensamientos y comportamientos recurrentes e intrusivos. Las personas con TOCP suelen tener dificultades para completar tareas debido a sus altos estándares, una excesiva devoción por el trabajo, inflexibilidad y dificultad para delegar. ",
        "sintomas": "•	Perfeccionismo extremo, •	Preocupación por el orden y los detalles, •	Control y rigidez, •	Inflexibilidad, •	Devoción excesiva por el trabajo, •	Dificultad para delegar, •	Aislamiento emocional, •	Avaricia/Precaución financiera",
    },
    {
        "nombre": "Trastorno de Tics",
        "descripcion": "Un trastorno de tics es una afección neurológica que provoca movimientos o sonidos repentinos e involuntarios llamados tics. Pueden ser motores (movimientos, como parpadear o encoger los hombros) o vocales (sonidos, como carraspear o gruñir). Existen diferentes tipos, como los trastornos de tics transitorios (que duran menos de un año) y el trastorno de Gilles de la Tourette (un trastorno crónico). ",
        "sintomas": "•	Trastorno de tics transitorios, •	Trastorno crónico de tics motor o vocal, •	Síndrome de Gilles de la Tourette",
    },
    {
        "nombre": "Trastorno de Tourette",
        "descripcion": "El síndrome de Tourette es un trastorno del sistema nervioso que causa movimientos y sonidos repetitivos e involuntarios, llamados tics. Estos tics pueden ser simples (como parpadear o carraspear) o complejos (como movimientos elaborados o la repetición de palabras). Generalmente, los síntomas comienzan en la niñez, varían en severidad y pueden cambiar con el tiempo, a menudo mejorando en la edad adulta.  ",
        "sintomas": "•	Tics",
    },
    {
        "nombre": "Autolesión",
        "descripcion": "•	Es un comportamiento en el que una persona se causa daño a sí misma de manera intencionada para intentar lidiar con el dolor emocional. Funciona como una estrategia de afrontamiento temporal que puede generar un alivio momentáneo, pero que a menudo se vuelve un ciclo difícil de romper. Las lesiones pueden variar desde leves hasta graves y pueden dejar cicatrices permanentes. Aunque es más común en adolescentes y adultos jóvenes, puede ocurrir a cualquier edad. ",
        "sintomas": "•	Cortarse, •	Quemarse, •	Golpearse, •	Arrancarse el cabello o la piel, •	Insertarse objetos, •	Romperse huesos o causarse moret",
    },
    {
        "nombre": "Trastorno de Estrés Postraumático (TEPT)",
        "descripcion": "El Trastorno de Estrés Postraumático (TEPT) es una afección de salud mental que puede desarrollarse después de experimentar o presenciar un evento traumático, como un desastre natural, un accidente grave o la violencia. Las personas con TEPT pueden revivir el trauma a través de flashbacks o pesadillas, experimentar problemas para dormir o concentrarse, sentirse distantes o aislados, y sobresaltarse fácilmente. Aunque muchas personas se recuperan naturalmente con el tiempo, el TEPT se diagnostica cuando los síntomas persisten y afectan significativamente la vida diaria. ",
        "sintomas": "•	Reexperimentación, •	Evitación, •	Cambios en el estado de ánimo y el pensamiento, •	Hiperactivación",
    },
    {
        "nombre": "Trastorno de Personalidad Limítrofe (TLP)",
        "descripcion": "El trastorno límite de la personalidad (TLP) es una afección de salud mental caracterizada por patrones de comportamiento emocional inestable, impulsividad y relaciones interpersonales caóticas. Las personas con TLP pueden experimentar cambios extremos de humor, miedo intenso al abandono, problemas de autoimagen, y comportamiento autolesivo o de riesgo. Aunque el TLP puede ser grave, existen tratamientos efectivos, principalmente a través de psicoterapia, que ayudan a manejar los síntomas y mejorar la calidad de vida.",
        "sintomas": "•	Inestabilidad emocional, •	Miedo al abandono, •	Relaciones interpersonales inesta, •	Impulsividad,. •	Autolesiones o ideas suicidas, •	Sentimientos crónicos de vacío, •	Ira intensa",
    },
    {
        "nombre": "Delirante",
        "descripcion": "Un trastorno de salud mental caracterizado por una o más creencias falsas que persisten durante un mes o más, sin que la persona sepa que no son reales.",
        "sintomas": "",
    },
    {
        "nombre": "TDAH (Trastorno por Déficit de Atención e Hiperactividad)",
        "descripcion": "El Trastorno por Déficit de Atención e Hiperactividad (TDAH) es un trastorno del neurodesarrollo caracterizado por la falta de atención, la hiperactividad y la impulsividad, que puede persistir desde la infancia hasta la edad adulta. Sus síntomas pueden causar dificultades en el rendimiento académico, laboral y en las relaciones sociales. El tratamiento suele incluir una combinación de medicamentos, terapia y estrategias de apoyo.  ",
        "sintomas": "•	Falta de atención, •	Hiperactividad, •	Impulsividad",
    },
    {
        "nombre": "Trastorno Obsesivo-Compulsivo (TOC)",
        "descripcion": "El Trastorno Obsesivo-Compulsivo (TOC) se caracteriza por pensamientos obsesivos y recurrentes, y/o comportamientos compulsivos que la persona siente la necesidad de realizar. Las obsesiones pueden ser pensamientos, imágenes o impulsos no deseados sobre temas como la contaminación, el daño o la simetría, mientras que las compulsiones son comportamientos repetitivos para reducir la ansiedad o prevenir algo. El tratamiento suele incluir terapia conductual, como la exposición y prevención de la respuesta, y medicamentos. ",
        "sintomas": "•	Obsesiones, , •	Compulsiones",
    },
    {
        "nombre": "Alzheimer",
        "descripcion": "La enfermedad de Alzheimer es un trastorno del cerebro que lentamente destruye la memoria y la habilidad para pensar y, con el tiempo, la capacidad de realizar hasta las tareas más sencillas. Esta enfermedad es la forma más común de demencia en personas mayores.",
        "sintomas": "",
    },
    {
        "nombre": "Trastornos Alimentarios",
        "descripcion": "Los trastornos alimentarios (o trastornos de la conducta alimentaria, TCA) son enfermedades mentales graves que se caracterizan por una alteración grave y persistente de los comportamientos alimentarios y una preocupación excesiva por el peso, la figura y la comida. Estos trastornos afectan negativamente la salud física y mental de una persona y pueden poner en peligro su vida. ",
        "sintomas": "",
    },
    {
        "nombre": "Bipolaridad (Trastorno Bipolar)",
        "descripcion": " El trastorno bipolar es una enfermedad mental que causa cambios extremos en el estado de ánimo, la energía y los niveles de actividad, alternando entre episodios de manía (euforia, excitación o irritabilidad extrema) y episodios de depresión (tristeza profunda o desesperanza). Estos períodos pueden durar días o semanas y afectar significativamente el funcionamiento diario de una persona, como su trabajo, estudios y relaciones. ",
        "sintomas": "•	Euforia o irritabilidad excesiva, •	Aumento de energía, •	Pensamiento acelerado, •	Juicio deficiente",
    },
    {
        "nombre": "Bruxismo",
        "descripcion": "El bruxismo es una afección en la que una persona rechina, aprieta o cruje los dientes; puede ocurrir cuando se está despierto o dormido. El bruxismo que ocurre mientras una persona está despierta es más frecuente, pero el bruxismo que ocurre durante el sueño se ha estudiado más. Tanto los niños como los adultos pueden tener esta afección.",
        "sintomas": "",
    },
    {
        "nombre": "DELIRIO",
        "descripcion": "Es una confusión grave y repentina debido a cambios rápidos en la actividad cerebral que pueden ocurren con enfermedad física o mental.",
        "sintomas": "",
    },
    {
        "nombre": "Ludopatía",
        "descripcion": "La ludopatía o juego patológico se ha definido como un impulso irreprimible de jugar y/o apostar. La palabra se origina del latín: ludus, que significa “yo juego” y la palabra griega pathos, que significa afección, enfermedad o pasión por el juego. El juego patológico también se ha definido como una enfermedad crónica y progresiva consistente en la falta de control en los impulsos y un deseo irreprimible de participar en juegos de apuesta. Es una conducta descontrolada relacionada con los juegos de azar y las apuestas (Iturriaga, 2010), se refiere a las actividades en las que se realizan apuestas y como componente prominente se encuentra el azar, incluye todos los juegos de azar y apuestas como las máquinas tragamonedas, bingos, casinos, loterías, cupones, cartas, ruletas, dados, dominó, peleas de animales (gallos, perros), carreras de caballos, entre otros, y más recientemente, las apuestas por internet.",
        "sintomas": "cambia",
    }
   
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/podcast')
def podcast():
    return render_template('podcast.html', podcasts=PODCASTS)

@app.route('/carteles')
def pagina_carteles():
    return render_template('carteles.html', carteles=CARTEL_DATA)

@app.route('/informacion')
def informacion():
    return render_template('informacion.html', enfermedades = ENFERMEDADES)

if __name__ == '__main__':
    app.run(debug=True)