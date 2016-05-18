function Y = gen2vec(X,str_list,num_list);
% gen2vec - converts an array of strings to a matrix with numerical values
% 
% Usage: Y = gen2vec(X,str_list,num_list);
%            
% Example: X = ['AA','GG'];
%          str_list = ['AA';'TT';'GG';'CC';'AG';'AC';'TG';'TC';'--'];
%          num_list = [100;1-i,2;3;19;0;-2;1000;4]   (not that I would recommend this choice for num_list)
%          Y = gen2vec(X) gives Y = [100;2];

for k = 1:length(X)
    dummy = X{k};
    for j = 1:length(str_list);
        a = num_list(j,:);
        if isstr(num_list(j)) == 0;
           a = num2str(a);
        end
        dummy = strrep(dummy,str_list(j,:),a);
    end
    dummy = str2num(dummy);
    Y(k,:) = dummy;
end

          
