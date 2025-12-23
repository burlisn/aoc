#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool IsInGrid(const std::vector<std::vector<char>>& aGrid, const size_t aR, const size_t aC) {
  return (aR < aGrid.size() && aC < aGrid.at(aR).size());
}

uint32_t GetAdjacentRolls(const std::vector<std::vector<char>>& aGrid, const size_t aR, const size_t aC) {
  auto adjacentRolls = 0;
  for (auto dr = -1; dr <= 1; ++dr) {
    for (auto dc = -1; dc <= 1; ++dc) {
      if (dr == 0 && dc == 0) {
        // Not adjacent, don't consider
        continue;
      }
      const auto nr = aR + dr;
      const auto nc = aC + dc;
      if (IsInGrid(aGrid, nr, nc) && aGrid.at(nr).at(nc) == '@') {
        ++adjacentRolls;
      } 
    }
  }
  return adjacentRolls;
}

uint32_t RemoveRolls(std::vector<std::vector<char>>& aGrid) {
  auto rollsRemoved = 0;
  for (auto r = size_t{}; r < aGrid.size(); ++r) {
    for (auto c = size_t{}; c < aGrid.at(r).size(); ++c) {
      if (aGrid.at(r).at(c) != '@') {
        continue;
      }
      const auto adjacentRolls = GetAdjacentRolls(aGrid, r, c);
      if (adjacentRolls < 4) {
        aGrid.at(r).at(c) = '.';
        ++rollsRemoved;
      }
    }
  }
  return rollsRemoved;
}

int main() {
  auto inputFile = std::ifstream{"input.txt"};
  auto ans1 = 0;
  auto ans2 = 0;

  auto grid = std::vector<std::vector<char>>{};
  auto line = std::string{};
  for (auto i = size_t{}; std::getline(inputFile, line); ++i) {
    grid.emplace_back(std::vector<char>{});
    for (auto j = size_t{}; j < line.length(); ++j) {
      grid.at(i).emplace_back(line.at(j));
    }
  }

  auto removedRoll = false;
  do {

  } while (removedRoll == true);

  for (auto r = size_t{}; r < grid.size(); ++r) {
    for (auto c = size_t{}; c < grid.at(r).size(); ++c) {
      if (grid.at(r).at(c) != '@') {
        continue;
      }
      const auto adjacentRolls = GetAdjacentRolls(grid, r, c);
      if (adjacentRolls < 4) {
        ++ans1;
      }
    }
  }

  std::cout << "ans1: " << ans1 << std::endl;
  return 0;
}