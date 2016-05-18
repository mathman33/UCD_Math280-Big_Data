function L = get_laplacian(A)

	D = zeros(200, 200);

	for i = 1:200
		D(i,i) = sum(A(i,:));
	end

	L = D - A;

end
