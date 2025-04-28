#include <cmath>
#include <iostream>
#include <map>

int main() {
  std::map<char, int> res;
  int charsum{};
  std::string num;
  while (std::cin.good()) {
    std::cin >> num;
    for (const auto &c : num) {
      charsum++;
      res[c]++;
    }
  }

  for (auto [k, n] : res) {
    std::cout << k << ": " << (double)n / (double)charsum * 100 << "%\n";
  }
}
