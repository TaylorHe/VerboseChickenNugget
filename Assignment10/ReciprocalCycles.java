/**
 *	CS 370 Assignment 10: Reciprocal Cycles	
 * 	Taylor He, Jacob Manzelmann, Thomas Osterman
 *	I pledge my honor that I have abided by the Stevens Honor System.
 */

import java.util.HashMap;
public class ReciprocalCycles {
	/**
	 *	Finds the repeating cycle, if any, in a fraction 1/d
	 *	@param int denominator [1,2000]
	 *	@return String "0.%s(%s), cycle length %d"
	 */
	public static String findCycle(int d) {
		if (d == 1) {
			return "1";
		}
		String result = "";
		HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
		int remainder = 1 % d;
		int quotient;
		// Loop while the remainder is not 0 and the hashmap entry
		// for the remainder exists
		while(remainder != 0 && (h.get(remainder) == null)) {
			// append to the hashmap
			h.put(remainder, result.length()); 
			remainder *= 10;
			quotient = remainder / d;
			result += Integer.toString(quotient);
			remainder = remainder % d;
		}

		if (remainder == 0) {
			return String.format("0.%s", result);
		} else {
			// Formatting magic
			String cycle = result.substring(h.get(remainder));
			return String.format("0.%s(%s), cycle length %d", result.substring(0, h.get(remainder)), cycle, cycle.length());
			// return result.substring(0, h.get(remainder)) + "(" + cycle + "), cycle length " + cycle.length();
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
			// Finally print
			System.out.println(String.format("1/%s = %s", args[0], findCycle(num)));
		} catch (Exception e) {
			System.err.println("Error: Denominator must be an integer in [1, 2000]. Received \'" + args[0] + "\'.");
			return;
		}

	}
}
