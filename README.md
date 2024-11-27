# genomic-databases

## Análisis Comparativo de Secuencias de ADN en Formato FASTA y GenBank:

## 1. Descripción de las Secuencias:
¿Qué tipo de información contienen los archivos?
Los archivos contienen secuencias de ADN representando genes específicos en los formatos FASTA y GenBank. Además, los archivos GenBank incluyen descripciones detalladas de las funciones y características de los genes.
¿Son secuencias de genes específicos, genomas completos u otras entidades biológicas?
Todas las secuencias corresponden a genes específicos, como la hemoglobina, insulina, receptor de factor de crecimiento epidérmico (EGFR), proteína fluorescente verde (GFP) y adrenorreceptores.

## 2. Características de las Secuencias:
### ¿Cuál es la longitud de las secuencias en cada archivo?
- Gen de la Hemoglobina en Humanos: 628 nucleótidos.
- Gen de la Insulina en Humanos: 465 nucleótidos.
- Gen de la Proteína Receptora del Factor de Crecimiento Epidérmico (EGFR): 9905 nucleótidos.
- Gen de la Proteína Green Fluorescent Protein (GFP): 4737 nucleótidos.
- Gen de la Proteína S (coagulación) en Humanos: 2013 nucleótidos.
- Gen de la Proteína Causante de la Fibrosis Quística (CFTR): 6070 nucleótidos.
- Gen de la Proteína Relacionada con el Alzheimer (APP): 3583 nucleótidos.
- Gen de la Distrofina en la Distrofia Muscular de Duchenne (DMD): 3583 nucleótidos.
- Gen de la Huntingtina en la Enfermedad de Huntington (HTT): 13498 nucleótidos.
- Gen de la Proteína Relacionada con el Cáncer de Mama (BRCA1): 7088 nucleótidos.

### ¿Qué proporción de A, T, C y G contienen las secuencias?
- Gen de la Hemoglobina en Humanos: A: 22.13%, T: 26.59%, C: 25.00%, G: 26.27%.
- Gen de la Insulina en Humanos: A: 19.57%, T: 16.56%, C: 33.55%, G: 30.32%.
- Gen de la Proteína Receptora del Factor de Crecimiento Epidérmico (EGFR): A: 27.62%, T: 24.59%, C: 24.73%, G: 23.04%.
- Gen de la Proteína Green Fluorescent Protein (GFP): A: 24.07%, T: 22.42%, C: 27.18%, G: 26.33%.
- Gen de la Proteína S (coagulación) en Humanos: A: 23.15%, T: 26.28%, C: 25.83%, G: 24.74%.
- Gen de la Proteína Causante de la Fibrosis Quística (CFTR): A: 30.69%, T: 28.40%, C: 19.28%, G: 21.63%.
- Gen de la Proteína Relacionada con el Alzheimer (APP): A: 27.24%, T: 24.25%, C: 22.47%, G: 26.04%.
- Gen de la Distrofina en la Distrofia Muscular de Duchenne (DMD): A: 27.24%, T: 24.25%, C: 22.47%, G: 26.04%.
- Gen de la Huntingtina en la Enfermedad de Huntington (HTT): A: 22.91%, T: 23.31%, C: 27.05%, G: 26.72%.
- Gen de la Proteína Relacionada con el Cáncer de Mama (BRCA1): A: 33.41%, T: 24.82%, C: 19.41%, G: 22.36%.


## Interpretación de Arabidopsis thaliana (cromosoma 4, contig fragment No. 17).
### 1. Descripción del Contexto:
Este fragmento corresponde a un contig de 198,176 nucleótidos, identificado como AL161505.2, y es parte del genoma de Arabidopsis thaliana, una planta modelo en investigación genética. Utilizamos un archivo FASTA para analizar la composición de la secuencia, y el gráfico genómico para comprender su estructura funcional.


### 2. Información del Gráfico:

Estructura Genómica:
- En la parte superior, el gráfico muestra los genes anotados, representados como rectángulos verdes y azules. Por ejemplo, se identifican genes como AT4g47310, AT4g47320, y otros más en esta región.
- Las flechas indican la dirección de transcripción, ya sea hacia adelante o hacia atrás en la secuencia.

Exones:
Dentro de cada gen, los exones, que son las regiones codificantes del ADN, están indicados con colores específicos. Por ejemplo:
- El gen AT4g47320 contiene 5 exones.
- Otros genes tienen menos o más exones, dependiendo de su complejidad.

Regiones Repetitivas:
- En la parte inferior del gráfico, las líneas azules representan regiones repetitivas. Estas son comunes en genomas de plantas y pueden tener funciones regulatorias o estructurales.

