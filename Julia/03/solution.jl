function solve_one(geology::Array{Char, 2}, slope::Tuple{Int64, Int64})::Int64
	
	geology = geology.== '#'
	
	x, y = slope
	height, width = size(geology)
	run_width = ceil(- height / y * x)
	if width < run_width
        factor = convert(Int64, ceil(run_width / width))
        geology = repeat(geology, outer=(1, factor))
        width = size(geology)[2]
	end
	
	mask = mod.(transpose(reshape(1:(width * height), (width, height))) .- 1, width * - y + x) .== 0
    trees = sum(mask .* geology)

	@info(trees)
    return trees
end

function solve_two(geology::Array{Char, 2}, slopes::Array{Tuple{Int64, Int64}, 1})::Int64
	product = 1
	for slope in slopes
		product *= solve_one(geology, slope)
	end

	@info(product)
    return product
end
