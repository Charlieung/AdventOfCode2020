struct Passport
	
end

function parse_input(input::String)::Int64
	passports = []
	records = split(input, "\n\n")
	records = replace.(records, '\n'=>' ')
	for record in records		
		passport = Dict{String, String}()
		entries = split(record, ' ')
		for entry in entries
			key, value = split(entry, ':')
			passport[key] = value
		end
		push!(passports, passport)
	end
    return passports
end

function solve_one(passports::Array{Any, 1})::Int64
	
	valid_passports = 0
	@info(valid_passports)
    return valid_passports
end

function solve_two(passports::Array{Any, 1})::Int64

	valid_passports = 0
	@info(valid_passports)
    return valid_passports
end
