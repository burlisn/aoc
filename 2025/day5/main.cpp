#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdint>
#include <string>
#include <stack>
#include <algorithm>

// 1. Construct the list of ranges. Even indexes indicate a start, odd indicate an end.
// If a new start or end is in a range, it doesn't need to be added. If you add a start,
// the next start may need to be removed (if that start is in your range). If you add an end,
// the previous end may need to be removed (if that end is in your range).

enum class End {
  Open,
  Close
};

struct Mark {
  End mEnd{};
  uint64_t mValue{};
};

bool InRange(std::vector<Mark>& aRanges, uint64_t aNumber, size_t aIndex) {
  if (aNumber < aRanges[aIndex].mValue) {
    return false;
  }
  if (aIndex + 1 < aRanges.size()) {
    if (aNumber > aRanges[aIndex + 1].mValue) {
      return false;
    }
  }
  return true;
}

int main() {
  auto ans1 = 0;

  // 158025699 too low
  // 158025699 too low
  auto ans2 = uint64_t{};

  auto inputFile = std::ifstream{"input.txt"};
  auto line = std::string{};
  auto ranges = std::vector<Mark>{};


  for (; std::getline(inputFile, line) && !line.empty(); ) {
    auto const delimiter = std::string{"-"};
    auto startPos = size_t{};
    auto pos = line.find(delimiter, startPos);
    auto const start = std::stoull(line.substr(startPos, pos));
    ranges.emplace_back(Mark{End::Open, start});
    auto const end = std::stoull(line.substr(pos+1));
    ranges.emplace_back(Mark{End::Close, end});
  }

  // Sort the list
  std::sort(ranges.begin(), ranges.end(), [](Mark a, Mark b){
    if (a.mValue == b.mValue) {
      if (a.mEnd == End::Open) {
        return true;
      } else {
        return false;
      }
    }
    return a.mValue < b.mValue;
  });

  for (auto const& mark : ranges) {
    auto stuff = mark.mEnd == End::Open ? "Open" : "Close";
    std::cout << mark.mValue << " " << stuff << std::endl;
  }

  {
    auto stack = std::stack<uint64_t>{};
    for (auto const& mark : ranges) {
      if (mark.mEnd == End::Open) {
        stack.push(mark.mValue);
      } else if (mark.mEnd == End::Close) {
        if (stack.size() == 1) {
          auto const& rangeBegin = stack.top();
          auto const& rangeEnd = mark.mValue;
          auto const valuesInRange = rangeEnd - rangeBegin + 1;
          ans2 += valuesInRange;
          // std::cout << rangeBegin << "-" << rangeEnd <<
        }
        stack.pop();
      }
    }
  }

  {
    auto stack = std::stack<bool>{};
    auto open = uint64_t{};
    auto lastValid = uint64_t{};

    for (auto const& mark : ranges) {
      if (mark.mEnd == End::Open) {
        if (stack.size() == 0) {
          open = mark.mValue;
        }
        stack.push(true);
      } else if (mark.mEnd == End::Close) {
        stack.pop();
        if (stack.size() == 0) {
          if (lastValid != mark.mValue) {
            lastValid = mark.mValue;
          }
          open = 0;
        }
      }
    }
  }

  while (std::getline(inputFile, line)) {
    auto const number = std::stoull(line);
    auto stack = std::stack<bool>{};
    for (auto i = size_t{}; i < ranges.size(); ++i) {
      if (ranges[i].mEnd == End::Open) {
        stack.push(true);
      }

      if (ranges[i].mEnd == End::Close) {
        stack.pop();
      }

      // First and onlytime number is in range
      if (InRange(ranges, number, i)) {
        if (stack.size() > 0) {
          ++ans1;
        }
        break;
      }
    }
  }

  std::cout << "ans1: " << ans1 << std::endl;
  std::cout << "ans2: " << ans2 << std::endl;

  return 0;
}