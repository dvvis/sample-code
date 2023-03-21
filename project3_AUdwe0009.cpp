//Davis Edwards dwe0009
//project3_dwe0009
//Accepts 2 input files, combines and sorts them and creates a new file.
//Compiles with g++ project3_dwe0009.cpp on AU servers
//Sources:
//Project 3 pdf was used for source code.
//Various note slides were referenced.

#include <fstream>
#include <iostream>
#include <cstdlib>  //for exit()
#include <cstring>
#include <string>
using namespace std;
const int MAX_SIZE = 100;

//Input: (1) Array storing data retrieved from the file(i.e.,instream)
//       (2) input file stream object
//Output: Size of array. Note: you need to use this parameter to control the array size.

int readfile(int inputArray[], ifstream& instream) {
	if (instream.fail()) {
		cout << "Input file opening failed." << endl;
		exit(1);
	}

	int index = 0;
	instream >> inputArray[index];
	while (!instream.eof()) {
		index++;
		instream >> inputArray[index];
	}
	return index;
}

//takes array1 & 2 and combines them into a single outputArray
int sort(int inputArray1[], int inputArray1_size, int inputArray2[], int inputArray2_size, int outputArray[]) {
	int i = 0;
	int j = 0;
	int k = 0;
		while (i < inputArray1_size && j < inputArray2_size) {
			if (inputArray1[i] <= inputArray2[j]) {
				outputArray[k] = inputArray1[i];
				i++;
			}
			else {
				outputArray[k] = inputArray2[j];
				j++;
			}
			k++;
		}
		if (i < inputArray1_size) {
			while (i < inputArray1_size) {
				outputArray[k] = inputArray1[i];
					i++;
					k++;
			}
		}
		if (j < inputArray2_size) {
			while (j < inputArray2_size) {
				outputArray[k] = inputArray2[j];
					j++;
					k++;
			}
		}
	//returns the number of sorted elements
	return k;
}
//writes the file, named after a given string.
void writefile(int outputArray[], int outputArray_size, string name) {
	int i = 0;
	ofstream output;
	output.open(name.c_str());
	while (i < outputArray_size) {
		output << outputArray[i] << "\n";
		i++;
	}
	output.close();
}

//main function
int main() {
	ifstream inStream1;
	ifstream inStream2;
	int iArray1[MAX_SIZE];
	int iArray1_size;
	int iArray2[MAX_SIZE];
	int iArray2_size;
	int outputArray[MAX_SIZE];
	string file1;
	string file2;
	string fileN;
	int i = 0;
	int j = 0;
	int k = 0;

	cout << "*** Welcome to Davis' sorting program ***\n";
	cout << "Enter the first input file name: ";
	cin >> file1;
	inStream1.open(file1.c_str());
	iArray1_size = readfile(iArray1, inStream1);
	if (iArray1_size < 0) {
		exit(1);
	}
	cout << "The list of " << iArray1_size << " numbers in file " << file1 << " is: \n";
	while (i < iArray1_size) {
		cout << iArray1[i] << "\n";
		i++;
	}
	inStream1.close();

	cout << "\nEnter the second input file name: ";
	cin >> file2;
	inStream2.open(file2.c_str());
	iArray2_size = readfile(iArray2, inStream2);
	if (iArray2_size < 0) {
		exit(1);
	}
	cout << "The list of " << iArray2_size << " numbers in file " << file2 << " is: \n";
	while (j < iArray2_size) {
		cout << iArray2[j] << "\n";
		j++;
	}
	inStream2.close();
	int output = sort(iArray1, iArray1_size, iArray2, iArray2_size, outputArray);
	cout << "\nThe sorted list of " << output << " numbers is: ";
	while (k < output) {
		cout << outputArray[k] << " ";
			k++;
	}
	cout << "\nEnter the output file name: ";
	cin >> fileN;

	writefile(outputArray, output, fileN);
	cout << "*** Please check the new file - " << fileN << " ***\n*** Goodbye. ***\n";
}



