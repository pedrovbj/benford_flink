# Benford Law using Flink Framework
This project uses [Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law "Benford's law - Wikipedia") to analyse the [accountability](http://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais-1/repositorio-de-dados-eleitorais "Repositorio de dados eleitorais") of candidates at the Brazilian 2012, 2014 and 2016 elections.

### Compiling
mvn clean package

### Running
mvn exec:java -Dexec.mainClass=org.apache.flink.Benford -Dexec.args="file:///home/user/path/to/file 0000000000000000001 -n=2 -d=; -o=file:///home/user/path/to/results"
