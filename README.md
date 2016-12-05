## Para compilar o código
mvn clean package
## Para rodar o código
mvn exec:java -Dexec.mainClass=org.apache.flink.Benford -Dexec.args="file:///home/grupo11sd/caminho/para/arquivo 0000000000000000001 -n=2 -d=; -o=file:///home/grupo11sd/results"
ps: sao tres barras mesmo em "file:///"
## Sobre o argumento fieldMask
https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/api/java/io/CsvReader.html#includeFields-java.lang.String-
## Testes de desempenho
### Para alterar o número de nós que o flink vai rodar no cluster
Editar arquivo  ~/.flink_build/build-target/conf/slaves comentando os nós que nao se quer utilizar com #
Ex: utilizar somente nós 01, 02, 03 e 04
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
Caso isso ocorra, primeiro esperar o start-cluster.sh finalizar, e rodar no frontend:
- stop-cluster.sh
Entao, para cada nó XX em q a mensagem ocorrer rodar:
- ssh nodeXX
- flink-daemon.sh stop-all taskmanager
E entao iniciar o cluster novamente com start-cluster.sh

## Demais duvidas
https://www.facebook.com/vrglh
