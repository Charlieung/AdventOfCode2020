#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <tuple>
#include <optional>

using namespace std;

auto read_file(string_view path) -> string {
    constexpr auto read_size = size_t{4096};
    auto stream = ifstream{path.data()};
    stream.exceptions(ios_base::badbit);

    auto out = string{};
    auto buf = string(read_size, '\0');
    while (stream.read(& buf[0], read_size)) {
        out.append(buf, 0, stream.gcount());
    }
    
    out.append(buf, 0, stream.gcount());
    return out;
}

vector<int> parse_input (const string &s) {
    vector<int> result;
    stringstream ss (s);
    string item;

    int number;
    while (getline (ss, item, '\n')) {
        number = stoi(item);
        result.push_back(number);
    }

    return result;
}

optional<int> solve_one(vector<int> numbers, int total) {
    
    int value;
    int reciprocal;
    for (size_t i = 0; i < numbers.size(); i++)
    {
        value = numbers[i];
        reciprocal = total - value;
        if (find(numbers.begin(), numbers.end(), reciprocal) != numbers.end()) {
            int answer = value * reciprocal;
            cout << value << " * " << reciprocal << " = " << answer << endl;
            return answer;
        }
    }
    return nullopt;
}

optional<int> solve_two(vector<int> numbers, int total) {
    
    int value;
    int subtotal;
    for (size_t i = 0; i < numbers.size(); i++)
    {
        value = numbers[i];
        subtotal = total - value;
        optional<int> subproduct = solve_one(numbers, subtotal);
        if (subproduct.has_value()) {
            int answer = *subproduct * value;
            cout << *subproduct << " * " << value << " = " << answer << endl;
            return answer;
        }
    }
    return nullopt;
}

int main()
{
    string input = read_file("./cpp/01/input.txt");
    vector<int> numbers = parse_input(input);
    
    cout << "[Part 1]" << endl;
    optional<int> answer_one = solve_one(numbers, 2020);
    cout << "[Part 2]" << endl;
    optional<int> answer_two = solve_two(numbers, 2020);
}