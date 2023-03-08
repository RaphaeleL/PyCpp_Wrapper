#include <iostream>
#include <string>
#include "Python.h"

std::string getPath() {
	// Auto Detect Current Working Directory
    #ifdef __APPLE__
    return "/Users/raphaelelicciardo/Studium/Master/Semester-3/Master-Thesis/Code/PyCpp_Wrapper/";
    #elif __MACH__
    return "/Users/raphaelelicciardo/Studium/Master/Semester-3/Master-Thesis/Code/PyCpp_Wrapper/";
    #elif __LINUX__
    return "/home/stud-lira1011/master-thesis/bindings/PyCpp_Wrapper/";
    #endif
}

std::string createPath(const char* filename) {
	return std::string(getPath() + std::string(filename));
}

int main(int argc, char* argv[]) {
	// Get Path
	const char* filename = "";
	if (argc > 1) {
		filename = argv[1];
	}
	std::string path = createPath(filename);
	const char* file = path.c_str();

	// Initialize the Python Instance
	Py_Initialize();

    // Add the directory of the Python script to the Python path
	std::string scriptDir = path.substr(0, path.find_last_of("/\\"));
	if (scriptDir.empty()) {
		std::cerr << "Failed to extract script directory from path: " << path << std::endl;
		return 1;
	}
	std::string pythonPath = std::string("sys.path.append(\"") + scriptDir + "\")";
	if (!Py_IsInitialized()) {
		std::cerr << "Python interpreter is not initialized" << std::endl;
		return 1;
	}
	PyRun_SimpleString("import sys, os\n");
	PyRun_SimpleString("print(os.getcwd())");
	if (PyRun_SimpleString(pythonPath.c_str()) == -1) {
		std::cerr << "Failed to execute Python code: " << pythonPath << std::endl;
		PyErr_Print();
		return 1;
	}
	PyRun_SimpleString("import sys, os\n");
	PyRun_SimpleString("print(os.getcwd())");

	// Run the File
	FILE* PScriptFile = fopen(file, "r");
	if (PScriptFile) {
		PyRun_SimpleFile(PScriptFile, file);
		fclose(PScriptFile);
	} else {
		std::cerr << "There is no '" << filename << "' in " << getPath() << std::endl;
		PyErr_Print();
		return 1;
	}

	// Close the Python Instance
	Py_Finalize();

	return 0;
}
