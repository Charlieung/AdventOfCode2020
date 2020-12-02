function solve_one(password_policies::Array{Tuple{Int64, Int64, Char, String}, 1})::Int64
	
	function is_password_valid(password_policy)
		min, max, letter, password = password_policy 
		letter_count = count(i->(i==letter), password)
		valid = min <= letter_count <= max 
		return valid
	end

	valid_policies = sum(is_password_valid.(password_policies))

	@info(valid_policies)
    return valid_policies
end

function solve_two(password_policies::Array{Tuple{Int64, Int64, Char, String}, 1})::Int64
	
	function is_password_valid(password_policy)
		min, max, letter, password = password_policy 
		valid = xor(password[min] == letter, password[max] == letter) 
		return valid
	end

	valid_policies = sum(is_password_valid.(password_policies))	

	@info(valid_policies)
    return valid_policies
end
