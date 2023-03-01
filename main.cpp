#include <iostream>
#include <string>
#include "Python.h"

std::string getPath() {
	// TODO: Auto Detect Current Working Directory
	return std::string("/Users/raphaelelicciardo/Studium/Master/Semester-3/Master-Thesis/Code/boost-test/");
}

std::string createPath(const char* filename) {
	return std::string(getPath() + std::string(filename));
}

int main(int argc, char* argv[]) {
	// Initialize the Python Instance
	Py_Initialize();

	// Run a simple string
	PyRun_SimpleString("from time import time,ctime\n"
			           "print('Today is', ctime(time()))\n");

	// Run a simple file
	std::string path = createPath("test.py");
	const char* file = path.c_str();
	FILE* PScriptFile = fopen(file, "r");
	if (PScriptFile) {
		PyRun_SimpleFile(PScriptFile, file);
		fclose(PScriptFile);
	}

	// Close the Python Instance
	Py_Finalize();

	return 0;
}
