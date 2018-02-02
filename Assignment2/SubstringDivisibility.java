/*
 * Project Euler #43, with some modifications to support various lengths
 * @author Taylor He
 * @author Jacob Manzelmann
 * I pledge my honor that I have abided by the Stevens Honor System.
 *   - Taylor He, Jacob Manzelmann
 */

import java.util.HashSet;
import java.util.Arrays;
import java.util.Set;
import java.util.ArrayList;

public class SubstringDivisibility {

	private static boolean isUnique(String num) {
		Set<Character> numSet = new HashSet<Character>();
		for (char c : num.toCharArray()) {
			if (! numSet.add(c)) {
				return false;
			}
		}
		return true;
	}

	private static int strSum(String numberAsString) {
		int sum = 0;
		for (char c : numberAsString.toCharArray()) {
			sum += (int)c-48;  // 48 is the ascii starting value of 0
		}
		return sum;
	}

	private static String findFirstDigit(String num, String inputString) {
		return Integer.toString(strSum(inputString) - strSum(num));
	}

	private static boolean inElements(String candidateInt, HashSet<Character> elements) {
		for (char c : candidateInt.toCharArray()) {
			if (!elements.contains(c)) {
				return false;
			}
		}
		return true;
	}

	private static String pad3(String num) {
		if (num.length() == 3) return num;
		if (num.length() == 2) return '0' + num;
		return "00" + num;
	}

	private static ArrayList<String> buildSet(int prime, HashSet<Character> elements) {
		ArrayList<String> retSet = new ArrayList<String>();
		String paddedNum;
		for (int i=prime; i<1000; i+=prime) {
			if (!inElements(Integer.toString(i), elements)) {
				continue;
			}
			paddedNum = pad3(Integer.toString(i));
			if (isUnique(paddedNum)) retSet.add(paddedNum);
		}
		return retSet;
	}

	private static ArrayList<String> combinations(ArrayList<String> left, ArrayList<String> right) {
		String s;
		ArrayList<String> retSet = new ArrayList<String>();
		for (String s1 : left) {
			for (String s2 : right) {
				//System.out.println("anything: " + s1 + '\n' + s2);
				if (s1.substring(1).equals(s2.substring(0,2))) {
					s = s1 + s2.substring(2);
					if (isUnique(s)) {
						retSet.add(s);
					}
				}
			}
		}
		return retSet;
	}

	private static long arraySum(ArrayList<String> arr) {
		long sum = 0;
		for (String item : arr) {
			sum += Long.parseLong(item);
		}
		return sum;
	}

	private static void printList(ArrayList<String> arr) {
		for (String item : arr) {
			System.out.println(item);
		}
	}


	public static void main(String[] args) {
		if (args.length != 1) {
			System.out.println("Usage: java SubstringDivisibility <uniqueDigits>");
			return;
		}
		// Start the timer.
		long start = System.nanoTime();
		String input = args[0];

		int[] primes = {2, 3, 5, 7, 11, 13, 17};
		int primesIndex = input.length() - 4;

		HashSet<Character> elements = new HashSet<Character>();
		for (char c : input.toCharArray()) {
			elements.add(c);
		}
		ArrayList<String> left, right = buildSet(primes[primesIndex], elements);
		for (int i = primesIndex - 1; i >= 0; --i) {
			left = buildSet(primes[i], elements);
			right = combinations(left, right);
		}

		//System.out.println(right);
		
		for (int i = 0; i < right.size(); ++i) {
			right.set(i, findFirstDigit(right.get(i), input) + right.get(i));
		}
		printList(right);
		System.out.println("Sum: " + arraySum(right));

		// Print the time!
		System.out.printf("Elapsed time: %.6f ms\n", (System.nanoTime() - start)/1e6);


	}
}

