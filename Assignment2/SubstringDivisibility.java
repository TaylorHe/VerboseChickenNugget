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

	private static String pad3(String num) {
		if (num.length() == 3) return num;
		if (num.length() == 2) return '0' + num;
		return "00" + num;
	}

	private static ArrayList<String> buildSet(int prime) {
		ArrayList<String> retSet = new ArrayList<String>();
		String paddedNum;
		for (int i=prime; i<1000; i+=prime) {
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

	public static void main(String[] args) {
		System.out.println(isUnique(""));
		System.out.println(isUnique("4"));
		System.out.println(isUnique("43435252"));
		System.out.println(isUnique("3456789"));
		System.out.println(isUnique("2345712"));
		ArrayList<String> a = buildSet(17);
		ArrayList<String> b = buildSet(13);
		System.out.println(a + "\n" + b + "\n" + combinations(b,a));

	}
}

