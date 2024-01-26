#!/home/bharat/julia-stable/bin/julia
using DelimitedFiles
cd(Base.source_dir())

samples = ["random","denovo","conserved"]

if length(ARGS) > 2
	@warn "more than one argument: only using the first two"
end

n = parse(Int,ARGS[2])

distlist = eachrow(readdlm(ARGS[1]));

snames = split(replace(ARGS[1],r"_.*" => ""),"-")

id1 = readdlm(snames[1]*"_ids.txt");
id2 = readdlm(snames[2]*"_ids.txt");


nearest = fill(Vector{Int}(), (length(distlist), n));

nearest[:,1] = [findall(x .== minimum(x)) for x in distlist];


if(n > 1)
	ixs = eachindex(distlist[1])
	vcn = (x,k) -> setdiff(ixs,vcat(nearest[x,1:k-1]...))
	for k = 2:n
		nearest[:,k] = [findall(distlist[x] .== minimum(distlist[x][vcn(x,k)])) for x in eachindex(distlist)]
	end
end

outfile = snames[1]*"-"*snames[2]*"_1-"*string(n)*"-nearest_neighbors.txt"

open(outfile,"w") do fout
	for i = 1:n
		q = [length(x) for x in nearest[:,i]];
		qix = vcat([y*ones(Int,q[y]) for y in eachindex(q)]...);
		tix = vcat(nearest[:,i]...);
		qid = id1[qix];
		tid = id2[tix];
		dist = [distlist[qix[x]][tix[x]] for x in eachindex(qix)];
		writedlm(fout,hcat(qid,i*ones(Int,length(qid)),tid,dist))
	end
end