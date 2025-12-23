#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <math.h>

void Update(uint64_t aNewNumber, uint64_t& aJoltage, uint64_t aIndex);

static constexpr auto JoltageSize = 12;

int main() {
  auto input_file = std::ifstream{"input.txt"};
  auto ans1 = 0;
  auto ans2 = uint64_t{};

  auto line = std::string{};
  while (std::getline(input_file, line)) {
    auto first = 0;
    auto second = 0;
    auto joltage2 = uint64_t{};
    for (auto i = size_t{}; i < line.length(); ++i) {
      const auto num = line.at(i) - '0';
      std::cout << "num: " << num << std::endl;
      if (num > first && i < line.length() - 1) {
        first = num;
        second = 0;
      } else if (num > second) {
        second = num;
      }
      
      auto idx = line.length() - i - 1;
      if (idx >= 12) {
        idx = 11;
      }
      Update(num, joltage2, idx);
    }

    std::cout << first << second << std::endl;
    std::cout << joltage2 << std::endl;
    ans1 += first * 10 + second;
    ans2 += joltage2;
  }

  std::cout << "ans1: " << ans1 << std::endl;
  std::cout << "ans2: " << ans2 << std::endl;
  return 0;
}

void Update(const uint64_t aNewNumber, uint64_t& aJoltage, const uint64_t aIndex) {
  const auto weight = static_cast<uint64_t>(pow(10, aIndex));
  const auto number = (aJoltage / weight) % 10;
  std::cout << "number: " << aNewNumber << std::endl;
  const auto leftPart = aJoltage / (weight * 10);
  const auto rightPart = aJoltage % weight;
  if (aNewNumber > number) {
    std::cout << "leftPart: " << leftPart << "aNewNumber: " << aNewNumber << std::endl;
    aJoltage = (leftPart * weight * 10) + (aNewNumber * weight) + (weight / 10);
    std::cout << "joltage: " << aJoltage << std::endl;
  } else if (aIndex == 0) {
    // Last
    return;
  } else {
    Update(aNewNumber, aJoltage, aIndex - 1);
  }
}
