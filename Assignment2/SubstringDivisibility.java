/*
 * Project Euler #43, with some modifications to support various lengths
 * @author Taylor He
 * @author Jacob Manzelmann
 * @author Thomas Osterman
 * I pledge my honor that I have abided by the Stevens Honor System.
 *   - Taylor He, Jacob Manzelmann, Thomas Osterman
 */

import java.util.HashSet;
import java.util.Arrays;
import java.util.Set;
import java.util.Collections;
import java.util.ArrayList;

public class SubstringDivisibility {
	/**
	 * Checks if a String has all unique characters
	 * @param  numberAsString
	 * @return true if all characters are unique in the string, else false
	 */
	private static boolean isUnique(String numberAsString) {
		Set<Character> numSet = new HashSet<Character>();
		for (char c : numberAsString.toCharArray()) {
			if (!numSet.add(c)) {
				return false;
			}
		}
		return true;
	}

	/**
	 * Finds the sum of the digits in the number
	 * @param  numberAsString
	 * @return the sum of the digits in the number
	 */
	private static int strSum(String numberAsString) {
		int sum = 0;
		for (char c : numberAsString.toCharArray()) {
			sum += (int)c-48;  // 48 is the ascii starting value of 0
		}
		return sum;
	}

	/**
	 * Finds the remaining digit not used
	 * @param  numberAsString
	 * @param  inputString
	 * @return the remaining digit not used as a String
	 */
	private static String findFirstDigit(String numberAsString, int inputSum) {
		return Integer.toString(inputSum - strSum(numberAsString));
	}

	/**
	 * Checks that all digits in candidateInt belong in the HashSet elements
	 * @param  candidateInt the int to check
	 * @param  elements all valid elements as type HashSet<Character> 
	 * @return boolean
	 */
	private static boolean inElements(String candidateInt, HashSet<Character> elements) {
		for (char c : candidateInt.toCharArray()) {
			if (!elements.contains(c)) {
				return false;
			}
		}
		return true;
	}

	/**
	 * Pads the number to 3 digits, adding zeroes to the front
	 * @param  numberAsString
	 * @return String
	 */
	private static String pad3(String numberAsString) {
		if (numberAsString.length() == 3) return numberAsString;
		if (numberAsString.length() == 2) return '0' + numberAsString;
		return "00" + numberAsString;
	}

	/**
	 * Builds all valid 3-digit multiples of the given prime and possible elements
	 * @param  prime
	 * @param  all valid elements represented by HashSet<Character> 
	 * @return ArrayList<String> of all valid 3-digit multiples of the given prime
	 */
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

	/**
	 * Given two ArrayList of Strings left and right, finds all permutations of Strings
	 * where the last 2 digits of left and the first 2 digits of right overlap.
	 * Left is always 3 digits long, and right is always at least 3 digits long
	 * @param left  ArrayList<String> where the length of each string is exactly 3
	 * @param right ArrayList<String> where the length of each string is at least 3
	 * @return      An ArrayList<String> where the length of each string is the length 
	 *                                of each String in right + 1
	 */
	private static ArrayList<String> combinations(ArrayList<String> left, ArrayList<String> right) {
		String s;
		ArrayList<String> retSet = new ArrayList<String>();
		for (String s1 : left) {
			for (String s2 : right) {
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

	/**
	 * Sums the elements in an ArrayList where each element is a String
	 * @param  arr
	 * @return the sum as type long
	 */
	private static long arraySum(ArrayList<String> arr) {
		long sum = 0;
		for (String item : arr) {
			sum += Long.parseLong(item);
		}
		return sum;
	}

	/**
	 * Prints the elements in an ArrayList in ascending order
	 * @param arr
	 */
	private static void printList(ArrayList<String> arr) {
		Collections.sort(arr);
		for (String item : arr) {
			System.out.println(item);
		}
	}

	/**
	 * Prints as specified in assignment specs
	 */

	private static void print(ArrayList<String> arr) {
		printList(arr);
		System.out.println("Sum: " + arraySum(arr));
	}

	public static void main(String[] args) {
		// Quick check
		if (args.length != 1) {
			System.out.println("Usage: java SubstringDivisibility <uniqueDigits>");
			return;
		}
		// Parse the command line argument
		String input = args[0];

		// Start the timer.
		long start = System.nanoTime();

		int[] primes = {2, 3, 5, 7, 11, 13, 17};
		int primesIndex = input.length() - 4;

		// Generate valid element HashSet
		HashSet<Character> elements = new HashSet<Character>();
		for (char c : input.toCharArray()) {
			elements.add(c);
		}
		// Build and combine sets as specified in combinations()
		ArrayList<String> left, right = buildSet(primes[primesIndex], elements);
		for (int i = primesIndex - 1; i >= 0; --i) {
			left = buildSet(primes[i], elements);
			right = combinations(left, right);
		}
		
		// Find the unused digit and adds it to the front of the element
		int sumOfInputDigits = strSum(input);
		for (int i = 0; i < right.size(); ++i) {
			right.set(i, findFirstDigit(right.get(i), sumOfInputDigits) + right.get(i));
		}

		// Print nicely
		print(right);

		// Print the time!
		System.out.printf("Elapsed time: %.6f ms\n", (System.nanoTime() - start)/1e6);


	}
}

