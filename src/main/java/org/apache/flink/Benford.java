package org.apache.flink;

import org.apache.flink.api.java.DataSet;
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.common.functions.FilterFunction;
import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.common.operators.Order;
import org.apache.flink.api.java.io.CsvReader;
import org.apache.flink.api.java.tuple.Tuple1;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.core.fs.FileSystem.WriteMode;
import org.apache.flink.types.StringValue;
import org.apache.flink.util.Collector;

import scala.collection.immutable.List;
import scala.collection.immutable.List;

public class Benford {

	public static void main(String[] args) throws Exception {

		if(args.length < 2) {
			System.out.println("Benford - returns the frequencies of the first n digits of a csv file");
			System.out.println("args: input_file field_mask [-d=field_delimiter(default ;)]" +
					" [-o=output_folder] [-n=number_of_digits]");
			System.exit(0);
		}
		String inputFile = args[0];
		String fieldMask = args[1];
		String outputFolder = inputFile+".results";
		String fieldDelimiter = ";";
		if(args.length > 2) {
			for(int i = 2; i < args.length; i++) {
				final String a = args[i];
				if(a.startsWith("-o")) {
					outputFolder = a.substring(3).trim();
				} else if(a.startsWith("-d")) {
					fieldDelimiter = a.substring(3).trim();
				} else if(a.startsWith("-n")) {
					try {
						WrapNumOfDig.numberOfDigits = Integer.parseInt(a.substring(3).trim());
				    } catch (NumberFormatException e) {
				        System.err.println("Argument" + a + " must be an integer.");
				        System.exit(1);
				    }
				} else {
					System.out.println("Invalid argument " + a);
					System.exit(1);
				}
			}
		}
		
		// set up the execution environment
		final ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();

		// get input data
		DataSet<Integer> digit = env.readCsvFile(inputFile)
				.ignoreFirstLine()
				.includeFields(fieldMask) //Apenas "Valor despesa"
				.fieldDelimiter(fieldDelimiter)
				.types(String.class)
				.map(new MapFunction<Tuple1<String>, String>() {
					@Override
					public String map(Tuple1<String> t1) {
						return t1.f0.substring(1,WrapNumOfDig.numberOfDigits+1);
					}
				})
				.filter(new FilterFunction<String>() {
					  public boolean filter(String s) { return s.matches("[1-9][0-9]*"); }
				})
				.map(new MapFunction<String, Integer>() {
					@Override
					public Integer map(String s) {
						return Integer.parseInt(s);
					}
				});

		DataSet<Tuple2<Integer, Integer>> counts =
				digit.flatMap(new FlatMapFunction<Integer, Tuple2<Integer, Integer>>() {
					public void flatMap(Integer value, Collector<Tuple2<Integer, Integer>> out) {
						out.collect(new Tuple2<Integer,Integer>(value, 1));
					}
				})
				.groupBy(0)
				.sum(1);
		
		counts.writeAsCsv(outputFolder, WriteMode.OVERWRITE);
		counts.print();
		
		System.exit(0);
		
	}
	
}

class WrapNumOfDig {
	public static int numberOfDigits = 1;
}