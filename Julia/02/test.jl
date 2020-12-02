using Test
using Logging
disable_logging(Logging.Info)

include("solution.jl")

password_policies = [
        (1, 3, 'a', "abcde"),
        (1, 3, 'b', "cdefg"),
        (2, 9, 'c', "ccccccccc")
        ]

@testset "main" begin
	@test solve_one(password_policies) == 2
	@test solve_two(password_policies) == 1
end