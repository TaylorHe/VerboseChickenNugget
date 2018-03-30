#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

void backtrack(int** table, int size) {
	
}

void solve(vector<vector<int> > data) {
	int size = data.size();
	int** table = new int*[size];
	for (int i=0; i<size; ++i) {
		table[i] = new int[size];
	}

	for (int i=0; i<size; ++i) {
		table[i][0] = data[i][0];
	}

	for (int j=1; j<size; ++j) {
		table[0][j] = data[0][j] + table[0][j-1];

		for (int i=1; i<size; ++i) {
			if (table[i][j-1] > table[i-1][j]) {
				table[i][j] = data[i][j] + table[i-1][j];
			}
			else {
				table[i][j] = data[i][j] + table[i][j-1];
			}
		}

		for (int i=size-2; i>=0; --i) {
			if (table[i][j-1] > table[i+1][j]) {
				table[i][j] = data[i][j] + table[i+1][j];
			}
		}
	}

	backtrack(table, size);

	for (int i=0; i<size; ++i) {
		delete table[i];
	}
	delete table;
}

int main(int argc, char** argv) {
	ifstream file("matrix.txt");
	vector<vector<int> > data;
	string line;
	string value;
	while (getline(file, line)) {
		vector<int> vec;
		istringstream ss(line);
		while (getline(ss, value, ',')) {
			vec.push_back(stoi(value));
		}
		data.push_back(vec);
	}
	if (data.size() == 1) {
		cout << "Min sum: " << data[0][0] << endl;
		cout << "Values: [" << data[0][0] << ']' << endl;
	}
	else {
		solve(data);
	}
	return 0;
}