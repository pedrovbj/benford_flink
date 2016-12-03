## Para compilar o código
mvn clean package
## Para rodar o código
mvn mvn exec:java -Dexec.mainClass=org.apache.flink.Benford -Dexec.args="file:///home/grupo11sd/caminho/para/arquivo 0000000000000000001 -n=2 -d=; -o=file:///home/grupo11sd/results"
ps: sao tres barras mesmo em "file:///"
## Sobre o argumento fieldMask
https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/api/java/io/CsvReader.html#includeFields-java.lang.String-
## Testes de desempenho
### Para alterar o número de nós que o flink vai rodar no cluster
Editar arquivo  ~/.flink_build/build-target/conf/slaves comentando os nós que nao se quer utilizar com #
Ex: utilizar somente nós 01, 02, 03 e 04\n
- node01
- node02
- node03
- node04
- #node05
- #node06
- #node07
- ...
- #node18
### Iniciar e para cluster
Ao se iniciar o cluster com o comando start-cluster.sh, não pode ocorrer esse tipo de mensagem:
[INFO] 2 instance(s) of taskmanager are already running on node03
Caso isso ocorra, para cada nó que ocorrer tem-se que parar os taskmanagers para nao afetarem os testes, isso eh feito assim:
Primeiro no frontend:
stop-cluster.sh
Depois nos demais nós em q apareceu a mensagem
ssh node03
taskmanager.sh stop
taskmanager.sh stop
Tem q se rodar o comando taskmanager.sh stop uma vez para cada instancia de taskmanager e entao no caso, sao duas vezes.
## Demais duvidas
https://www.facebook.com/vrglh
