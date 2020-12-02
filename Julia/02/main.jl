include("solution.jl")

# setup
current_directory = dirname(@__FILE__)
input_path = string(current_directory, "/input.txt")
f = open(input_path, "r")
lines = readlines(f)

# init array of types.
password_policies = Tuple{Int64, Int64, Char, String}[]

for line in lines
	policy, password = split(line, ": ")
	bounds, letter = split(policy, " ")
	letter = first(letter)
	min, max = split(bounds, "-")
	min, max = parse(Int, min), parse(Int, max)
	entry = min, max, letter, password
	push!(password_policies, entry)
end

# part 1
@info("[Part 1]")
@time solve_one(password_policies)

# part 2
@info("[Part 2]")
@time solve_two(password_policies)
