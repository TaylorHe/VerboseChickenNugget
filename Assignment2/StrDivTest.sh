#!/bin/bash
if [ ! -f "SubstringDivisibility.class" ]; then
	$(javac SubstringDivisibility.java)
fi

OUTPUT="$(java SubstringDivisibility 1357)"
if [[ "$OUTPUT" =  "Sum: 0"* ]]; then
	echo "passed: 1357"
else
	echo "failed: 1357"
fi

OUTPUT="$(java SubstringDivisibility 12346789)"
if [[ "$OUTPUT" =  "Sum: 0"* ]]; then
	echo "passed: 12346789"
else
	echo "failed: 12346789"
fi

OUTPUT="$(java SubstringDivisibility 0135)"
if [[ "$OUTPUT" =  "1350
1530
3150
3510
5130
5310
Sum: 19980"* ]]; then
		echo "passed: 0135"
	else
		echo "failed: 0135"
	fi

	OUTPUT="$(java SubstringDivisibility 0246)"
	if [[ "$OUTPUT" =  "0246
0264
0426
0462
0624
0642
2046
2064
2406
2460
2604
2640
4026
4062
4206
4260
4602
4620
6024
6042
6204
6240
6402
6420
Sum: 79992"* ]]; then
		echo "passed: 0246"
	else
		echo "failed: 0246"
	fi

	OUTPUT="$(java SubstringDivisibility 0123)"
	if [[ "$OUTPUT" =  "0132
0312
1032
1230
1302
1320
2130
2310
3012
3102
3120
3210
Sum: 22212"* ]]; then
		echo "passed: 0123"
	else
		echo "failed: 0123"
	fi

	OUTPUT="$(java SubstringDivisibility 13469)"
	if [[ "$OUTPUT" =  "14369
14963
41369
41963
50369
50963
Sum: 213996"* ]]; then
		echo "passed: 13469"
	else
		echo "failed: 13469"
	fi

	OUTPUT="$(java SubstringDivisibility 0235689)"
	if [[ "$OUTPUT" =  "0836952
2390658
2596308
2896350
2930658
3290658
3806952
3860952
5296308
6830952
6958203
8036952
8296350
8306952
8360952
8630952
9230658
9658203
Sum: 102215970"* ]]; then
		echo "passed: 0235689"
	else
		echo "failed: 0235689"
	fi

	OUTPUT="$(java SubstringDivisibility 123456789)"
	if [[ "$OUTPUT" =  "149635728
419635728
509635728
Sum: 1078907184"* ]]; then
		echo "passed: 123456789"
	else
		echo "failed: 123456789"
	fi

	OUTPUT="$(java SubstringDivisibility 012345678)"
	if [[ "$OUTPUT" =  "140635728
146035728
410635728
416035728
Sum: 1113342912"* ]]; then
		echo "passed: 012345678"
	else
		echo "failed: 012345678"
	fi

	OUTPUT="$(java SubstringDivisibility 0123456789)"
	if [[ "$OUTPUT" =  "1406357289
1430952867
1460357289
4106357289
4130952867
4160357289
Sum: 16695334890"* ]]; then
		echo "passed: 0123456789"
	else
		echo "failed: 0123456789"
	fi