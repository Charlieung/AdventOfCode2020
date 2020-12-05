include("solution.jl")

# setup
current_directory = dirname(@__FILE__)
input_path = string(current_directory, "/input.txt")
f = open(input_path, "r")
passports = parse_input(read(f))

# part 1
@info("[Part 1]")
@time solve_one(passports)

# part 2
@info("[Part 2]")
@time solve_two(passports)

