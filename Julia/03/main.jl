include("solution.jl")

# setup
current_directory = dirname(@__FILE__)
input_path = string(current_directory, "/input.txt")
f = open(input_path, "r")
lines = readlines(f)
geology = permutedims(hcat([[collect(c)[1] for c in split(line, "")] for line in lines]...))

slope = (3, -1)

slopes = [
    (1, -1),
    (3, -1),
    (5, -1),
    (7, -1),
    (1, -2),
    ]

# part 1
@info("[Part 1]")
@time solve_one(geology, slope)

# part 2
@info("[Part 2]")
@time solve_two(geology, slopes)
