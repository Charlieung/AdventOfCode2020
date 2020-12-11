#include <string>
#include <vector>
#include <solution.h>

using namespace std;

int main()
{
    string input = read_file("input.txt");
    vector<int> numbers = parse_input(input);
    
    cout << "[Part 1]" << endl;
    optional<int> answer_one = solve_one(numbers, 2020);
    cout << "[Part 2]" << endl;
    optional<int> answer_two = solve_two(numbers, 2020);
}