3. Análisis del Archivo FASTA:
El archivo FASTA correspondiente a este fragmento proporciona detalles cuantitativos sobre la secuencia de ADN:
- Composición de Bases:
  - Adenina (A): 63,937 nucleótidos, que representan el 32.26% de la secuencia.
  - Timina (T): 61,468 nucleótidos, equivalentes al 31.02%.
  - Citosina (C): 37,013 nucleótidos, o el 18.68%.
  - Guanina (G): 35,758 nucleótidos, aproximadamente el 18.04%.
- Características Genómicas:
  - La secuencia tiene una proporción mayor de bases A y T, algo característico de regiones genómicas ricas en AT.
 
## Proteínas:

##1. ¿Qué tipo de información contienen los archivos? 
Se han descargado dos formatos de archivo, fasta y GenPept. 

El archivo fasta contiene una cabecera donde se indica distinto tipo de información sobre la secuencia separada por |. En primer lugar encontramos el origen de la secuencia, es decir, de qué base de datos proviene.  Luego encontramos el identificador de la secuencia en la base de datos y por último, una descripción de la proteína. En la siguiente línea, se encuentra la propia secuencia.

Un GenBank record es una entrada en la base de datos GenBank que describe información detallada sobre una secuencia biológica. En el caso de un archivo en formato .gp (GenPept), los campos clave incluyen:
- Locus: Nombre único de la secuencia y sus características (tamaño, tipo de molécula, especie, fecha de modificación).
- Definición: Descripción breve de la proteína o molécula.
- Accesión y Versión: Identificadores únicos para la secuencia y su versión.
- DBSource: Información sobre la base de datos de origen (en este caso, Protein Data Bank) y los detalles del método - experimental (como difracción de rayos X).
- Palabras clave: Términos que describen la secuencia.
- Fuente y Organismo: Especie de origen y su clasificación taxonómica.
- Referencia: Cita de artículos relevantes sobre la secuencia.
- Comentario: Información adicional sobre la secuencia, como su función o estado.
- Features: Características específicas de la secuencia, como localización o modificaciones.
- Origen: La secuencia de aminoácidos de la proteína.

##2. ¿Son secuencias de genes específicos, genomas completos u otras entidades biológicas?

Son secuencias de aminoácidos que representan proteínas. En el caso de la Hemoglobina Humana, está compuesta por cuatro cadenas, dos alfa (A y C) y dos beta (B y D). Las cadenas A y C comparten longitud de secuencia (141) y contenido, mientras que las dos beta comparten estas características también (longitud 146). Esto provoca que la hemoglobina sea una proteína tetrámera, es decir, formada por cuatro subunidades.

La hemoglobina humana es una proteína compleja que tiene como función principal transportar oxígeno desde los pulmones hasta los tejidos y órganos del cuerpo, y transportar dióxido de carbono (CO₂), un producto de desecho del metabolismo celular, de vuelta a los pulmones para ser exhalado.

La proteína verde fluorescente (o GFP) es una proteína producida por la medusa Aequorea victoria, que emite fluorescencia en la zona verde del espectro visible.

La estructura de la proteína verde fluorescente (GFP) fue determinada en 1996. Esta proteína monomérica consta de aproximadamente 238 aminoácidos y adopta una estructura terciaria en forma de barril beta, una característica común en muchas proteínas fluorescentes que se han identificado posteriormente. El barril beta de la GFP está compuesto por 11 cadenas y contiene una hélice alfa central que atraviesa el barril a lo largo de su longitud. En esta hélice se encuentran tres aminoácidos consecutivos que forman un cromóforo natural, lo que permite que la GFP emita una brillante fluorescencia verde cuando se expone a luz ultravioleta.

2. Longitud y composición: 

2. ¿Cuál es la longitud de las secuencias en cada archivo? 
3. ¿Qué proporción de A, T, C y G contienen las secuencias?

Cadena A (ALFA) - Hemoglobina Humana:
- Longitud de la secuencia: 141
- Mayor Proporción: A (0.1489)

Cadena B (BETA) - Hemoglobina Humana:
- Longitud de la secuencia: 146
- Mayor Proporción: L (0.1233)

Cadena C (ALFA) - Hemoglobina Humana:
- Longitud de la secuencia: 141
- Mayor Proporción: A (0.1489)

Cadena D (BETA) - Hemoglobina Humana:
- Longitud de la secuencia: 146
- Mayor Proporción: L (0.1233)

Proteína Verde Fluorescente (GFP) - Cadena A:
- Longitud de la secuencia: 236
- Mayor Proporción: G (0.0890)


