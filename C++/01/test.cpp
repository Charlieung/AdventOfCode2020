#include <CppUnitTest.h>
#include <solution.h>
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

TEST_CLASS(TestSolution)
{
public:
  TEST_METHOD(TestSolveOne)
  {
    vector<int> numbers = {1721, 979, 366, 299, 675, 1456};
    int expected = 514579;
    optional<int> actual = solve_one(numbers, 2020);
    Assert::AreEqual(expected, *actual);
  }
  TEST_METHOD(TestSolveTwo)
  {
    vector<int> numbers = {1721, 979, 366, 299, 675, 1456};
    int expected = 241861950;
    optional<int> actual = solve_two(numbers, 2020);
    Assert::AreEqual(expected, *actual);
  }
};