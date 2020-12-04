using Test
using Logging
disable_logging(Logging.Info)

include("solution.jl")

geology = replace(strip("""
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """), "    " => "")

geology = permutedims(hcat([[collect(c)[1] for c in split(line, "")] for line in split(geology, '\n')]...))

slope = (3, -1)

slopes = [
    (1, -1),
    (3, -1),
    (5, -1),
    (7, -1),
    (1, -2),
    ]

@testset "main" begin
	@test solve_one(geology, slope) == 7
	@test solve_two(geology, slopes) == 336
end