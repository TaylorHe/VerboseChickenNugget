#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

/*
 Takes in a table and a size, and backtracks to find the minimal path
*/
void backtrack(int** table, int size) {
    //vector that contains the values of each cell taken for the path
    vector<int> minRoute;
    int minSum = table[0][size-1];
    int start = 0;
    int i = 0;
    int j = size-1;
    //finds the starting position for the backtrack, whose value is also the sum
    for(; i < size; i++) {
        if(minSum > table[i][size-1]) {
            minSum = table[i][size-1];
            start = i;
        }
    }
    
    // direction last moved: 0=right, 1=down, 2=up
    int direction = 0;
    
    i = start;
    cout << "Min sum: " << minSum << endl;
    while(j != 0)
    {
        int tempMin;
        //if we're at the top we can't check above us
        if(i == 0)
        {
            //finds the next minSum and adds the difference to the vector
            if(direction != 2 && table[i+1][j] < table[i][j-1]){
                tempMin = table[i+1][j];
                i++;
                direction = 1;
            }
            else{
                tempMin = table[i][j-1];
                j--;
                direction = 0;
            }
            minRoute.push_back(minSum - tempMin);
            minSum = tempMin;
        }
        //if we're at the bottom we can't check below us
        else if(i == size-1){
            //finds the next minSum and adds the difference to the vector
            if(direction != 1 && table[i-1][j] < table[i][j-1]){
                tempMin = table[i-1][j];
                i--;
                direction = 2;
            }
            else{
                tempMin = table[i][j-1];
                j--;
                direction = 0;
            }
            minRoute.push_back(minSum - tempMin);
            minSum = tempMin;
        }
        else{
            //finds the next minSum and adds the difference to the vector
            //move down
            if(direction != 2 && table[i+1][j] <= table[i-1][j] && table[i+1][j] <= table[i][j-1]){
                tempMin = table[i+1][j];
                i++;
                direction = 1;
            }
            //move up
            else if(direction != 1 && table[i-1][j] <= table[i+1][j] && table[i-1][j] <= table[i][j-1]){
                tempMin = table[i-1][j];
                i--;
                direction = 2;
            }
            //move left
            else{
                tempMin = table[i][j-1];
                j--;
                direction = 0;
            }
            minRoute.push_back(minSum - tempMin);
            minSum = tempMin;
        }
    }
    //add the final value to the vector and reverse it
    minRoute.push_back(minSum);
    reverse(minRoute.begin(), minRoute.end());
    cout << "Values: [";
    for(i = 0; i < minRoute.size()-1; i++){
        cout << minRoute[i] << ", ";
    }
    cout << minRoute[minRoute.size()-1] << "]" << endl;
}

/*
 Creates a dp table that contains the increasing sums
 as the data matrix is traversed from left to right
*/
void solve(vector<vector<int> > data) {
	int size = data.size();
    // If 1x1 matrix
    if (size == 1) {
        cout << "Min sum: " << data[0][0] << endl;
        cout << "Values: [" << data[0][0] << ']' << endl;
        return;
    }
    // allocate table
	int** table = new int*[size];
	for (int i=0; i<size; ++i) {
		table[i] = new int[size];
	}

    // populate the left-most column
    // (it will always be the same the left-most column of the data)
	for (int i=0; i<size; ++i) {
		table[i][0] = data[i][0];
	}

    // populate table
	for (int j=1; j<size; ++j) {
        // the upper row can only come from the left initially
		table[0][j] = data[0][j] + table[0][j-1];

        // traverse the row moving downwards
		for (int i=1; i<size; ++i) {
            table[i][j] = min(data[i][j] + table[i-1][j], data[i][j] + table[i][j-1]);
		}

        // traverse back up the row and change values when necessary
		for (int i=size-2; i>=0; --i) {
            table[i][j] = min(table[i][j], data[i][j] + table[i+1][j]);
		}
	}

	backtrack(table, size);

	for (int i=0; i<size; ++i) {
		delete table[i];
	}
	delete[] table;
}

int main(int argc, char** argv) {
    // This is for debugging purposes. The program does not require a
    // parameter, but if given one, then it will use that filename.
    // Otherwise, default to "matrix.txt"
    string filename = argc == 1 ? "matrix.txt" : argv[1];
	ifstream file(filename);
	vector< vector<int> > data;
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
