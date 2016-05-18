function A = get_adjacency(x)
	
	A = zeros(200, 200);
	for i = 1:200
		for j = 1:200
			A(i,j) = weight([x(1,i) x(2,i)], [x(1, j), x(2,j)]);
		end
	end

	A = A - eye(200);

end

