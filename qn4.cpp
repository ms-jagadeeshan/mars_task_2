#include <fstream>
#include <iostream>
#include <vector>
// Read a matrix from a file, where each line represents a row in the matrix
// with values separated by spaces, print the matrix in standard 2D matrix
// format after transposing it.

void print(int rows, int cols, int *matrix) {
  std::cout << "Matrix: " << std::endl;

  std::cout << "[" << std::endl;
  for (int i = 0; i < rows; ++i) {
    std::cout << "[";
    for (int j = 0; j < cols; ++j) {
      std::cout << matrix[i * cols + j] << ",";
    }
    std::cout << "]," << std::endl;
  }
  std::cout << "]" << std::endl;
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " filename" << std::endl;
    return 1;
  }

  std::ifstream file(argv[1]);
  if (!file.is_open()) {
    std::cerr << "Could not open file " << argv[1] << std::endl;
    return 1;
  }

  int rows, cols;
  file >> rows >> cols;
  if (rows != cols) {
    std::cerr << "Matrix must be square" << std::endl;
    return 1;
  }

  std::vector<int> matrix(rows * cols);
  for (int i = 0; i < rows; ++i) {
    for (int j = 0; j < cols; ++j) {
      file >> matrix[i * cols + j];
    }
  }

  print(rows, cols, matrix.data());
}
