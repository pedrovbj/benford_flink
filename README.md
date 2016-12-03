## Para compilar o código
mvn clean package
## Para rodar o código
mvn mvn exec:java -Dexec.mainClass=org.apache.flink.Benford -Dexec.args="file:///home/grupo11sd/caminho/para/arquivo 0000000000000000001 -n=2 -d=; -o=file:///home/grupo11sd/results"
ps: sao tres barras mesmo em "file:///"
## Sobre o argumento fieldMask
https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/api/java/io/CsvReader.html#includeFields-java.lang.String-
## Demais duvidas
https://www.facebook.com/vrglh
