#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::pair<std::size_t, std::size_t> GetStartEnd(const std::string& a_range); 
size_t InvalidId(const std::string& a_id);

int main() {
  auto ans1 = size_t{};

  auto input_file = std::ifstream{"input.txt"};
  const auto input_string = std::string{std::istreambuf_iterator<char>(input_file), std::istreambuf_iterator<char>()};
  const auto delimiter = std::string{","};
  auto ranges = std::vector<std::string>{};
  auto invalid_ids = std::vector<size_t>{};
  auto invalid_ids2 = std::vector<size_t>{};

  auto start_pos = std::size_t{};
  auto pos = std::size_t{};
  do {
    pos = input_string.find(delimiter, start_pos);
    const auto count = pos - start_pos;
    auto token = input_string.substr(start_pos, count);
    ranges.push_back(token);
    start_pos = start_pos + count + 1;
  } while (pos != std::string::npos);

  for (const auto& token : ranges) {
    const auto [start, end] = GetStartEnd(token);
    for (auto i = start; i <= end; ++i) {
      const auto num_string = std::to_string(i);
      const auto length = num_string.length();
      if (InvalidId(num_string) != 0 && std::find(invalid_ids2.begin(), invalid_ids2.end(), i) == invalid_ids2.end()) {
        invalid_ids2.push_back(i);
      }
      if (length % 2) {
        continue;
      }
      if (num_string.substr(0, length / 2) == num_string.substr(length / 2)) {
        if (std::find(invalid_ids.begin(), invalid_ids.end(), i) == invalid_ids.end()) {
          invalid_ids.push_back(i);
        }
        // std::cout << num_string << std::endl;
      }
    }
    std::cout << start << "," << end << std::endl;
  }

  for (const auto& id : invalid_ids) {
    ans1 += id;
  }

  auto ans2 = size_t{};
  for (const auto& id : invalid_ids2) {
    ans2 += id;
  }

  std::cout << "ans1: " << ans1 << std::endl;
  std::cout << "ans2: " << ans2 << std::endl;
  return 0;
}

std::pair<std::size_t, std::size_t> GetStartEnd(const std::string& a_range) {
  auto start_pos = std::size_t{};
  auto pos = std::size_t{};
  constexpr auto delimiter = "-";
  pos = a_range.find(delimiter, start_pos);
  const auto start = std::stoull(a_range.substr(start_pos, pos - start_pos));
  const auto end = std::stoull(a_range.substr(pos + 1));
  return {start, end};
}

size_t InvalidId(const std::string& a_id) {
  const auto id_length = a_id.length();
  for (auto sequence_length = size_t{1}; sequence_length <= id_length / 2; ++sequence_length) {
    if (id_length % sequence_length != 0) {
      continue;
    }

    // Find if the sequence is repeated
    auto invalid_id = true;
    auto pos = std::size_t{};
    const auto sequence = a_id.substr(0, sequence_length);
    do {
      if (sequence != a_id.substr(pos, sequence_length)) {
        invalid_id = false;
        break;
      }
      pos += sequence_length;
    } while (pos < id_length);
    if (invalid_id) {
      return std::stoull(a_id);
    }
  }
  return 0;
}
