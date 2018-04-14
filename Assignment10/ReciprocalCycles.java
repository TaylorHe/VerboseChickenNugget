/**
 *	CS 370 Assignment 10: Reciprocal Cycles	
 * 	Taylor He, Jacob Manzelmann, Thomas Osterman
 *	I pledge my honor that I have abided by the Stevens Honor System.
 */

import java.util.HashMap;
public class ReciprocalCycles {
	
	public static String fractionToDecimal(int denr) {
		if (denr == 1) {
			return "1";
		}
		String result = "";
		HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
		int remainder = 1 % denr;
		while(remainder != 0 && (h.get(remainder) == null)) {
			h.put(remainder, result.length());
			remainder *= 10;
			int res_part = remainder / denr;
			result += Integer.toString(res_part);
			remainder = remainder % denr;
		}

		if (remainder == 0) {
			return "0." + result;
		} else {
			// Formatting magic
			String cycle = result.substring(h.get(remainder));
			return "0." + result.substring(0, h.get(remainder)) + "(" + cycle + "), cycle length " + cycle.length();
		}
		
	}
	
	public static void main(String[] args) {
		// Check args
		if (args.length != 1) {
			System.err.println("Usage: java ReciprocalCycles <denominator>");
			return;
		}
		try {
			int num = Integer.parseInt(args[0]);
			if (num < 1) {
				System.err.println("Error: Denominator must be an integer in [1, 2000]. Received \'" + args[0] + "\'.");
				return;
			}
		} catch (Exception e) {
			System.err.println("Error: Denominator must be an integer in [1, 2000]. Received \'" + args[0] + "\'.");
			return;
		}
		// Finally print
		System.out.println("1/" + args[0] + " = " + fractionToDecimal(Integer.parseInt(args[0])));

	}
}
