function solve_one(password_policies::Array{Tuple{Int64, Int64, Char, String}, 1})::Union{Int64, Nothing}
	valid_policies = 0
	for password_policy in password_policies
		min, max, letter, password = password_policy 
		letter_count = count(i->(i==letter), password)
		if min <= letter_count <= max
			valid_policies += 1
		end
	end
	@info(valid_policies)
    return valid_policies
end

function solve_two(password_policies::Array{Tuple{Int64, Int64, Char, String}, 1})::Union{Int64, Nothing}
	valid_policies = 0
	for password_policy in password_policies
		min, max, letter, password = password_policy 
		if xor(password[min] == letter, password[max] == letter) 
			valid_policies += 1
		end
	end
	@info(valid_policies)
    return valid_policies
end
