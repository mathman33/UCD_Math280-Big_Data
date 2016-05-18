function w = weight(p1, p2)

	w = exp(-((norm(p1 - p2))^2)*100);
end
