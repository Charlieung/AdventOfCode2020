include("solution.jl")

# setup
current_directory = dirname(@__FILE__)
@info(current_directory)
input_path = string(current_directory, "/input.txt")
f = open(input_path, "r")
lines = readlines(f)
expense_report = [parse(Int, line) for line in lines]

# part 1
@info("[Part 1]")
@time solve_one(expense_report, 2020)

# part 2
@info("[Part 2]")
@time solve_two(expense_report, 2020)
