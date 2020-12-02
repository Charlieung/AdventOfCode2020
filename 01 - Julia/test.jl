using Test
include("solution.jl")

expense_report = [1721, 979, 366, 299, 675, 1456]

@testset "main" begin
	@test solve_one(expense_report, 2020) == 514579
	@test solve_two(expense_report, 2020) == 241861950
end