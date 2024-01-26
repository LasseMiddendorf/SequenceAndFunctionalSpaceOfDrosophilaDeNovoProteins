#!/home/bharat/julia-stable/bin/julia
using DelimitedFiles
using Distances

cd(Base.source_dir())

samples = ["random","denovo","conserved","consrand"]

if length(ARGS) > 2
	@warn "more than two arguments: only using first two"
end

if any(ARGS .∉ Ref(samples))
	@error "argument must be 'random', 'denovo', or 'conserved'"
end

println("Calculating pairwise distance between " * ARGS[1] * " and " * ARGS[2])

emb1 = readdlm(ARGS[1]*"_ESM2-650M-emb.csv", ',')';
emb2 = readdlm(ARGS[2]*"_ESM2-650M-emb.csv", ',')';


#id1 = readdlm(ARGS[1]*"_id.csv", ',');
#id2 = readdlm(ARGS[1]*"_id.csv", ',');


#manhattan(x,y) = sum(abs.(x .- y))

distmat = pairwise(cityblock,emb1, emb2, dims = 2);

writedlm(ARGS[1]*"-"*ARGS[2]*"_dist.txt",distmat)