function solve_one(expense_report::Array{Int64, 1}, total::Int64)::Union{Int64, Nothing}
	inverse = [total - x for x in expense_report]
    intersection = intersect(inverse, expense_report)
    if isempty(intersection)
        return
    end
    a, b = intersection
    product = a * b
    @info("$(a) * $(b) = $(product)")
    return product
end

function solve_two(expense_report::Array{Int64, 1}, total::Int64)::Union{Int64, Nothing}
    for c in expense_report
        new_total = total - c
        product = solve_one(expense_report, new_total)
        if isnothing(product)
            continue
        end
        @info("$(c) * $(product) = $(c * product)")
        return c * product
    end
end