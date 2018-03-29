#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

void solve(vector<vector<int> > data) {

}

void backtrack(int table[[]]) {

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
	solve(data);
	return 0;
}